def retrieve_facts(question, world_facts, k=2):
    # naive keyword matching (start simple)
    relevant = []
    for fact in world_facts:
        for word in question.lower().split():
            if word in fact.lower():
                relevant.append(fact)
                break
    return relevant[:k]