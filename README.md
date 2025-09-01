🎬 BookMyShow Analysis – SQL Project
📌 Project Overview

This project is an SQL-based analysis of BookMyShow-like data, designed to explore insights from movies, users, and bookings. Using structured queries, the project demonstrates data modeling, relational schema design, joins, aggregations, and analytical SQL queries to uncover trends such as most popular movies, user preferences, and revenue generation.

It serves as a real-life use case for applying SQL concepts in the entertainment domain.

🗂️ Dataset Description

The dataset is structured into multiple tables with primary and foreign key relationships.

Tables:

Users – Stores information about registered users

Movies – Contains details like movie title, genre, language, release date, and ratings

Theatres – Theatre details including location and seating capacity

Bookings – Tracks tickets booked by users for specific movies and shows

Payments – Payment details for transactions

⚙️ Features & Analysis

📊 Movie Insights: Find highest-rated, most popular, and trending movies

👥 User Insights: Analyze user booking behavior

🎭 Genre & Language Trends: Identify audience preferences

💰 Revenue Analysis: Track earnings from bookings & theatres

📍 Theatre Analysis: Find most crowded theatres and occupancy trends

🛠️ Tech Stack

Database: MySQL / PostgreSQL (can adapt)

Query Language: SQL

Tools: MySQL Workbench / DBeaver / pgAdmin (for execution & visualization)

📂 Project Structure
BookMyShow-SQL-Analysis/
│── dataset/            # CSV files for movies, users, theatres, bookings, payments
│── schema.sql          # Database schema with PK & FK constraints
│── insert_data.sql     # Insert queries for populating tables
│── analysis_queries.sql# SQL queries for analysis
│── results/            # Query results (screenshots/exports)
│── README.md           # Project documentation

🚀 How to Run

Clone this repository:

git clone https://github.com/your-username/BookMyShow-SQL-Analysis.git
cd BookMyShow-SQL-Analysis


Import schema and data into your SQL environment:

SOURCE schema.sql;
SOURCE insert_data.sql;


Run analysis queries:

SOURCE analysis_queries.sql;

📈 Sample Queries

🔹 Top 5 highest-rated movies:

SELECT title, rating 
FROM Movies 
ORDER BY rating DESC 
LIMIT 5;


🔹 Most popular genre by total bookings:

SELECT m.genre, COUNT(b.booking_id) AS total_bookings
FROM Bookings b
JOIN Movies m ON b.movie_id = m.movie_id
GROUP BY m.genre
ORDER BY total_bookings DESC;

🎯 Learning Outcomes

Database design with primary & foreign keys

Writing complex SQL queries with joins, aggregations, and subqueries

Performing real-life business analysis using SQL

Improving data handling and problem-solving skills

📌 Future Scope

Add Streamlit dashboard for visualization

Integrate with Python (Pandas + SQLAlchemy) for deeper analysis

Include real-time API-based dataset

👨‍💻 Author
Kavish Nag

Kashish Chelwani

Kunal Jhindal
