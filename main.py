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
    report_data = report.model_dump(mode="json")

    if report is None:
      return
      
    else:
      with open('job_report.json', 'w', encoding='utf-8') as f:
        json.dump(report_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
  main()
