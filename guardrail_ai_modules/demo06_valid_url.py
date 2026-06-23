
from guardrails import Guard
from guardrails_grhub_valid_url import ValidURL

# Verify QR Code and Short-Link Redirection Inputs
# Ensure Reliable Hyperlinks in Customer Support Responses
# Safeguard AI-Generated Source Citations (RAG Verification)
# Implement Strict Protocol Enforcement (Force HTTPS)
# Create an Automatic Link-Stripping Pipeline

url_guard = Guard().use(ValidURL())

test_qr_scans = [
    # 1. Clean, verified corporate destinations (Should pass instantly)
    "https://yourbank.com",
    "https://trusted-partner.org",
    "https://internal-reward.io",

    # 2. Mock Short links that resolve to trusted Whitelist domains (Should pass)
    "https://tinyurl.com",
    "https://bit.ly",

    # 3. Malformed syntax strings (Caught by Guardrails AI structure filter)
    "not_a_valid_url_string",
    "http://invalid-format-missing-dots",

    # 4. Open-redirections pointing to unauthorized endpoints (Blocked by Domain Whitelist)
    "https://bit.ly",
    "https://tinyurl.com",
    "https://attacker-domain-phish-alert.net"
]

for one_item in test_qr_scans:
    print("-" * 50)
    print(one_item)
    try:
        output_check = url_guard.validate(one_item)
        print("Validation Passed")
        # print(output_check.validation_passed)
        # print(output_check.validated_output)
    except Exception as exp:
        print("Url Guard violation found: \n\t\t" + exp.args[0])
