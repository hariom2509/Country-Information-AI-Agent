from typing import TypedDict, Optional, List

class AgentState(TypedDict):
    question: str
    country: Optional[str]
    fields: Optional[List[str]]
    country_data: Optional[dict]
    answer: Optional[str]