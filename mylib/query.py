from databricks import sql
from dotenv import load_dotenv
import os


# Query module for the HR database
complex_query = """
SELECT c.customer_name, c.customer_city, COUNT(o.order_id) AS total_orders, SUM(o.order_amount) AS total_spent
FROM customersyy c
JOIN ordersyy o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.customer_city
HAVING total_spent > 300
ORDER BY total_spent DESC;

"""

# Load environment variables for Databricks connection
load_dotenv()
server_hostname = os.getenv("SERVER_HOSTNAME")
access_token = os.getenv("DATABRICKS_KEY")
http_path = os.getenv("HTTP_PATH")

def run_query():
    with sql.connect(
        server_hostname=server_hostname, 
        http_path=http_path, 
        access_token=access_token
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(complex_query)
            query_result = cursor.fetchall()
            for row in query_result:
                print(row)
            return "success"  

# Execute the complex query when the script runs
if __name__ == "__main__":
    result = run_query()
