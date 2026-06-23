from guardrails import Guard
from pydantic import BaseModel
from typing import List
import warnings

# Ignore common warnings for a cleaner output
warnings.filterwarnings(action="ignore", category=UserWarning, module="guardrails")

class MovieReview(BaseModel):
    title: str
    sentiment: str  # 'positive' or 'negative'
    key_points: List[str]

# Create a Guard from our Pydantic class
guard = Guard.for_pydantic(output_class=MovieReview)

# Simulate a valid LLM response
raw_output = """
{
  "title": "Inception",
  "sentiment": "positive",
  "key_points": ["Mind-bending plot", "Brilliant direction"]
}
"""

validated_output = guard.parse(raw_output)
if validated_output.validation_passed:
    print("Validation Passed!")
    print(validated_output.validated_output)
else:
    print("Validation Failed!")
