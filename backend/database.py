import sqlite3
import csv

def main():
    con = sqlite3.connect('data/cdw-database.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS countries (id INTEGER PRIMARY KEY, country_name TEXT, country_code TEXT, continent TEXT, 
                country_flag TEXT, dish_name TEXT, cooked BOOLEAN DEFAULT FALSE)""")
    con.commit()
    con.close()

def load_countries():
    path = 'data/countries_list.csv'
    db = sqlite3.connect('data/cdw-database.db')
    cursor = db.cursor()
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            country_code = row['country_code']
            country_flag = f"https://flagsapi.com/{country_code}/shiny/64.png"
            cursor.execute("INSERT INTO countries (country_name, country_code, continent, country_flag, dish_name) VALUES (?, ?, ?, ?, ?)",
                        (row['country_name'], country_code, row['continent'], country_flag, row['dish']))
    db.commit()
    db.close()
    remove_duplicates()

def remove_duplicates():
    db = sqlite3.connect('data/cdw-database.db')
    cursor = db.cursor()
    cursor.execute("""
        DELETE FROM countries
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM countries
            GROUP BY country_name, country_code
        )
    """)
    db.commit()
    db.close()

def database_manipulater():
    db = sqlite3.connect('data/cdw-database.db')
    cursor = db.cursor()
    cursor.execute("""UPDATE countries SET dish_name = 'Pasta alla papalina' 
                   WHERE country_code = 'VA'""")
                   
    db.commit()
    db.close()

if __name__ == "__main__":
    main()
    database_manipulater()