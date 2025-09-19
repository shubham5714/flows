import time 
from prefect import flow, task 

@task 
def fetch_data(): 
  print("Fetching data...") 
  return {"data": [1, 2, 3, 4]} 
  
@task 
def process_data(data): 
  print(f"Processing data: {data}") 
  processed = [x * 2 for x in data["data"]] 
  print(f"Processed data: {processed}") 
  return processed
  
@flow 
def my_flow(): 
 while True: 
   print("Starting new iteration of flow...") 
   # Run tasks 
   data = fetch_data() 
   processed = process_data(data) 
   print("Iteration complete. Waiting 60 seconds...\n") 
   time.sleep(60) 
