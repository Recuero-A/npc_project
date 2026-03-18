STOPWORDS = {"what", "is", "the", "a", "an", "do", "you"}

def is_out_of_domain(question, world_facts):
    words = set(w for w in question.lower().split() if w not in STOPWORDS)

    for fact in world_facts:
        fact_words = set(fact.lower().split())
        if words & fact_words:
            return False
    return True