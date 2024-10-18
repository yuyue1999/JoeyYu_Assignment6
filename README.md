

# Database Schema and Query Explanation

## 1. **Table Structure**

### Customers Table
The `customers` table stores information about customers, with the following columns:
- `customer_id` (INT, PRIMARY KEY): A unique identifier for each customer.
- `customer_name` (VARCHAR(255), NOT NULL): The name of the customer.
- `customer_city` (VARCHAR(255), NOT NULL): The city where the customer resides.

```sql
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    customer_city VARCHAR(255) NOT NULL
);
```

### Orders Table
The `orders` table stores information about customer orders, with the following columns:
- `order_id` (INT, PRIMARY KEY): A unique identifier for each order.
- `customer_id` (INT, FOREIGN KEY): A reference to the `customer_id` in the `customers` table, establishing a relationship between a customer and their orders.
- `order_amount` (DECIMAL(10, 2)): The monetary value of the order.
- `order_date` (DATE): The date the order was placed.

```sql
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_amount DECIMAL(10, 2),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

## 2. **SQL Query Explanation**

```sql
SELECT c.customer_name, c.customer_city, COUNT(o.order_id) AS total_orders, SUM(o.order_amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.customer_city
HAVING total_spent > 300
ORDER BY total_spent DESC;
```

### Explanation of the Query:

- **SELECT**: The query selects the `customer_name` and `customer_city` from the `customers` table, along with two aggregate values:
  - `total_orders`: The total number of orders placed by the customer.
  - `total_spent`: The total monetary value of all orders placed by the customer.

- **JOIN**: A `JOIN` is performed between the `customers` and `orders` tables using the `customer_id` field. This allows us to link the customers to their respective orders.

- **GROUP BY**: The query groups the results by the `customer_id`, `customer_name`, and `customer_city`. This ensures that the aggregate values are calculated per customer.

- **Aggregation**: 
  - `COUNT(o.order_id)` counts the number of orders each customer has placed.
  - `SUM(o.order_amount)` calculates the total amount spent by each customer.

- **HAVING**: The `HAVING` clause filters the results to only include customers who have spent more than 300.

- **ORDER BY**: The results are sorted in descending order (`DESC`) based on the total amount spent (`total_spent`), so the customers who spent the most appear at the top.

### Purpose of the Query:
This query provides insights into customer spending behavior by summarizing the total number of orders and the total amount spent by each customer. It only returns customers who have spent more than 300 units and sorts them by the highest spenders.

### Resultof the Query:

Row(customer_name='Charlie', customer_city='Chicago', total_orders=20, total_spent=Decimal('14000.00'))
Row(customer_name='Alice', customer_city='New York', total_orders=40, total_spent=Decimal('14000.00'))
Row(customer_name='David', customer_city='Houston', total_orders=20, total_spent=Decimal('6000.00'))
Row(customer_name='Bob', customer_city='Los Angeles', total_orders=20, total_spent=Decimal('2000.00'))

