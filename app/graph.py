from langgraph.graph import StateGraph, END

from .state import AgentState
from .nodes import identify_intent, invoke_tool, synthesize_answer

builder = StateGraph(AgentState)

builder.add_node("intent", identify_intent)
builder.add_node("tool_call", invoke_tool)
builder.add_node("generate_answer", synthesize_answer)

builder.set_entry_point("intent")

builder.add_edge("intent", "tool_call")
builder.add_edge("tool_call", "generate_answer")
builder.add_edge("generate_answer", END)

graph = builder.compile()