# Find out more about building APIs with Plumber here:
# https://www.rplumber.io/

library(plumber)

#* @apiTitle Plumber API Cheshire Cat
#* @apiDescription Plumber example description.

#* Echo back the input (just to try that it works)
#* @param msg The message to echo
#* @get /echo
#* @serializer text
function(msg = "") {
  list(msg = paste0("The message is: '", msg, "'"))
}

#* run R code
#* @post /rtool
#* @param file:file
function(file, req){
  result = req$body$file$parsed %>%
    str2expression() %>%
    eval()
  
  return(result)
}
