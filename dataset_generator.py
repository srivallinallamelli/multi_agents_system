import pandas as pd
import random

from sqlalchemy import text

from database.connection import engine


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


def fetch_output(sql):

    with engine.connect() as conn:

        result = conn.execute(
            text(sql)
        )

        rows = [
            dict(r._mapping)
            for r in result
        ]

    return rows


def generate_dataset(n=100):

    data = []

    for _ in range(n):

        query_type = random.choice([
            "department",
            "city",
            "salary"
        ])

        if query_type == "department":

            dept = random.choice(departments)

            query = (
                f"Show employees in {dept} department"
            )

            sql = (
                f"SELECT * FROM employees "
                f"WHERE department='{dept}'"
            )

        elif query_type == "city":

            city = random.choice(cities)

            query = (
                f"Show employees in {city}"
            )

            sql = (
                f"SELECT * FROM employees "
                f"WHERE city='{city}'"
            )

        else:

            salary = random.randint(
                70000,
                150000
            )

            query = (
                f"Show employees earning more than {salary}"
            )

            sql = (
                f"SELECT * FROM employees "
                f"WHERE salary>{salary}"
            )

        expected_output = fetch_output(sql)

        data.append(
            {
                "query": query,
                "expected_output": str(
                    expected_output
                )
            }
        )

    df = pd.DataFrame(data)

    df.to_csv(
        "evaluation/dataset.csv",
        index=False
    )

    print(
        f"Generated {n} evaluation samples."
    )


if __name__ == "__main__":
    generate_dataset()