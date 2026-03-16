import random

ideas = [
    "Krishna explains karma",
    "Why Arjuna felt fear before battle",
    "Krishna's message about time",
    "How Bhagavad Gita teaches discipline",
    "Why duty is greater than fear",
]


def generate_idea() -> str:
    return random.choice(ideas)
