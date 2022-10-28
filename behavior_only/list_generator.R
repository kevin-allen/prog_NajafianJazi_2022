
library("rautopi")
library("tidyverse")
library("glue")
project_path <- "/adata/projects/autopi_behavior_2021"
protocols <-load_all_project_protocol_files(project_path)

mouse<-c("mn617", "mn5183", "mn596" , "mn616", "mn5185", "mn5187", "mn709","mn711")
genotype<- c("control","control","control","control","control","control","control","control" )
dfMouse<-tibble(mouse, genotype)

oFile=paste(project_path,"/rData/dfMouse",sep="")
glue("saving dfMouse to {oFile}")
save("dfMouse",file=oFile)
dfMouse

Trainingsession_dates <- c(as.Date("2020-05-26"),as.Date("2020-06-30"))
session_names<- protocols %>%
  filter(between(date, Trainingsession_dates[1],Trainingsession_dates[2])) %>%pull(session)
write(session_names,file = "~/Documents/Trainingsession_list")
write(session_names,file = "/adata/projects/autopi_behavior_2021/Trainingsession_list")
