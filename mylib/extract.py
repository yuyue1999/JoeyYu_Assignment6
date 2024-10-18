import requests
customersUrl="https://raw.githubusercontent.com/yuyue1999/ids_assignment6_data/refs/heads/main/customers.csv"
customersPath="customers.csv"
ordersUrl="https://raw.githubusercontent.com/yuyue1999/ids_assignment6_data/refs/heads/main/orders.csv"
ordersPath="orders.csv"

def extract():
    try:
        response1 = requests.get(customersUrl, timeout=10)
        response1.raise_for_status()
        with open(customersPath, "wb") as f1:
            f1.write(response1.content)

        response2 = requests.get(ordersUrl, timeout=10)
        response2.raise_for_status()
        with open(ordersPath, "wb") as f2:
            f2.write(response2.content)
        return "success"
    
    except (requests.exceptions.RequestException, OSError) as e:
        print(f"An error occurred: {e}")
        return "failure"

if __name__ == "__main__":
    extract()