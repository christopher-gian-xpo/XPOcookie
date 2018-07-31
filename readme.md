## XPO Data Science Template Structure

```
Root
|-- cookiecutter.json        <- jinja2-like configuration file. 
|
|-- hooks                    <- this template file's README
|   `-- post_gen_project.py  <- pre or post template gen scripts
|
|-- readme.md                <- this template file's README
|
|
`-- {{cookiecutter.directory_name}} <- MAIN TEMPLATE
	|-- activate_env.sh      <- run, "source activate_env.sh" to activate env before "bash setup_env"
	|-- data                 	<- main data folder
	|   |-- interim          	<- interim data process
	|   |-- processed        	<- completely processed data
	|   `-- raw              	<- raw data files
	|-- documentation        <- documentation files, research, knowledge xfer ppts 
	|-- notebooks            <- jupyter notebooks
	|-- readme.md            <- this file
	|-- reports              <- Any reports generated for this project
	|-- requirements.txt     <- XPO Data Science Modules
	|-- scripts              <- 
	`-- setup_env.sh         <- run "bash setup_env.sh" to install requirements then install kernel into virtualenv
```

10 directories, 7 files
