
# Import Guard and Validator
from guardrails_grhub_ban_list import BanList
from guardrails import Guard

# Protect Internal Project Codenames (Data Leak Prevention)
# Block "Fuzzy" Evasions and Typos
# Enforce Confident Brand Voice

ban_guard = Guard().use(BanList(banned_words=["Athena", "Project-X", "Falcon-9"]))

test_samples = [
    # 1. Exact leak of a secret name
    "The launch date for Project-X is set for July.",
    # 2. Fuzzy evasion (Typos/Leet speak) - 'Ath3na' is distance 2 from 'Athena'
    "We need to discuss the budget for Ath3na immediately.",
    # 3. Safe text with no secrets
    "The lunch menu for the cafeteria is available now.",
    # 4. Another fuzzy leak - 'Falc0n-9'
    "Falcon-9 propulsion tests are looking good."
]

for one_item in test_samples:
    print("-" * 50)
    print(one_item)
    try:
        output_check = ban_guard.validate(one_item)
        print("Validation Passed")
        # print(output_check.validation_passed)
        # print(output_check.validated_output)
    except Exception as exp:
        print("Ban Guard violation found: \n\t\t" + exp.args[0])
