import json

# Separating JSON and text file handling 

def load_resume(filename):
  try:
    with open(filename, 'r') as file:
      resume_data = json.load(file)
    return resume_data
    
  except json.JSONDecodeError:
      print("Error: Failed to decode JSON from the file.")
      return None

def load_job_desc(filename):
  try:
    with open(filename) as file:
      job_desc_data = file.read()
    return job_desc_data
    
  except FileNotFoundError: 
    print("File does not exist")
    return None
  
  finally:
    file.close()

def main():
  # Carry the loaded files and print from main 
  resume_data = load_resume('example_resume1.json')
  job_desc = load_job_desc('example_job_description.txt')

  print(resume_data)
  print(job_desc)

  
if __name__ == "__main__":
  main()








