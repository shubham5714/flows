from prefect import flow, task 
from prefect.task_runners import ConcurrentTaskRunner 
import time 
import random # A sample task that simulates processing 

@task 
def process_item(item: int) -> str: 
  sleep_time = random.uniform(0.5, 2.0) 
  time.sleep(sleep_time) 
  result = f"Processed item {item} in {sleep_time:.2f}s" 
  print(result) 
  return result 

# The main flow using concurrent task runner
@flow(task_runner=ConcurrentTaskRunner()) 
def parallel_processing_flow(items: list[int]): 
   results = process_item.map(items) 
   return results
