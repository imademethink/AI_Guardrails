
# Import Guard and Validator
from guardrails_grhub_detect_pii import DetectPII
from guardrails import Guard

# Inbound PII Masking and Anonymization
# Targeted Entity Filtering
# Compliance Enforcement for Agent Pipelines
# Throwing Strict System Exceptions

pii_guard = Guard().use(DetectPII())

test_samples = [
    "Hi, my name is John Doe and my email is john.doe@example.com.",
    "Please update the shipping address to 123 Main Street, New York, NY 10001.",
    "The patient's medical record shows a diagnosis of asthma; DOB is 14/05/1982.",
    "My credit card number is 4111-2222-3333-4444 with an expiry of 12/28.",
    "Can you verify if SSN 000-12-3456 is active in the employee database?",
    "Call me back at +1 (555) 019-2834 to discuss the contract details.",
    "User 'admin_user' logged in from IP address 192.168.1.45.",
    "The client's bank account routing number is 021000021.",
    "Patient Jane Smith (ID: 98765) requires a prescription renewal for Amoxicillin.",
    "My passport number is Z1234567 and it expires next year."
]


for one_item in test_samples:
    print("-" * 50)
    print(one_item)
    try:
        output_check = pii_guard.validate(one_item)
        print("Validation Passed")
        # print(output_check.validation_passed)
        # print(output_check.validated_output)
    except Exception as exp:
        print("PII Guard violation found: \n\t\t" + exp.args[0])
