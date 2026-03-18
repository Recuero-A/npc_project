from core.retriever import retrieve_facts
from core.prompt import build_prompt
from core.llm import query_llm
from models.llm_classifier.classifier import classify_domain


class LLMClassifierAgent:
    def __init__(self, npc, world_facts):
        self.npc = npc
        self.world_facts = world_facts

    def respond(self, question):
        in_domain = classify_domain(question)

        facts = retrieve_facts(question, self.world_facts)

        prompt = build_prompt(
            self.npc,
            facts,
            question,
            out_of_domain=not in_domain
        )

        return query_llm(prompt)