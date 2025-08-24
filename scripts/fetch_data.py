import os
import requests
import psycopg2
from datetime import datetime

def fetch_and_store():
    API_KEY = os.getenv("API_KEY")
    SYMBOL = "AAPL"  # Example stock (Apple)

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval=1min&apikey={API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()

        time_series = data.get("Time Series (1min)", {})
        if not time_series:
            print("⚠️ No data received from API.")
            return


        latest_timestamp, latest_data = list(time_series.items())[0]
        price = float(latest_data["1. open"])
        volume = int(latest_data["5. volume"])


        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host="postgres",   
            port=os.getenv("POSTGRES_PORT")
        )
        cur = conn.cursor()


        cur.execute("""
            CREATE TABLE IF NOT EXISTS stock_data (
                id SERIAL PRIMARY KEY,
                symbol VARCHAR(10),
                price NUMERIC,
                volume BIGINT,
                timestamp TIMESTAMP
            )
        """)

        cur.execute(
            "INSERT INTO stock_data (symbol, price, volume, timestamp) VALUES (%s, %s, %s, %s)",
            (SYMBOL, price, volume, datetime.strptime(latest_timestamp, "%Y-%m-%d %H:%M:%S"))
        )

        conn.commit()
        cur.close()
        conn.close()

        print("✅ Data inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")
