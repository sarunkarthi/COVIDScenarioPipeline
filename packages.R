list.of.packages <- c("Rcpp", "tidyr", "dplyr", "readr", "ggplot2", "gridExtra", "sf", "viridis", "ggfortify", "flextable", "cowplot")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)
