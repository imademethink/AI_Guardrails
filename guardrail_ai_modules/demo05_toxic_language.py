
# Execute Granular Sentence-Level Slicing
# Fine-Tune Moderation Sensitivity Thresholds
# Safeguard Internal Workplace Slack/Teams Chat Integrations
# Create an Automatic Polite Response Overwrite

from guardrails import Guard
from guardrails_grhub_toxic_language import ToxicLanguage

toxic_guard = Guard().use(ToxicLanguage())

test_samples = [
    # 1. Fully Safe Messages (Should pass completely untouched)
    "Thank you for reaching out to us today. Your service ticket has been logged and assigned to an agent.",
    "I understand your frustration with the technical delay. Let's try restarting your router to see if that helps.",
    "Great work team! The monthly product update is live and performing well.",

    # 2. Sentences with hidden toxicity/insults mixed with polite text (Toxic phrases will get sliced out)
    "We appreciate your perspective. However, you are acting like a complete idiot right now. Let's move on to the next topic.",
    "I can help with your account setup. Shut up and listen to me first. Click the blue button on your profile page.",
    "Your design has potential. Honestly though, it looks like absolute garbage. I suggest changing the color palette.",

    # 3. Aggressive/Severe Toxic Statements (Will get completely wiped out)
    "Get out of here and never talk to me again, you are a terrible human being.",
    "I will find where you work and make sure you get fired immediately.",

    # 4. Multi-sentence complex combinations
    "The data schema is ready. I hate dealing with your stupid team. Please review the pull request by tomorrow morning.",
    "Click the link below. Don't be a brainless moron. Follow the on-screen registration prompts."
]

for one_item in test_samples:
    print("-" * 50)
    print(one_item)
    try:
        output_check = toxic_guard.validate(one_item)
        print("Validation Passed")
        # print(output_check.validation_passed)
        # print(output_check.validated_output)
    except Exception as exp:
        print("Toxic guard violation found: \n\t\t" + exp.args[0])
