# 🎬 BookMyShow Analysis — SQL Project  

> 🧠 *A structured SQL project that explores movie data, user bookings, theatres, and payments through relational database design and analytical queries.*  

---

<p align="center">
  <img src="https://img.shields.io/badge/MySQL-Database-orange?logo=mysql" />
  <img src="https://img.shields.io/badge/SQL-Structured_Query_Language-blue?logo=databricks" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
  <img src="https://img.shields.io/badge/Data%20Modeling-ERD-red" />
</p>

---

## 📌 Project Overview  

This project is a **SQL-based analysis** of BookMyShow-like data, designed to simulate how online ticketing systems manage and analyze data.  
It demonstrates:  
- **Relational database design** with normalized tables  
- **Primary/Foreign Key relationships**  
- **Data insertion and queries** for actionable insights  
- **Real-world analysis** of movies, users, bookings, and revenue  



---

## 🗂️ Dataset & Tables  

The project uses **9 tables**, each carefully designed with PK–FK relationships to ensure relational integrity.

| Table | Description |
|-------|--------------|
| 🎥 **movies** | Stores movie details (title, genre, language, duration, rating, release date) |
| 👤 **users** | Stores user info such as name, email, location |
| 🎟️ **bookings** | Ticket booking info linked with users and movies |
| 💳 **payments** | Payment details associated with each booking |
| 🏢 **theatres** | Theatre name, location, and number of screens |
| 📅 **shows** | Show timings mapped to theatres and movies |
| 💺 **seats** | Seat details and availability per show |
| 🎫 **tickets** | Ticket details linked with bookings |
| ⭐ **reviews** | User reviews and ratings for movies |

---

## 🏗️ Database Schema — ER Diagram  

```
users ||--o{ bookings : places
movies ||--o{ bookings : includes
bookings ||--o{ payments : has
movies ||--o{ shows : scheduled
theatres ||--o{ shows : hosts
shows ||--o{ seats : contains
seats ||--o{ tickets : booked
bookings ||--o{ tickets : generates
users ||--o{ reviews : writes
movies ||--o{ reviews : receives
```

Each relationship reflects a **real-world mapping** between entities in the BookMyShow system.

---

## ⚙️ Features  

✅ **Relational Database Design** — with 9 normalized tables  
✅ **Primary & Foreign Key Constraints** — ensuring referential integrity  
✅ **Automated Data Insertion** — using Python + SQL scripts  
✅ **Analytical SQL Queries** — to extract valuable business insights  
✅ **Reusable Architecture** — can be extended for real-time dashboards  

---

## 🧠 Automated Database Creation  

📘 **Notebook:** [`making tables and insertion through python`](https://github.com/kjuhi-18/Book-My-Show-Analysis/blob/main/Notebooks/making%20tables%20and%20insertion%20thorugh%20python)  

This notebook automates the entire database setup using Python and MySQL Connector:  
- Creates the database `bookmyshow`  
- Generates all 9 tables with constraints  
- Inserts sample data automatically  
- Verifies data with SQL queries  

🔧 This eliminates the need for manual SQL entry, ensuring quick setup and reproducibility.  

---

## 🚀 How to Run  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Kavish-Nag/bookmyshow-sql-analysis.git
cd bookmyshow-sql-analysis
```

### 2️⃣ Setup MySQL Database  
```sql
CREATE DATABASE bookmyshow;
USE bookmyshow;
```

### 3️⃣ Run the Automation Notebook  
Open the Jupyter Notebook:  
[`making tables and insertion through python`](https://github.com/kjuhi-18/Book-My-Show-Analysis/blob/main/Notebooks/making%20tables%20and%20insertion%20thorugh%20python)  

This notebook automatically:  
- Creates all **9 relational tables** with primary and foreign keys  
- Inserts the **sample dataset** into each table  
- Runs basic SQL **queries and verifications** for data integrity  

No manual SQL scripting required — the entire database setup and data insertion are handled seamlessly within the notebook. 🚀  

---

## 🧩 Tech Stack  

| Category | Tools |
|-----------|--------|
| **Database** | MySQL 🐬 |
| **Language** | SQL |
| **Automation** | Python (MySQL Connector) |
| **Documentation** | Canva, PowerPoint, Word |

---

## 📈 Insights Generated  

✅ Top 10 highest-rated movies 🎞️  
✅ Most frequent users 👥  
✅ Revenue per movie 💰  
✅ Theatre performance by city 🏙️  
✅ Payment mode analysis 💳  

---

## 📌 Future Enhancements  

🔹 Add **stored procedures & triggers** for automation  
🔹 Build a **Streamlit dashboard** for live visualization  
🔹 Expand dataset with **real-world movie booking data**  
🔹 Integrate with **Power BI / Tableau** for visual reporting  

---

## 👨‍💻 Contributors  

| Name |
|------|
| **Kavish Nag** |
| **Kunal Jhindal** |
| **Kashish Chelwani** |

---

## 🪪 License  

Licensed under the **MIT License** — open for academic and personal use.  

---

## 🌟 Support  

⭐ **Star this repo** if you found it useful!  
💬 Feedback and contributions are always welcome.  


---

> 💡 *Data doesn’t just tell stories — it sells tickets too.* 🎫  

---
