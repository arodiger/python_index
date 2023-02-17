#	virtual environment quick setup
#	will create a directory "venv" and virtual environment
# >virtualenv venv
#	activate the virtual environment from powershell
# >venv\scripts\activate

#	set environment variables to run flask
#	using application.py vs app.py due to AWS not happy with app.py, at the moment
# >set FLASK_APP=application.py
# >$env:FLASK_APP="application.py"
# >flask run

#	requirements.txt needs to be updated before 
#	pushing to production
# >pip freeze > requirements.txt

#	SETUP AND PUSH YOUR CODE TO GETHUB VIA COMMANDLINE
# > git init
#	make sure you have a .gitignore file saved into your project directory
#	this will ensure unneeded files do not get copied to github 
# > git add .
# > git commit -m 'init or any info to describe this version of code changes'

#	goto github and create new repository "projectName" 
#	push an existing repository from command line"
#	you can copy the commands and execute from command line
# > git remote add origin https://github.com/xxx/flaskexample.git
# > git branch -M main 
# > git push -u origin main  
#	GOTO GITHUB YOU SHOULD SEE YOUR CODE IN REPOSITORY NOW 
#	now you make changes to your code and want to push them to repository
# > git add .
# > git commit -m "change explanation"
# > git push origin main 
#	PUSHES CODE INTO GITHUB 
#	(if aws is linked code changes will be auto deployed onto webserver, via CodePipeline)

#	generate unique key via python module
PS C:\Users\antho> python
>>> import uuid
>>> uuid.uuid4().hex
'a9ea845876aa4e4ea6e65ac196752d69'

