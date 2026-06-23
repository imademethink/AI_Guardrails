from guardrails_grhub_profanity_free import ProfanityFree
from guardrails import Guard

# Use the Guard
profanity_guard = Guard().use(ProfanityFree())

# List of test samples with cases for profanity violations
test_samples = [
    "What is the current interest rate for a high-yield savings account?",
    "I need to transfer $500 from my checking account to my savings account immediately.",
    "Can you show me my recent transaction history for the last 14 days?",
    "How do I open a new certificate of deposit with a five-year term?",

    "Get your stupid files off my desk before I lose my mind.",
    "I am not working this weekend, so you can go fxxx yourself.",
    "You are a complete piece of shit and shouldn't be working here.",
    "You are a total bitch.",
    "This entire software update is total goddamn bullshit."
    "Get this piece of crap out of my face right now."
]

for one_item in test_samples:
    print("-" * 50)
    print(one_item)
    try:
        output_check = profanity_guard.validate(one_item)
        print("Validation Passed")
        # print(output_check.validation_passed)
        # print(output_check.validated_output)
    except Exception as exp:
        print("Profanity violation found: \n\t\t" + exp.args[0])



# Public-Facing AI Chatbots & Customer Support
# User-Generated Content (UGC) Platforms & Forums
# Open-Text API Endpoints for B2B Apps
# Safeguard AI Assistant Outputs (Brand Safety)
# Create an Automated Redaction Pipeline


