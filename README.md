# Pi Gallery
Bash photo gallery using feh and nextcloud server.

## Server Usage
- Clone repository: `git clone https://github.com/natefduncan/pi-gallery.git`
- Create virtual environment in folder: `virtualenv venv`
- Activate environment: `source ./venv/bin/activate`
- Install pip packages: `pip3 install -r requirements.txt`
- Create .env file based on template.env file. 
- Start server: `python3 server.py`

## Client Usage
- Clone repository: `git clone https://github.com/natefduncan/pi-gallery.git`
- Install feh: `sudo apt-get install feh` 
- May need to also install libcurl: `sudo apt-get install libcurl`
- Start gallery: `source ./gallery.sh`

You can install `xscreensaver` to disable sleep. 