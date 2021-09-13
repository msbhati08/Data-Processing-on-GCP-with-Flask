import sys
import pandas as pd
from datetime import datetime
from google.cloud import storage

def main(event, context):
     """Triggered by a change to a Cloud Storage bucket.
     Args:
          event (dict): Event payload.
          context (google.cloud.functions.Context): Metadata for the event.
     """
    
     # Initialize variables at runtime
     target_bucket = 'webpage-static-content-bucket'

     file = event
     print(f"Processing file: {file['name']}.")

     try:
          if (file['name'].split('.')[1]=='csv'):
               # Call function to convert csv to html and load to bucket
               csv_to_html(file['bucket'], file['name'], target_bucket)

          elif (file['name'].split('.')[1]=='prn'):
         
               # Call function to convert prn to html and load to bucket
               prn_to_html(file['bucket'], file['name'], target_bucket)

     except Exception as e:
          print("Stopped Execution!! Error ", e.__class__, "occurred.")

def csv_to_html(bucket_name, file_name, target_bucket):
     
     try:
          # Read csv file into pandas dataframe
          input_df = pd.read_csv('gs://' + bucket_name + '/' + file_name)
    
          client = storage.Client()
          bucket = client.get_bucket(target_bucket)
    
          #  Storing the converted html file to cloud storage bucket
          bucket.blob('output_csv.html').upload_from_string(input_df.to_html(index=False), 'text/html')
     
     except Exception as e:
          print("Stopped Execution!! Error ", e.__class__, "occurred.")

          
def prn_to_html(bucket_name, file_name, target_bucket):
     
     try:
          # Read prn file into pandas dataframe
          input_df = pd.read_fwf('gs://' + bucket_name + '/' + file_name)
    
          client = storage.Client()
          bucket = client.get_bucket(target_bucket)

          # Storing the converted html file to cloud storage bucket
          bucket.blob('output_prn.html').upload_from_string(input_df.to_html(index=False), 'text/html')
     
     except Exception as e:
          print("Stopped Execution!! Error ", e.__class__, "occurred.")