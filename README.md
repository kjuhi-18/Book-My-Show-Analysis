🎬 BookMyShow Analysis – SQL Project
📌 Project Overview

This project is a SQL-based analysis of BookMyShow data, designed to explore movie details, user bookings, payments, theatres, and more.
It demonstrates database design, relationships (PK–FK), and analytical queries that extract insights about movies and user engagement.

ppt link:https://yogicshifu.my.canva.site/dcdslppt

🗂️ Dataset & Tables

The project contains 9 tables with proper Primary Key (PK) and Foreign Key (FK) references:

Table Name	Description

🎥 movies	Stores movie details like title, genre, language, duration, rating, and release date

👤 users	Stores user details such as name, email, and location

🎟️ bookings	Stores ticket booking information linked with users and movies

💳 payments	Handles booking payment details

🏢 theatres	Theatre information including name, location, and screens

📅 shows	Show timings mapped to theatres and movies

💺 seats	Seat details for each show

🎫 tickets	Ticket details linked with bookings

⭐ reviews	User reviews and ratings for movies

🏗️ Database Schema

ER Diagram
    
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

⚙️ Features

✅ Relational Database Design with 9 tables
✅ Primary Key & Foreign Key constraints
✅ Data insertion with sample dataset (movies, users, bookings, etc.)
✅ SQL queries for insights such as:

Top-rated movies 🎞️

Most active users 👥

Highest-grossing movies 💰

Theatre-wise show analysis 🏢

🚀 How to Run

Clone this repository

git clone https://github.com/your-username/bookmyshow-sql-analysis.git
cd bookmyshow-sql-analysis


Set up MySQL Database

CREATE DATABASE bookmyshow;
USE bookmyshow;


Create Tables
Run the create_tables.sql script (includes all 9 tables with constraints).

Insert Data
Run the insert_data.sql script to load sample data.

Run Queries
Execute queries from analysis_queries.sql to get insights.

📊 Sample Query & Output

Query: Find top 5 highest-rated movies

SELECT title, genre, rating
FROM movies
ORDER BY rating DESC
LIMIT 5;


Output:

Title	Genre	Rating

Ready road establish	Romance	8.8

Day prevent	Comedy	8.3

While institution	Comedy	8.2

Important true	Action	8.1

Night mind	Romance	8.0

🛠️ Tech Stack

Database: MySQL 🐬

Language: SQL

Visualization (Optional): Power BI / Tableau 📈

📌 Future Enhancements

🔹 Add stored procedures & triggers for automation

🔹 Build a Streamlit dashboard for visual insights

🔹 Expand dataset with real-world BookMyShow-like data
