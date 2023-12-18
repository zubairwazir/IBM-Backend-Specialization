
# return your user name

1.  `whoami` 


# return your user and group id

1.  `id` 

# return operating system name, username, and other info

1.  `uname -a` 

# display reference manual for a command

1.  `man top` 

# get help on a command

1.  `curl --help` 

# return the current date and time

1.  `date` 

### Monitoring performance and status

----------

# list selection of or all running processes and their PIDs

1.  `ps` 
2.  `ps -e` 

# display resource usage

1.  `top` 

# list mounted file systems and usage

1.  `df`

### Working with files

----------

# copy a file

1.  `cp file.txt new_path/new_name.txt`

# change file name or path

1.  `mv this_file.txt that_path/that_file.txt`

# remove a file verbosely

1.  `rm this_old_file.txt -v`

# create an empty file, or update existing file’s timestamp

1.  `touch a_new_file.txt` 

# change/modify file permissions to ‘execute’ for all users

1.  `chmod +x  my_script.sh`

# get count of lines, words, or characters in file

1.  `wc -l table_of_data.csv` 
2.  `wc -w my_essay.txt` 
3.  `wc -m some_document.txt` 

# return lines matching a pattern from files matching a filename pattern - case insensitive and whole words only

1.  `grep -iw hello  \*.txt` 

# return file names with lines matching the pattern ‘hello’ from files matching a filename pattern

1.  `grep -l hello  \*.txt`

### Navigating and working with directories

----------

# list files and directories by date, newest last

1.  `ls -lrt` 

# find files in directory tree with suffix ‘sh’

1.  `find -name '\*.sh'`

# return present working directory

1.  `pwd`

# make a new directory

1.  `mkdir new_folder` 

# change the current directory: up one level, home, or some other path

1.  `cd ../` 
2.  `cd ~ or cd` 
3.  `cd another_directory`

5.  `` `\# remove directory, verbosely` ``
6.  `rmdir temp_directory -v`

### Printing file and string contents

----------

# print file contents

1.  `cat my_shell_script.sh` 

# print file contents page-by-page

1.  `more ReadMe.txt` 

# print first N lines of file

1.  `head -10 data_table.csv`

# print last N lines of file

1.  `tail -10 data_table.csv`
2. 
# print string or variable value

1.  `echo "I am not a robot"` 
2.  `echo "I am $USERNAME"` 

### Compression and archiving

----------

# archive a set of files

1.  `tar -cvf my_archive.tar.gz file1 file2 file3`

# compress a set of files

1.  `zip my_zipped_files.zip file1 file2` 
2.  `zip my_zipped_folders.zip directory1 directory2`

# extract files from a compressed zip archive

1.  `unzip my_zipped_file.zip` 
2.  `unzip my_zipped_file.zip -d extract_to_this_direcory`

### Performing network operations

----------

# print hostname

1.  `hostname` 

# send packets to URL and print response

1.  `ping  www.google.com`

# display or configure system network interfaces

1.  `ifconfig` 
2.  `ip` 

# display contents of file at a URL

1.  `curl <url>`

# download file from a URL

1.  `wget <url>`

### Bash shebang

----------

`#!/bin/bash`

### Pipes and Filters

----------

# chain filter commands using the pipe operator

1.  `ls | sort -r` 

# pipe the output of manual page for ls to head to display the first 20 lines

1.  `man ls | head -20` 

### Shell and Environment Variables

----------

# list all shell variables

1.  `set` 

# define a shell variable called my_planet and assign value Earth to it

1.  `my_planet=Earth` 

# display shell variable

1.  `echo $my_planet` 

# list all environment variables

1.  `env`

# environment vars: define/extend variable scope to child processes

1.  `export my_planet` 
2.  `export my_galaxy='Milky Way'`

### Metacharacters
----------
# comments  
`# The shell will not respond to this message`

# command separator

1.  `echo 'here are some files and folders'; ls`

# file name expansion wildcard

1.  `ls *.json` 

# single character wildcard

1.  `ls file_2021-06-??.json`

### Quoting
----------
# single quotes - interpret literally

1.  `echo 'My home directory can be accessed by entering: echo $HOME'`

# double quotes - interpret literally, but evaluate metacharacters

1.  `echo "My home directory is $HOME"`
2. 
# backslash - escape metacharacter interpretation

1.  `echo "This dollar sign should render: \$"`

### I/O Redirection

----------

# redirect output to file

1.  `echo 'Write this text to file x'  > x`

# append output to file

1.  `echo 'Add this line to file x'  >> x`

# redirect standard error to file

1.  `bad_command_1 2> error.log`

# append standard error to file

1.  `bad_command_2 2>> error.log` 

# redirect file contents to standard input

1.  `$ tr “[a-z]”  “[A-Z]”  < a_text_file.txt` 

# the input redirection above is equivalent to

1.  `$cat a_text_file.txt | tr “[a-z]”  “[A-Z]”`

### Command Substitution

----------
# capture output of a command and echo its value

1.  `THE_PRESENT=$(date)` 
2.  `echo "There is no time like $THE_PRESENT"`

### Command line arguments

----------

1.  `./My_Bash_Script.sh arg1 arg2 arg3`

### Batch vs. concurrent modes

----------
# run commands sequentially

1.  `start=$(date);  ./MyBigScript.sh ; end=$(date)`

# run commands in parallel

1.  `./ETL_chunk_one_on_these_nodes.sh &  ./ETL_chunk_two_on_those_nodes.sh` 

## Scheduling jobs with Cron

----------

# open crontab editor

1.  `crontab -e` 

# job scheduling syntax

1.  `m  h  dom  mon  dow   command` 

_minute, hour, day of month, month, day of week_  
`*`  means any

# append the date/time to file every Sunday at 6:15 pm

1.  `15  18  *  *  0 date >> sundays.txt`

# run a shell script on the first minute of the first day of each month

1.  `1  0  1  *  *  ./My_Shell_Script.sh`

# back up your home directory every Monday at 3 am

1.  `0  3  *  *  1 tar -cvf my_backup_path\my_archive.tar.gz $HOME\`

# deploy your cron job  
_Close the crontab editor and save the file_

# list all cron jobs

1.  `crontab -l`
