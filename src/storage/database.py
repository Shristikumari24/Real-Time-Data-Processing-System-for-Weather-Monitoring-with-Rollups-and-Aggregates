import sqlite3

class Database:
    def _init_(self):
        self.conn = sqlite3.connect('weather_data.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summaries (
            date INTEGER PRIMARY KEY,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
        ''')
        self.conn.commit()

    def update_daily_summary(self, summary):
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT OR REPLACE INTO daily_summaries 
        (date, avg_temp, max_temp, min_temp, dominant_condition) 
        VALUES (?, ?, ?, ?, ?)
        ''', (summary['date'], summary['avg_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
        self.conn.commit()

    def get_daily_summaries(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM daily_summaries ORDER BY date DESC LIMIT 7')
        return cursor.fetchall()

