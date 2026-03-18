from core.llm import query_llm

class BaselineAgent:
    def respond(self, question):
        prompt = f"""
You are a guard in an Inca fantasy world.
Answer naturally.

User: {question}
NPC:
"""
        return query_llm(prompt)