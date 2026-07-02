from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from configs.settings import MODEL_NAME


llm = ChatGroq(
    model_name=MODEL_NAME,
    temperature=0
)

sql_prompt = ChatPromptTemplate.from_template("""
You are a Senior SQL Engineer.

Database Table:

employees

Columns:

employee_id INTEGER
name TEXT
department TEXT
salary INTEGER
experience INTEGER
city TEXT
joining_year INTEGER

Rules:

1. Generate SQLite compatible SQL.
2. Return ONLY SQL.
3. Do NOT add explanations.
4. Do NOT wrap in markdown.
5. Use table name employees.

User Query:
{query}
""")


def sql_agent(state):

    query = state["query"]

    response = llm.invoke(
        sql_prompt.format_messages(query=query)
    )

    sql_query = response.content.strip()

    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")
    sql_query = sql_query.strip()

    state["sql"] = sql_query

    return state