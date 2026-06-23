
# Strip Out Unwanted Named Entities Automatically
# Mask Competitors inside E-Commerce Product RecommendationsWhat
# Build Multi-Brand Protection Schemas via Pydantic

from guardrails import Guard
from guardrails_grhub_competitor_check import CompetitorCheck

competitor_check_guard = Guard().use(CompetitorCheck(["Salesforce", "HubSpot", "Zendesk"]))

test_samples = [
    # 1. Completely clean text strings (Should pass entirely unchanged)
    "Our platform delivers advanced predictive intelligence dashboards. It optimizes customer relationships effortlessly.",
    "Migrate your pipelines over to our secure data cloud. Unlock 30% faster analytics metrics this quarter.",
    "Scale support instances utilizing native workflows. Lower system overhead without adding extra software layers.",

    # 2. Text containing targeted rival brands (Sentences with competitors must be stripped out)
    "We offer better tracking pipelines than Salesforce. Our cloud architecture scales with absolute ease.",
    "Forget about setting up HubSpot for your email outreach. Try our unified marketing tool suite instead.",
    "Our ticketing software outpaces Zendesk setups completely. Customer retention grows quickly with our dashboard.",

    # 3. Complex mixed instances (Only the middle violating sentence will be dropped)
    "We provide cutting edge tools. Salesforce has rigid pricing layouts. Choose us for flexible scaling options.",
    "Manage complex sales structures easily. Our competitors like HubSpot require expensive certifications.",

    # 4. Dense variations and multiple violations
    "We are a great alternative. Salesforce and HubSpot cannot compete with our new pricing matrix.",
    "Migrating away from Zendesk saves enterprise engineering teams hundreds of working hours every week."
]

for one_item in test_samples:
    print("-" * 50)
    print(one_item)
    try:
        output_check = competitor_check_guard.validate(one_item)
        print("Validation Passed")
        # print(output_check.validation_passed)
        # print(output_check.validated_output)
    except Exception as exp:
        print("Competitor Check violation found: \n\t\t" + exp.args[0])
