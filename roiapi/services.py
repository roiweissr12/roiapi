import random


def fake_llm_response(prompt: str) -> str:
    if prompt == "Hello, who are you?":
        return "LLM says: I am me"
    random_number = random.randint(1, 100)
    return (
        f"LLM says: You said '{prompt}'. I will give you a random number,"
        f" Because that's what I was told to do: {random_number}"
    )
