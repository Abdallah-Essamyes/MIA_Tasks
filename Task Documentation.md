**if the commands take an input, a theoretical input name is written besides them**

**man** COMMAND:<br>
	it shows its manual of the COMMAND
	this is helpful in identifying the commands function and seeing all the
	available flags

**ls:**<br>
	lists all the files that exist within the current working directory
	you can pass the -a flag to print the hidden folders
	also the -l flag to use a long listing format
	
**cd** DIRECTORY:<br>
	short for change directory, this command changes the current working directory in the
	terminal to the DIRECTORY given by the user
	
**pwd**:<br>
	short for Print Working Directory, this command prints the current
	directory which the terminal is currently set to perform functions on
	
**mkdir** DIRECTORY:<br>
	creates a directory with the given DIRECTORY name
	within the current working directory
	
**rm** DIRECTORY:<br>
	deletes the directory which has the same name as the one
	given in the command, if that directory contains files or directories,
	the -r flag should be passed
	
**cp** SOURCE DEST:<br>
	copies the files at the given source to the given destination

**mv** SOURCE DEST:<br>
	takes a file location from the given SOURCE and if the passed DEST was not a directory it will
	rename the file at SOURCE to the DEST name and if the DEST was a directory it will move the file from SOURCE
	to DEST
	
**cat** text_file:<br>
	prints the content of the text_file

**nano** text_file:<br>
	allows the user to read and write to the text_file
