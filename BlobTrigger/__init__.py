import logging
import json

import azure.functions as func


def main(inputblob: str):
    
    logging.info(f"Received new blob with {len(inputblob)} bytes in size")
    content = json.loads(inputblob)
    
    # Perform some processing on the JSON
    
    logging.info(f"JSON processed, content: {content}")
    