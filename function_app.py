import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", 
                  path="uploads/{name}",  # <--- THIS is your trigger path
                  connection="AzureWebJobsStorage") 
def BlobTriggerWorker(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")