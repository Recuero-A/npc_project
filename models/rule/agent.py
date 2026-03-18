from core.retriever import retrieve_facts
from core.prompt import build_prompt
from core.llm import query_llm
from models.rule.domain import is_out_of_domain


class RuleAgent:
    def __init__(self, npc, world_facts):
        self.npc = npc
        self.world_facts = world_facts

    def respond(self, question):
        out = is_out_of_domain(question, self.world_facts)

        facts = retrieve_facts(question, self.world_facts)

        prompt = build_prompt(self.npc, facts, question, out)

        return query_llm(prompt)