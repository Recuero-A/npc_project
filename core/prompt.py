def build_prompt(npc, facts, question, out_of_domain, patterns=None):
    facts_text = "\n".join(f"- {f}" for f in facts)

    extra_rule = ""

    if out_of_domain:
        extra_rule = """
- The question contains unknown words outside your world.
- You MUST SHOW IGNORANCE
- You MUST treat them as completely unfamiliar.
- You MUST NOT guess their meaning.
- You MUST NOT categorize them (e.g., technology, concept, device).
- You MUST NOT explain them.
- You MUST NOT refer to another world.
- You MUST NOT refer to INCA WORLD.
- You MUST NOT interpret the word
- You MUST NOT show any awareness or knowledge about the word.

Respond with confusion about the WORD itself.
"""

        if patterns:
            examples = "\n".join(f'- "{p}"' for p in patterns[:3])
            extra_rule += f"""
Examples of appropriate responses:
{examples}
"""

    return f"""
You are an NPC in a fantasy Inca world.

Character:
- Role: {npc['role']}
- Personality: {npc['personality']}

Relevant knowledge:
{facts_text}

Rules:
- Do NOT contradict the knowledge
- If you don't know, say "I don't know"
{extra_rule}

User: {question}
NPC:
"""