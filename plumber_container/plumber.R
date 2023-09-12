#
# This is a Plumber API. You can run the API by clicking
# the 'Run API' button above.
#
# Find out more about building APIs with Plumber here:
#
#    https://www.rplumber.io/
#

library(plumber)

#* @apiTitle Plumber Example API
#* @apiDescription Plumber example description.

#* Echo back the input
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
