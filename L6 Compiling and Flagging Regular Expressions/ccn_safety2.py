import re

text = """Have you ever noticed, in television and movies, that phone 
numbers and credit cards are obviously fake numbers like 555-123-4567 
or 5555-5555-5555-5555? It is because a number that appears to be real,
such as 1234-5678-1234-5678, triggers the attention of privacy and 
security experts."""

def converter(text):
    compiler = re.compile("[1-9]{4}-[1-9]{4}-[1-9]{4}-[1-9]{4}", re.VERBOSE)
    substitute = compiler.sub("CCN REMOVED FOR YOUR SAFETY", text, re.VERBOSE)
    return substitute

if __name__ == "__main__":
    print (converter(text))
