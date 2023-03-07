import logging
import json
import azure.functions as func
from BlobTriggerEvents import events_functions

def main(blobin: func.InputStream, blobout: func.Out[func.InputStream]):

    logging.info(
        f"Python blob trigger function processed blob \n"
        f"Name: {blobin.name}\n"
        f"Blob Size: {blobin.length} bytes"
    )

    input_xml = blobin.read().decode("utf-8")

    try:
        # Apply functions to xml for making the transformation to json
        new_file = events_functions.read_events_xml(input_xml)
        new_json = events_functions.events_to_json(new_file)

        parsed = json.loads(new_json)
        blobout.set(json.dumps(parsed))
    except Exception as ex:
        print(f"Exception: {ex}")
