from sqlalchemy import text
from database.connection import engine

def executor_agent(state):

    sql_query = state.get("sql")

    try:
        with engine.begin() as conn:
            result = conn.execute(
                text(sql_query)
            )

            rows = [
                dict(row._mapping)
                for row in result
            ]

            state["output"] = rows

    except Exception as e:

        state["output"] = []
        state["error"] = str(e)

    return state