import os 
import schema
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Prompt evaluation and ruleset is provided to GPT5.5. We pass on the parsed and opened resume and job desc.
def evaluate_job(resume_data, job_desc_data): 
  # convert JSON to readable text
  json.dumps(resume_data, indent=2)

  # temporary placeholder for API
  client = OpenAI()
  response = client.responses.parse(
    model="gpt-5",
    input=f"""
You are evaluating whether a candidate is a reasonable fit for a job.
Use only the supplied résumé. Do not invent qualifications or experience.

RESUME:
{resume_data}

JOB DESCRIPTION:
{job_desc_data}

Evaluation requirements:
- Identify genuine matches supported by evidence in the résumé.
- Identify important requirements that are missing or only partially supported.
- Assign a fit grade and score based on overall eligibility, relevance, and attainability.
- Choose one decision from the allowed values.
- Return a concise summary explaining the judgment.

Field meanings:
- fit_grade: overall letter grade for candidate-job alignment.
- fit_score: numeric fit score from 0 to 100.
- decision: recommended application action.
- strong_matches: résumé evidence that directly supports job requirements.
- major_gaps: important qualifications, experience, or constraints not demonstrated.
- summary: concise explanation of the overall evaluation. 
""",
  text_format=schema
  )

  # Parse each field instead of returning the whole thing
  return response.output_parsed 
