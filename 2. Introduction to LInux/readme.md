a/b - The File/Dir named b is inside the Dir named a

## Special Paths

- ~ Home Dir
- / Root Dir
- . Current Dir
- .. Parent of Current Dir

__cd ../../home/user/Docs__

## Nano CMD Editor

hold ctrl button and press the mentioned button for command

## Vim CMD Editor

Two Modes <br>
1. Insert Mode (type i for insert mode)
2. Command Mode (Type esc to escape for insert mode to command mode)

__Command Mode__

- Enter ***:sav exmaple.txt*** to create a file and write the buffer to the file
- Enter ***:w*** to write the buffer to the file without exiting
- Enter ***:q*** to quit vim seesion
- Enter ***:q!*** to quit without saving


### If a package is only available in one fomat you can use alien to convert it.

- **RPM to deb**

`alien <package-name>.rpm`

- **deb to RPM**

`alien -r <package-name>.deb`

### Installing a deb package wth apt

`sudo apt install <package-name>`

### Installing an RPM package wth yum

`sudo yum install <package-name>`

- Linux originated in the 1990s when Linus Torvalds developed a free, open source version of the Unix kernel. 
- The Linux system consists of five key layers: user, application, OS, kernel, and hardware. 
- The kernel is the lowest-level software and it enables applications to interact with your hardware. 
- The shell is an OS-level application for running commands. 
- You use a terminal to send commands to the shell. 

# WEEK 2

to check the default shell 

`printenv SHELL`

### To copy files

`cp /source/file /dest/filename` --it will paste with new name

`cp /source/file /dest/`    --to paste with same name

### To copy directories

`cp -r /source/dir/ /dest/dir/`

### To move files

`mv /source/file /dest/dir/`

### To move directories

`mv /source/dir/ /dest/dir/`

`mv Old New Documents`

### Chmod (change mode)
change file permissions

`ls -l filename` 
it will show file permissions i.e -rw-r--r-

`./main.sh`
bash: permission denied

`chmod +x main.sh`
`ls -l main.sh`
-rwxr-xr-x main.sh

`./main.sh`
hey linux is fun


The change of permissions is specified with the help of a combination of the following characters:

Option	Description
r, w and x	permissions: read, write and execute, respectively
u,g and o 	user categories: owner, group and all others, respectively
+, -	operations: grant and revoke, respectively
The command below removes read permission for all users (user, group and other) on the file usdoi.txt:

1
chmod -r usdoi.txt               
Copied!
You can verify the changed permissions by entering:

1
ls -l usdoi.txt
Copied!
To add read access to all users on usdoi.txt, enter:

1
chmod +r usdoi.txt                
Copied!
Now verify the changed permissions:

1
ls -l usdoi.txt
Copied!
To remove the read permission for ‘all other users’ category, enter:

1
chmod o-r usdoi.txt
Copied!
Verify the changed permissions:

1
ls -l usdoi.txt

**cat**
The cat command is used to display the contents of a file on the terminal.

`cat filename.txt`

**grep**
The grep command is used to search for a specific string or pattern within one or multiple files. For example:


`grep "example" filename.txt`

**sort**
The sort command is used to sort lines of text in a file alphabetically or numerically. For example:


`sort filename.txt`

**uniq**
The uniq command is used to remove duplicate lines of text from a file. For example:

`uniq filename.txt`

**cut**
The cut command is used to extract specific columns or fields from a file. For example, to extract the first two columns of a CSV file:

`cut -d ',' -f 1,2 filename.csv`

**paste**
The paste command is used to merge two or more files side by side. For example, to merge two files file1.txt and file2.txt:

`paste file1.txt file2.txt`

`ls -R`
recursively list the files

### View Networking Configuration

display hostname with domain
`hostname`

to drop the domain suffix
`hostname -s`

to display host ip address 
`hostname -i`

### `ifconfig`

to see the network info of eth0 (ethernet 0 )
`ifconfig eth0`

### Test connectivity. Send ICMP(Internet Control Message Protocols) packets to a host or IP Address

`ping google.com`

`ping -c 5 google.com`

print result after 5 packets

## curl - (Client URL)

Transfer data to and from URL

## wget - (web get)

Download files from a URL

# Summary
A shell is an interactive user interface 

You can use shell commands for navigating and working with files and directories, and to zip and unzip files 

You can use the “curl” and “wget” commands to display and download files from URLs 

The “echo” command prints string or variable values 

The “cat” and “tail” commands display file contents 

You can get user information with the "whoami" and "id" commands 

You can check system disk usage using the "df" command 

The “ls” command lists all files and directories contained within a specified directory tree 

The “cd” command allows you to navigate directories 

The “touch” command allows you to create a file or update its last–modified timestamp 

The “mkdir” command creates directories and “rmdir” deletes empty directories 

You can determine line, word, and character counts with “wc” 

You can use “grep” to get the lines of a file matching your desired criteria 

The “tar” command decompresses and unpacks a “tar.gz” archive 

You can view network configuration with “hostname” and “ifconfig” 


## Shell Scripting

`touch hello_world.sh`

`echo '# /bin/bash' >> hello_world.sh`

`echo 'echo hello world' >> hello_world.sh`

`ls -l hello_world.sh`

`chmod +x hello_world.sh`

`ls -l hello_world.sh`

`./hello_world.sh`

### Filters

wc, more, cat, head, tail

### Pipes (Pipelines)

Chain filters commands together
`ls | sort -r`

### Shell Variables

`set | head -4`

`var1='hello'`
`var2='world'`

`echo $var1 var2`

`unset var2`

### Environment Variables

Extended Scope

`export GREETING`
`echo $GREETING`
`env | grep 'GREE'`
`env | grep 'GREE' | xargs -n1 -I {} echo {}`

### Command Substitution

`$(command) or \`command\``

`here=$(pwd)`

`echo $here`

### Batch Mode

`command1; command2` - command 2 will only run when command 1 finishes.

### Concurrent Mode

`command1 & command2` - command 1 background pass to command 2 which will run in foreground

## Scheduling Jobs using Crontab

`crontab -e` -open the default editor

`add cronjob on the editor`

`save the file by pressing ctrl+x and press y`

# Summary

A shell script is an executable text file that begins with a ‘shebang’ interpreter directive 

Shell scripts are used to run commands and programs and can interpret command line arguments 

Filters are shell commands, and the pipe operator allows you to chain filter commands 

Shell variables can be assigned values with ‘=’ and listed using ‘set’ 

Environment variables are shell variables with extended scope; create with ‘export,’ list with ‘env’ 

Jobs can be scheduled to run periodically at selected times 

‘m h dom mon dow command’ is the cron job syntax 

Command substitution is used to replace a command with its output 

The Bash shell-scripting feature ‘concurrent mode’ allows commands to run in parallel 