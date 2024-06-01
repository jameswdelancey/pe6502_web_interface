# PE6502 Web Interface

This repository contains a package enabling the sending and receiving of machine code, Integer BASIC, and Applesoft BASIC code to the 6502 computer over serial via a web interface. Leveraging [Bottle](https://bottlepy.org), [pySerial](https://pyserial.readthedocs.io), and storage in [SQLite3](https://docs.python.org/3/library/sqlite3.html), it provides a user-friendly solution for loading and saving programs conveniently.

## Why?

- **Enhanced Accessibility**: The default load and save mechanisms for the pe6502 rely on RS232 serial, necessitating the presence of a computer or laptop. This package expands accessibility by allowing users to manage loading and saving operations from devices like smartphones or tablets via a web interface.
  
- **Effortless Program Management**: With a Raspberry Pi running standard Raspbian and the code provided in this repository, users can effortlessly load and save software, granting access to their library of programs with the tap of a link on their mobile device or through automation software.

## Scenarios and Use Cases

### Scenario 1: Porting Programs

- **Challenge**: You possess BASIC programs originally written for systems like the Commodore 64 and aim to adapt them to run on the pe6502.

- **Solution**: Utilize the web interface provided by this package to seamlessly adapt and transfer programs:
  1. Access the web interface from a desktop, laptop, or mobile device.
  2. Copy and paste the BASIC program into the "Add New" webform.
  3. Click "Run" to input the software into the pe6502.
  4. Test and adjust the program as necessary.
  5. When ready to save, click "Add New" and enter the appropriate command (e.g., LOAD in BASIC or memory addresses for Woz Mon).
  6. Submit the command to save your code.
  7. Edit descriptions or remove unwanted characters as needed.

## Installation

To set up and run the interface, follow these steps:

1. Clone the repository: `git clone https://github.com/jameswdelancey/pe6502_web_interface.git`
2. Install dependencies: `sudo pip3 install bottlepy pyserial`
3. Navigate to the directory: `cd pe6502_web_interface`
4. Execute the main script: `sudo python3 pe6502_web_interface/main.py` (sudo permission may be necessary for serial port access).

Please note that while this repository currently serves as a minimum viable product, it may evolve into a PyPI package in the future, hence its current structure.

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
