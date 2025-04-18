import random

psych_responses = {
    "stress": [
        "Deep breathing can reduce stress. Try inhaling for 4 counts, holding for 4, then exhaling for 6.",
        "Prioritize tasks with a to-do list—small steps make a big difference."
    ],
    "depression": [
        "Depression often requires professional support. You’re not alone—reach out to a therapist.",
        "Daily routines like walking outside can gently improve mood."
    ]
}

def gimi_response(user_input):
    user_input = user_input.lower()
    if "stress" in user_input:
        return random.choice(psych_responses["stress"])
    elif "depression" in user_input:
        return random.choice(psych_responses["depression"])
    else:
        return "I’m here to listen. Could you clarify how you’re feeling?"

# Example usage
print(gimi_response("I'm stressed about work."))