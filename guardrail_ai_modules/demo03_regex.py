
# most powerful tools for enforcing
#   strict formatting rules,
#   business logic, and
#   security constraints

# Enforce Standardized Currency Formats

from pydantic import BaseModel, Field
from guardrails import Guard
from guardrails_grhub_regex_match import RegexMatch

# US Pattern: Must start with $, use commas for thousands, and a dot for 2 decimal places.
US_CURRENCY_REGEX = r"^\$\d{1,3}(,\d{3})*(\.\d{2})?$"
# EU Pattern: Must use dots for thousands, a comma for 2 decimal places, followed by € or EUR.
EU_CURRENCY_REGEX = r"^\d{1,3}(\.\d{3})*(,\d{2})\s?(€|EUR)$"

class FinancialReportSchema(BaseModel):
    region: str
    # Validation for US transactions
    usd_amount: str = Field(
        validators=[
            RegexMatch(
                regex=US_CURRENCY_REGEX,
                match_type="fullmatch",
                on_fail="exception"
            )
        ]
    )

    # Validation for EU transactions
    eur_amount: str = Field(
        validators=[
            RegexMatch(
                regex=EU_CURRENCY_REGEX,
                match_type="fullmatch",
                on_fail="exception"
            )
        ]
    )

currency_guard = Guard.for_pydantic(output_class=FinancialReportSchema)

def process_ledger_entry(region: str, usd: str, eur: str) -> str:
    """
    Validates that incoming financial extraction results match strict geographic layout styles.
    """
    raw_json_input = f"""{{
        "region": "{region}",
        "usd_amount": "{usd}",
        "eur_amount": "{eur}"
    }}"""

    try:
        currency_guard.parse(llm_output=raw_json_input)
        return f"[SUCCESS]: Entry recorded for region '{region}' (USD: {usd} | EUR: {eur})"
    except Exception:
        return "[ERROR]: General execution error parsing financial objects."

test_samples = [
    # 1. Perfectly formatted inputs
    ("Global-A", "$1,250.50", "1.250,50 €"),
    ("Global-B", "$10,000,000.00", "10.000.000,00 EUR"),
    ("Global-C", "$0.99", "0,99 €"),
    ("Global-D", "$500", "500,00 EUR"),

    # 2. Failing Cases: Invalid US Formats (Using EU style punctuation for USD)
    ("US-Fail-1", "1.250,50 $", "1.250,50 €"),
    ("US-Fail-2", "$12,34,56.00", "1.234,56 €"),  # Incorrect comma grouping

    # 3. Failing Cases: Invalid EU Formats (Using US style punctuation for EUR)
    ("EU-Fail-1", "$1,250.50", "1,250.50 €"),
    ("EU-Fail-2", "$100.00", "1.250,50"),  # Missing currency symbol/tag

    # 4. Failing Cases: Casual text layout errors
    ("Text-Fail-1", "about $50 dollars", "120,00 €"),
    ("Text-Fail-2", "$100.00", "around fifty euros")
]

print("--- Starting Currency Format Validation Checks ---\n")
for idx, (region, usd, eur) in enumerate(test_samples, 1):
    print(f"Test Case #{idx}")
    print(f"Checking -> USD Input: '{usd}' | EUR Input: '{eur}'")
    result = process_ledger_entry(region, usd, eur)
    print(f"Action:     {result}")
    print("-" * 65)



# Block Phishing and Spam Links
# Validate Identifiers (IDs, UUIDs, and Serial Numbers)
# Sanitize and Extract Valid Postal/ZIP Codes
# Security - Strip out Inbound Code Injections e.g. XSS
# Enforce Precise Timestamp and Date Standards
# Validate Phone Number Syntax Across Regions
