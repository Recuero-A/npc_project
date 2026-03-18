from core.llm import query_llm

def classify_domain(question):
    prompt = f"""
Determine whether the following question is consistent or related 
to a possible conversation in a fantasy ancient Inca world.
Some of the Inca World facts are: magic condor lives in mountain, king is dead, capital Cuzco,
forest cursed, Inca empire. 
There are NO MODERN TECHNOLOGIES in Inca World

Answer ONLY:
IN_DOMAIN or OUT_OF_DOMAIN

Question: {question}
Answer:
"""
    res = query_llm(prompt).upper()
    return "IN_DOMAIN" in res