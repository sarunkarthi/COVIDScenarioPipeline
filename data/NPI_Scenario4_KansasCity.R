## create matrix for counties starting social distancing based on Bootsma Kansas City R0 reductions

library(dplyr)

county.status <- read.csv(paste0(foldername,'geodata.csv'))
dates <- seq.Date(as.Date(ti_str), as.Date(tf_str), 1)

NPI <- as.data.frame(matrix(0, dim(county.status)[1],length(dates)))
colnames(NPI) <- as.Date(dates)
rownames(NPI) <- county.status$geoid

## Introducing NPI: randomly assign a pc value to each county based on Bootsma paper values
NPI[ , colnames(NPI) >= as.Date("2020/03/19") & colnames(NPI) <= as.Date("2020/05/14") ] <- 1
county.status$pc <- replicate(dim(county.status)[1], runif(dim(county.status)[1], 0.35, 0.56))
NPI <- NPI * county.status$pc
