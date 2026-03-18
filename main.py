import json

# import all models
from models.baseline.agent import BaselineAgent
from models.rule.agent import RuleAgent
from models.pattern.agent import PatternAgent
from models.llm_classifier.agent import LLMClassifierAgent


# load data
world_facts = json.load(open("data/world_facts.json"))
npcs = json.load(open("data/npcs.json"))

npc = npcs["guard"]


# 🔥 SELECT MODEL
print("Choose model:")
print("1 - Baseline")
print("2 - Rule")
print("3 - Pattern")
print("4 - LLM Classifier")

choice = input("Enter number: ")


# 🔁 CREATE AGENT
if choice == "1":
    agent = BaselineAgent()
    model_name = "Baseline"

elif choice == "2":
    agent = RuleAgent(npc, world_facts)
    model_name = "Rule"

elif choice == "3":
    agent = PatternAgent(npc, world_facts)
    model_name = "Pattern"

elif choice == "4":
    agent = LLMClassifierAgent(npc, world_facts)
    model_name = "LLM Classifier"

else:
    print("Invalid choice, defaulting to Rule")
    agent = RuleAgent(npc, world_facts)
    model_name = "Rule"


print(f"\n--- Talking to NPC ({model_name}) ---")
print("Type 'exit' to quit\n")


# 💬 CHAT LOOP
while True:
    q = input("You: ")

    if q.lower() == "exit":
        break

    response = agent.respond(q)

    print("NPC:", response)