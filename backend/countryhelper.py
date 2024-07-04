import sqlite3
import random

def main():
    random_country = Country.get_random_country()
    print(random_country)


class Country:
    def __init__(self, country_name, country_code, continent, country_flag, dish_name, cooked):
        self.country_name = country_name
        self.country_code = country_code
        self.continent = continent
        self.country_flag = country_flag
        self.dish_name = dish_name
        self.cooked = cooked

    def __repr__(self):
        return f"{self.country_name} ({self.country_code}) - {self.continent} - {self.dish_name} - see flag: {self.country_flag} - cooked: {self.cooked}"

    @classmethod
    def get_random_country(cls, db_path):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM countries")
        count = cursor.fetchone()[0]

        # Wähln ein zufälliges Land aus
        random_id = random.randint(1, count)
        cursor.execute("SELECT country_name, country_code, continent, country_flag, dish_name, cooked FROM countries WHERE id = ?", (random_id,))

        result = cursor.fetchone()
        connection.close()

        if result:
            return cls(*result)  # Erstelle ein Country-Objekt mit den geladenen Daten
        else:
            return None


if __name__ == "__main__":
    main()

