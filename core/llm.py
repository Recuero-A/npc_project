import subprocess

def query_llm(prompt):
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    output = result.stdout.decode()
    if "Player:" in output:
        output = output.split("Player:")[0]

    return output.strip()