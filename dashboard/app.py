import os
from flask import Flask, render_template, request, jsonify
import pymysql

# --- Database Configuration (UPDATE THIS!) ---
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'sit123',  # <-- CHANGE THIS TO YOUR ACTUAL PASSWORD
    'database': 'bookmyshow',
    'cursorclass': pymysql.cursors.DictCursor
}
# --------------------------------------------

app = Flask(__name__)

def get_db_connection():
    """Establishes a MySQL connection."""
    try:
        return pymysql.connect(**DB_CONFIG)
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def fetch_filter_options():
    """Fetches unique values for filter categories."""
    conn = get_db_connection()
    if not conn: return {}
    
    try:
        with conn.cursor() as cursor:
            # Fetch distinct genres
            cursor.execute("SELECT DISTINCT genre FROM Movies ORDER BY genre;")
            genres = [row['genre'] for row in cursor.fetchall()]

            # Fetch distinct languages
            cursor.execute("SELECT DISTINCT language FROM Movies ORDER BY language;")
            languages = [row['language'] for row in cursor.fetchall()]
            
            # Fetch distinct theater chains
            cursor.execute("SELECT DISTINCT name FROM Theaters ORDER BY name;")
            theaters = [row['name'] for row in cursor.fetchall()]
            
            # Fetch distinct cities
            cursor.execute("SELECT DISTINCT city FROM Theaters ORDER BY city;")
            cities = [row['city'] for row in cursor.fetchall()]

        return {
            'genres': genres,
            'languages': languages,
            'theaters': theaters,
            'cities': cities
        }
    finally:
        conn.close()

def fetch_movies(filters, sort_by):
    """Fetches movies applying filters and sorting."""
    conn = get_db_connection()
    if not conn: return []

    # Base query combining Movie, Review (for avg_rating), Schedule, and Theater info
    query_parts = [
        """
        SELECT 
            m.movie_id,
            m.title,
            m.genre,
            m.language,
            m.duration,
            m.rating AS actual_rating,
            t.name AS theater_name,
            t.city,
            t.state,
            AVG(r.rating) AS avg_user_rating,
            COUNT(r.review_id) AS total_reviews
        FROM Movies m
        JOIN Schedule s ON m.movie_id = s.movie_id
        JOIN Theaters t ON s.theater_id = t.theater_id
        LEFT JOIN Reviews r ON m.movie_id = r.movie_id
        WHERE 1=1
        """
    ]
    
    params = []
    
    # --- Apply Filters (from phase 2.ipynb implied logic) ---
    if filters.get('genre'):
        query_parts.append(" AND m.genre = %s")
        params.append(filters['genre'])
    
    if filters.get('language'):
        query_parts.append(" AND m.language = %s")
        params.append(filters['language'])

    if filters.get('city'):
        query_parts.append(" AND t.city = %s")
        params.append(filters['city'])
        
    if filters.get('theater'):
        query_parts.append(" AND t.name = %s")
        params.append(filters['theater'])
        
    if filters.get('search_term'):
        query_parts.append(" AND m.title LIKE %s")
        params.append(f"%{filters['search_term']}%")

    # --- Grouping and Ordering ---
    query_parts.append(" GROUP BY m.movie_id, m.title, m.genre, m.language, m.duration, m.rating, t.name, t.city, t.state")
    
    # --- Apply Sorting (from phase 2.ipynb implied logic) ---
    if sort_by == 'rating_desc':
        query_parts.append(" ORDER BY avg_user_rating DESC, total_reviews DESC")
    elif sort_by == 'rating_asc':
        query_parts.append(" ORDER BY avg_user_rating ASC, total_reviews ASC")
    elif sort_by == 'reviews_desc':
        query_parts.append(" ORDER BY total_reviews DESC, avg_user_rating DESC")
    elif sort_by == 'title_asc':
        query_parts.append(" ORDER BY m.title ASC")
    else:
        # Default sort
        query_parts.append(" ORDER BY m.title ASC")
        
    final_query = "".join(query_parts)
    
    try:
        with conn.cursor() as cursor:
            # print(f"Executing query: {final_query} with params {params}") # Debugging
            cursor.execute(final_query, tuple(params))
            results = cursor.fetchall()

        # Deduplicate movies by selecting a representative theater/city if needed
        # Since the query groups by theater/city, we get multiple rows per movie/theater combo. 
        # For the final output, let's group logically on the backend side to show unique movies with relevant info.
        
        # A simple hack to combine multiple theater showings for one movie in one row:
        movie_map = {}
        for row in results:
            movie_id = row['movie_id']
            if movie_id not in movie_map:
                movie_map[movie_id] = {
                    'movie_id': row['movie_id'],
                    'title': row['title'],
                    'genre': row['genre'],
                    'language': row['language'],
                    'duration': row['duration'],
                    'avg_user_rating': f"{row['avg_user_rating']:.1f}" if row['avg_user_rating'] is not None else "N/A",
                    'total_reviews': row['total_reviews'],
                    'locations': []
                }
            
            location_string = f"{row['theater_name']} ({row['city']}, {row['state']})"
            if location_string not in movie_map[movie_id]['locations']:
                movie_map[movie_id]['locations'].append(location_string)
        
        # Convert map back to list, ensuring sorting is retained (Python dict iteration preserves insertion order after 3.7)
        final_list = list(movie_map.values())
        
        # Apply secondary sort if necessary (or just stick with the SQL sort from the grouped view)
        # Since the main display unit is the movie, sorting is mostly fine.

        return final_list

    finally:
        conn.close()


@app.route('/')
def index():
    """Renders the main dashboard page with initial filter options."""
    filter_options = fetch_filter_options()
    return render_template('index.html', options=filter_options)

@app.route('/api/movies', methods=['POST'])
def api_movies():
    """API endpoint to get filtered and sorted movie data."""
    data = request.json
    
    filters = {
        'genre': data.get('genre'),
        'language': data.get('language'),
        'city': data.get('city'),
        'theater': data.get('theater'),
        'search_term': data.get('search_term')
    }
    
    sort_by = data.get('sort_by', 'title_asc')
    
    movie_list = fetch_movies(filters, sort_by)
    
    return jsonify({'movies': movie_list})

if __name__ == '__main__':
    # You must run this command in your terminal/notebook to create the necessary functions:
    # python -c "import pymysql; con = pymysql.connect(host='localhost', user='root', password='010824@Symbi', database='bookmyshow'); cur = con.cursor(); cur.execute('CREATE FUNCTION getMovieRating(movie_id INT) RETURNS FLOAT DETERMINISTIC BEGIN DECLARE avg_rating FLOAT; SELECT AVG(rating) INTO avg_rating FROM Reviews WHERE Reviews.movie_id = movie_id; RETURN avg_rating; END;'); con.close()"
    # NOTE: The provided SQL in the notebook relies on MySQL functions like `AVG()`, `COUNT()` 
    # and implicitly relies on a combined view. The Flask app here uses the raw tables 
    # to perform the aggregation directly, which is more conventional for a backend.
    
    app.run(debug=True, port=5000)