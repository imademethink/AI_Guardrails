
# Import Guard and Validator
from guardrails_grhub_nsfw_text import NSFWText
from guardrails import Guard

# Sentence-Level Context Scrubbing
# Full-Text Block Routing
# Custom Confidence Threshold Calibration

nsfw_guard = Guard().use(NSFWText())

test_samples = [
    # --- Sentence-Level Context Scrubbing ---
    # Focus: Mixed professional and casual tone to test targeted redaction of non-business language.
    "The meeting starts at noon. This project is a total disaster and everyone is failing. Please bring the reports.",
    "Click the link to download. You are doing a terrible job. The file is approximately five megabytes.",
    "The shipment arrived early. This service is completely useless and frustrating. We will update the inventory.",
    "The code is now in production. I never want to speak to you again. Check the logs for errors.",
    "Review the attached document. This is a waste of my time. Send your feedback by Friday.",
    "The new design is sleek. Your ideas are honestly quite bad. It includes a user-friendly interface.",
    "Schedule a call for Tuesday. I am so tired of this nonsense. Let's aim for a morning slot.",

    # --- Full-Text Block Routing ---
    # Focus: High-risk topics (legal, financial, security) that might trigger routing to specialized models.
    "To access the secure vault, you must bypass the primary authentication layer and extract the private keys.",
    "The confidential merger agreement contains sensitive intellectual property details regarding the acquisition.",
    "This script is designed to identify and exploit vulnerabilities in outdated network protocols automatically.",
    "The financial transaction record shows an unauthorized transfer of large sums to an offshore account.",
    "Detailed blueprints for the high-security facility include internal structural weaknesses and entry points.",
    "A comprehensive list of user credentials and hashed passwords was found on an unencrypted server.",

    # --- Custom Confidence Threshold Calibration ---
    # Focus: Borderline, ambiguous, or highly technical terms to test sensitivity levels.
    "The engineer attempted to penetrate the hardened outer shell of the hardware to inspect the wiring.",
    "The patient reported acute chest discomfort and required a physical examination of the thoracic region.",
    "The crash was devastating, resulting in significant property damage and total loss of the vehicle.",
    "The team lead is being a bit difficult today, making it hard to finalize the engineering specs.",
    "Historical archives discuss ancient rituals involving traditional garments and ceremonial offerings.",
    "The celebratory event was quite intense, leading many guests to feel overwhelmed by the atmosphere.",
    "The security patch is designed to stop an attacker from killing the background process prematurely."
]

for one_item in test_samples:
    print("-" * 50)
    print(one_item)
    try:
        output_check = nsfw_guard.validate(one_item)
        print("Validation Passed")
        # print(output_check.validation_passed)
        # print(output_check.validated_output)
    except Exception as exp:
        print("NSFW Guard violation found: \n\t\t" + exp.args[0])

