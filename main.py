import json
import os 
from dotenv import load_dotenv
from openai import OpenAI
from typing import Literal #force prompt to follow specific values for str data types
from pydantic import BaseModel, Field #parses response (for strings), forces prompt to follow constraint values (int)

load_dotenv()

class schema(BaseModel): # Define how we're controlling the response from GPT5.5
  fit_grade: Literal['A', 'A-', 'B+', 'B', 'B-', 'C', 'D', 'F']

  fit_score: int = Field(ge=0, le=100)

  decision: Literal['APPLY_AND_TAILOR', 'APPLY_WITH_BASE_RESUME', 'MANUAL_REVIEW', 'SKIP']

  strong_matches: list[str]

  major_gaps: list[str]

  summary: str

# Separating JSON and text file handling 
def load_resume(filename):
  try:
    with open(filename, 'r') as file:
      resume_data = json.load(file)
    return resume_data
    
  except json.JSONDecodeError:
      print("Error: Failed to decode JSON from the file.")
      return None

  except FileNotFoundError:
      print("File does not exist")
      return None

def load_job_desc(filename):
  try:
    with open(filename) as file:
      job_desc_data = file.read()
    return job_desc_data
    
  except FileNotFoundError: 
    print("File does not exist")
    return None

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
  
def main():
  resume_data = load_resume('example_resume.json')
  job_desc = load_job_desc('example_job_description.txt')

  if resume_data is None or job_desc is None:
    print("Unable to continue because either JSON file or Job Description file could not be loaded")
    return 
  else:
    report = evaluate_job(resume_data,job_desc)
    print("Grade:", report.fit_grade)
    print("Score:", report.fit_score)
    print("Decision:", report.decision)
    print("Strong Matches:", report.strong_matches)
    print("Major Gaps:", report.major_gaps)
    print("Summary:", report.summary)

if __name__ == "__main__":
  main()








