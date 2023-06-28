# cc_Rtools
This plugin allow Cheshire Cat to use tools written in R (and to run R code in general)

## Installation

- Just download the cc_Rtools folder into cheshire-cat/core/cat/plugins.
  
## Add R container to cheshire-cat

Simply add to the cat's default docker-compose.yml the following code:

```yaml
  r-env:
     build: https://github.com/dejan94it/cc_Rtools.git#main:plumber_container
     container_name: r_env
     expose:
      - "5079:5000"
     restart: unless-stopped
```
and obviously run ```docker compose up```

## How to use it

- Write a ```yourscript.R``` file and put it into cc_Rtools folder.
- Add a @tool in ```Rtools.py``` using ```run_Rtool(R_url, "yourscript.R")``` in it.

You can see the example of ```today.R```, already present in the folder.
