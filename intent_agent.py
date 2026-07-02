from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from configs.settings import MODEL_NAME

llm = ChatGroq(
    model_name=MODEL_NAME,
    temperature=0)
prompt = ChatPromptTemplate.from_template("""
You are an Intent Classification Agent.

Classify the user query into ONE of the following:

- EMPLOYEE_SEARCH
- SALARY_ANALYSIS
- DEPARTMENT_ANALYSIS
- CITY_ANALYSIS
- EXPERIENCE_ANALYSIS
- JOINING_YEAR_ANALYSIS
- GENERAL_QUERY

User Query:
{query}

Return ONLY the label.
""")
def intent_agent(state):
    query = state["query"]
    response = llm.invoke(
        prompt.format_messages(query=query)
    )
    state["intent"] = response.content.strip()
    return state