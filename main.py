import json
import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

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

# Resume and Job Desc are now evaluated by GPT 5.5
def evaluate_job(resume_data, job_desc_data): 
  # convert JSON to readable text
  json.dumps(resume_data, indent=2)

  # temporary placeholder for API
  client = OpenAI()
  response = client.responses.create(
    model="gpt-5",
    input=f"""You are evaluating whether a candidate is a reasonable fit for a job.

    Use only the supplied résumé.
    Do not invent qualifications.
    
    RESUME:
    {resume_data}
    
    JOB DESCRIPTION:
    {job_desc_data}
    
    Return:
    - Overall fit
    - Strong matches
    - Major gaps
    - Recommendation
    """)

  return response.output_text

def main():
  resume_data = load_resume('example_resume.json')
  job_desc = load_job_desc('example_job_description.txt')

  if resume_data is None or job_desc is None:
    print("Unable to continue because either JSON file or Job Description file could not be loaded")
    return 
  else:
    report = evaluate_job(resume_data,job_desc)
    print(report)

if __name__ == "__main__":
  main()








