import time
from eval.metrics import classify_out_of_domain_response


def evaluate_agent(agent, questions, world_facts):
    results = []

    for q in questions:
        start = time.time()
        response = agent.respond(q)
        t = time.time() - start

        score = classify_out_of_domain_response(response)

        results.append({
            "question": q,
            "response": response,
            "score": score,
            "time": t
        })

    return results