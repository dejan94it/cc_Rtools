FROM rstudio/plumber

RUN R -e "install.packages(c('remotes', 'tidyverse', 'httr'))"

COPY / /

ENTRYPOINT []

CMD ["R","-e","pr <- plumber::plumb(file='myplumber.R'); args <- list(host = '0.0.0.0', port = as.numeric(Sys.getenv('PORT'))); if (packageVersion('plumber') >= '1.0.0') { pr$setDocs(TRUE) } else { args$swagger <- TRUE }; do.call(pr$run, args)"]