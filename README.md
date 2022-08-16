
# Project-Data-Modeling-with-Postgres

In this project, We've done data modeling with Postgres and build an ETL pipeline using Python. We've defined fact and dimension tables for a star schema for a startup company called Sparkify, and wrote an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [description_of_files](#Description_of_files)
* [Setup](#setup)



## General Information
- Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong
(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location,user_agent)
- Dimension Tables
users - users in the app (user_id, first_name, last_name, gender, level)
songs - songs in music database (song_id, title, artist_id, year, duration)
artists - artists in music database (artist_id, name, location, latitude, longitude)
time - timestamps of records in songplays broken down into specific units (start_time, hour, day, week, month, year, weekday)


## Technologies Used
- PostgreSQL
- Python 

## Description of files
- test.ipynb displays the first few rows of each table to let you check your database.
- create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
- etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
- etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
- sql_queries.py contains all your sql queries, and is imported into the last three files above.

## setup
- run create_tables.py
- run etl.ipynb
- run etl.py
- run test.ipynb



