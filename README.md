#Name
Ella Zhang

#Description of bookstore
This project is a command-line bookstore application built with SQLite and Python. It uses a relational database called `bookstore.db` to store bookstore information and a Python CLI (`bookstore_cli.py`) to let users interact with the data.

The goal is to:
- design a relational database
- populate it with meaningful sample data
- interact with it using SQL and Python

The system allows users to browse, search, and manage books in a structured and user-friendly way.

#structure
The project consists of the following files:
- `createTables.sql`: defines the database structure  
- `insertRows.sql`: inserts sample data  
- `bookstore_cli.py`: Python program for interacting with the database  
- `bookstore.db`: SQLite database file (generated during setup)  

#Create the database
1. Run: sqlite3 bookstore.db < createTables.sql
This command:
- creates the file bookstore.db (if it does not exist)
- creates the category and book tables

Insert sample data
2. Run: sqlite3 bookstore.db < insertRows.sql
This command:
- inserts categories and books into the database

#run the Python program
3. Run: python3 bookstore_cli.py





