import os
import pandas as pd
from databricks import sql
from dotenv import load_dotenv
dataset_customers="customers.csv"
dataset_orders="orders.csv"
def load_data_to_db():
    df_customers_data = pd.read_csv(dataset_customers)[
        ["customer_id", "customer_name", "customer_city"]
    ]
    df_orders_data = pd.read_csv(dataset_orders)[
        ["order_id", "customer_id", "order_amount", "order_date"]
    ]

    # Step 2: Load environment variables for database connection
    load_dotenv()
    server_hostname = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("DATABRICKS_KEY")
    http_path = os.getenv("HTTP_PATH")

    # Step 3: Connect to Databricks SQL Warehouse
    with sql.connect(
        server_hostname=server_hostname, http_path=http_path, access_token=access_token
    ) as conn:
        with conn.cursor() as c:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS customersyy (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    customer_city VARCHAR(255) NOT NULL
);"""
            )
            if not df_customers_data.empty:
                values = [tuple(row) for row in df_customers_data.values]
                string_sql = (
                    "INSERT INTO customersyy"
                    "(customer_id, customer_name, customer_city) VALUES"
                )
                string_sql += "\n" + ",\n".join([str(v) for v in values]) + ";"
                c.execute(string_sql)

            c.execute(
                """
                CREATE TABLE  IF NOT EXISTS ordersyy (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_amount DECIMAL(10, 2),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customersyy(customer_id)
);"""
            )
            if not df_orders_data.empty:
                values = [tuple(row) for row in df_orders_data.values]
                string_sql = (
                    "INSERT INTO ordersyy "
                    "(order_id, customer_id, order_amount, order_date) VALUES"
                )
                string_sql += "\n" + ",\n".join([str(v) for v in values]) + ";"
                c.execute(string_sql)
            conn.commit()
            return "success"


if __name__ == "__main__":
    result = load_data_to_db()


