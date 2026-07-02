import random
import pandas as pd

from faker import Faker

from database.connection import engine

fake = Faker()


def generate_data(n=1000):

    departments = [
        "HR",
        "Engineering",
        "Sales",
        "Marketing",
        "Finance"
    ]

    cities = [
        "Hyderabad",
        "Bangalore",
        "Chennai",
        "Mumbai",
        "Pune",
        "Delhi"
    ]

    records = []

    for emp_id in range(1, n + 1):

        records.append(
            {
                "employee_id": emp_id,
                "name": fake.name(),
                "department": random.choice(departments),
                "salary": random.randint(50000, 200000),
                "experience": random.randint(1, 15),
                "city": random.choice(cities),
                "joining_year": random.randint(2015, 2025)
            }
        )

    df = pd.DataFrame(records)

    df.to_sql(
        "employees",
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"\nGenerated {n} employee records successfully.")


if __name__ == "__main__":
    generate_data()