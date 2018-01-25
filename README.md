# pirobot
Repository for the development of the Robot Pi Project

Basic instructions
Power on the Pi
The IP address of the pi **should** be the same as the address on the label.
If not then check with Mr De Borde.

There are two way sot connect to the Pi
1. an SSH connection to execute the scripts
2. an SMB connection to up load and edit the script files with your favourite editor (eg: PyCharm or Atom)


### SSH connection

Open a terminal (ssh) to the Pi

>`ssh pi@10.0.14.XXX`

*password* = raspberry

Then at the terminal prompt

>`pi@PiRobotMaster:~ $`

change directory to the scripts www_folder

> `cd scripts`

then run your script (for example)

> `python3 gpio_test.py`

## SMB connection

### OSX

Finder > Go > Connect to Server (⌘K)

connect to
> smb://10.0.14.XXX

username = *pi*, password = *password*

Connect to the share point *pi*

### Windows

Map a network drive to 10.0.14.XXX


<hr>
### script_folder

Contains the scripts run for the Robot

<hr>
### www_folder
Contains the pages for the built in web server
