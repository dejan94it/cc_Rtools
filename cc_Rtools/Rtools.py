from cat.mad_hatter.decorators import tool, hook
import requests
import logging

R_url = "http://r_env:5079/rtool"
path = "./cat/plugins/cc_Rtools/"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_Rtool(url, tool_name):

    try:
        with open(path+tool_name, "rt") as f:
            files = {'file':  (tool_name, f, 'text/plain')}
            response = requests.post(url, files=files)
        return(response.json())
    
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except requests.RequestException as e:
        logger.error(f"HTTP request failed: {e}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise   


@tool(return_direct=True)
def today(tool_input, cat):
    """Useful to say what day is today. Input is always None."""
    try:
        res = run_Rtool(R_url, "today.R")
        return res[0]
    except Exception as e:
        logger.error(f"Failed to run today tool: {e}")
        return {"error": "Failed to determine today's date."}
