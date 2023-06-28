from cat.mad_hatter.decorators import tool, hook
import requests

R_url = "http://r_env:5079/rtool"

path = "./cat/plugins/cc_Rtools/"

def run_Rtool(url, tool_name):

    with open(path+tool_name, "rt") as f:
        files = {'file':  (tool_name, f, 'text/plain')}
        response = requests.post(url, files=files)

    return(response.json())


@tool(return_direct=True)
def today(tool_input, cat):
    """Useful to say what day is today. Input is always None."""
    res = run_Rtool(R_url, "today.R")
    return res[0]


