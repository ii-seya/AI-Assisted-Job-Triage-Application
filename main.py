import schema
import file_loaders
import evaluator

def main():
  resume_data = file_loaders.load_resume('example_resume.json')
  job_desc = file_loaders.load_job_desc('example_job_description.txt')

  if resume_data is None or job_desc is None:
    print("Unable to continue because either JSON file or Job Description file could not be loaded")
    return 
  else:
    report = evaluator.evaluate_job(resume_data,job_desc)
    print("Grade:", report.fit_grade)
    print("Score:", report.fit_score)
    print("Decision:", report.decision)
    print("Strong Matches:", report.strong_matches)
    print("Major Gaps:", report.major_gaps)
    print("Summary:", report.summary)

if __name__ == "__main__":
  main()
