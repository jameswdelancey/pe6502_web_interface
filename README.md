# Introduction

This package will send and receive machine code, Integer BASIC, and Applesoft 
BASIC code to the 6502 computer over serial via a web interface. The package is 
based on [Bottle](https://bottlepy.org), 
[pySerial](https://pyserial.readthedocs.io), and storage in 
[sqlite3](https://docs.python.org/3/library/sqlite3.html).

# Why?
- The load and save mechanisms for the pe6502 out of the box are implemented 
via RS232 serial, but as a user of the computer you need a computer/laptop or 
something nearby to conduct saving and loading. 
- Using a [RaspberryPi](https://www.raspberrypi.org/) with "stock" Raspbian 
configuration and the code in this repo, we we are able to controll loading and 
saving from a cell phone, for example, via a web interface.
- Additionally we have access to our library of software, which we can load at 
the push of a link on our cell phone. (It would of course work on a computer or 
via automation software, etc.)

# Scenarios and Use Cases

## Scenario 1
- I have a lot of BASIC programs written for Commodore 64, or other 
computers, and I want to check and/or tweak them in any way required to run on 
my pe6502.

## Solution 1
- With a desktop, laptop computer or cell phone
- Copy and paste the BASIC program into the "Add New" webform as shown in 
  images below, then
- Click "Run" to have the software input into the pe6502. 
- Test the software. 
- Tweak anything requied to get the software working. 
- When you're ready to backup / save the work, click "Add New", 
- Enter the command required to get the software to output the code (LOAD in 
  basic or 300.2000 [for example] in Woz Mon to get the hex output of the block 
  of RAM holding the program.
- Press the "Submit" button to save your code
- The software will run the command you entered (usually LOAD) and capture the 
output
- Your code is now saved in the table and you can edit the description and any 
leading or trailing spaces or characters you wish to remove by clicking edit

# Installation

To run, do the following:

- Clone the repo `git clone 
https://github.com/jameswdelancey/pe6502_web_interface.git`
- Install the dependencies `sudo pip3 install bottlepy pyserial`
- Enter the directory `cd pe6502_web_interface`
- Execute with this command: `sudo python3 pe6502_web_interface/main.py` (sudo 
is required for serial port access on my machine.)

This is a minimum viable product at this point but will likely be cleaned up 
into a pypi package, hence the structure.

Requires pyserial and bottlepy.

## Pic of the board
![.gif](https://github.com/jameswdelancey/pe6502_web_interface/raw/main/docs/_static/1-0.jpg)

## Nothing in RAM
![.gif](https://github.com/jameswdelancey/pe6502_web_interface/raw/main/docs/_static/1-1.jpg)

## Open website from app and find content
![.gif](https://github.com/jameswdelancey/pe6502_web_interface/raw/main/docs/_static/1-2.jpg)

## Edit or view if you like before running
![.gif](https://github.com/jameswdelancey/pe6502_web_interface/raw/main/docs/_static/1-3.jpg)

## Click Run to send to 6502 computer over serial
![.gif](https://github.com/jameswdelancey/pe6502_web_interface/raw/main/docs/_static/1-4.jpg)

## Type LIST to make sure it's there
![.gif](https://github.com/jameswdelancey/pe6502_web_interface/raw/main/docs/_static/1-5.jpg)

## Import BASIC or machine code by reading 6502 output from serial
![.gif](https://github.com/jameswdelancey/pe6502_web_interface/raw/main/docs/_static/1-6.jpg)

## Notice the new ID 5
![.gif](https://github.com/jameswdelancey/pe6502_web_interface/raw/main/docs/_static/2-0.jpg)

## Edit to add description or title
![.gif](https://github.com/jameswdelancey/pe6502_web_interface/raw/main/docs/_static/2-1.jpg)

