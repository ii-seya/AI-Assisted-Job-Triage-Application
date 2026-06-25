"""
Workflow:

open and parse json file

open and read .txt file (job desc)

check for:
1. missing .txt file
2. malformed JSON file

print results
"""
import json

# JSON file handling
try:
  with open('data.json', 'r') as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))
  
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from the file.")

# Job Desc. file handling
try:
  with open("jobdesc.txt") as f:
    print(f.read())

except FileNotFoundError: 
  print("File does not exist")

finally:
  f.close()
  
  

