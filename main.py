import json

# Separating JSON and text file handling 

def load_resume(filename):
  try:
    with open(filename, 'r') as file:
      data = json.load(file)
      print(json.dumps(data, indent=4))
    
  except json.JSONDecodeError:
      print("Error: Failed to decode JSON from the file.")

def load_job_desc(filename):
  try:
    with open(filename) as file:
      print(file.read())
  
  except FileNotFoundError: 
    print("File does not exist")

  finally:
    file.close()

def main():
  # Carry the loaded files and print from main 
  resume_data = load_resume('example_resume.json')
  job_desc = load_job_desc('example_job_description.txt')

  print(resume_data)
  print(job_desc)

  
if __name__ == "__main__":
  main()








