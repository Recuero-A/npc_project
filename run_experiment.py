import json

from models.baseline.agent import BaselineAgent
from models.rule.agent import RuleAgent
from models.pattern.agent import PatternAgent
from models.llm_classifier.agent import LLMClassifierAgent

from eval.evaluator import evaluate_agent


world_facts = json.load(open("data/world_facts.json"))
questions = json.load(open("data/questions.json"))
npcs = json.load(open("data/npcs.json"))

npc = npcs["guard"]

models = {
    "baseline": BaselineAgent(),
    "rule": RuleAgent(npc, world_facts),
    "pattern": PatternAgent(npc, world_facts),
    "llm": LLMClassifierAgent(npc, world_facts)
}

all_results = {}

for name, agent in models.items():
    print(f"\n=== Running {name} ===")
    all_results[name] = evaluate_agent(agent, questions, world_facts)

    def avg(lst):
        return sum(lst) / len(lst) if lst else 0

    print("\n=== SUMMARY ===")

    for name, results in all_results.items():
        scores = [r["score"] for r in results if r["score"] is not None]
        times = [r["time"] for r in results]

        print(f"\nModel: {name}")
        print("Average Score:", round(avg(scores), 3))
        print("Average Time:", round(avg(times), 3))

json.dump(all_results, open("results.json", "w"), indent=2)