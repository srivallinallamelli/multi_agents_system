from langgraph.graph import StateGraph

from agents.intent_agent import intent_agent
from agents.sql_agent import sql_agent
from agents.executor_agent import executor_agent
from agents.response_agent import response_agent


def build_graph():

    workflow = StateGraph(dict)

    # Nodes
    workflow.add_node(
        "intent_agent",
        intent_agent
    )

    workflow.add_node(
        "sql_agent",
        sql_agent
    )

    workflow.add_node(
        "executor_agent",
        executor_agent
    )

    workflow.add_node(
        "response_agent",
        response_agent
    )

    # Flow

    workflow.set_entry_point(
        "intent_agent"
    )

    workflow.add_edge(
        "intent_agent",
        "sql_agent"
    )

    workflow.add_edge(
        "sql_agent",
        "executor_agent"
    )

    workflow.add_edge(
        "executor_agent",
        "response_agent"
    )

    workflow.set_finish_point(
        "response_agent"
    )

    return workflow.compile()