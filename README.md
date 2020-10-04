# ![Logo](https://raw.githubusercontent.com/NiveditJain/muZik/master/files/logo.png) Democratic Party Music Control (CLI) <br>
![Python Version](https://img.shields.io/badge/Python-3.7.4-blue)
![Under Dev](https://img.shields.io/badge/Under-Development-red)
![Pull Requests](https://img.shields.io/badge/Pull%20Requests-Not%20Accepting-purple)
![build passing](https://img.shields.io/badge/Build-Passing-green)
![visitors](https://visitor-badge.glitch.me/badge?page_id=muZik.visitor-badge)
<br>
![Party GiF](https://raw.githubusercontent.com/NiveditJain/muZik/master/files/party.gif)
<br>

## About
The story begins with around 8 friends sitting in a hostel room of
IIT-Jodhpur, trying to find some ideas for a Hackathon (which 
eventually was cancelled) and fighting for whose music to play.
Solution? lets Vote. This project aims to serve this use-case. <br><br>
People connected over the same local network can connect to
it and add their favourite music to the server, 
vote (Upvote/Downvote) for the music they like/dislike,
can listen to music from server to their devices and Paaarrrty! <br><br>
This project also aims to replace small DJs usually in small parties,
with a microcontroller-based local area server running on IPv4 and
connected to large speakers. Giving people in the party democratic
control over music using their mobile phones or any other device 
which could be connected to the private local area network.

## Current Features

### AutoPlay 
Server mains a playlist of song in present instance and automatically
plays the highest priority song, priority decided by weight of 
upvote and downvote.

### Upload Song
Connected clients can add there song to the playlist.

### Upvote Song
Connected clients can upvote the song(s) which they like.

### Downvote Song
Connected clients can downvote the song(s) which they dislike.

### Playlist
Connected clients can view playlist

### Local Plat
Connected clients can play a song from server on there local machine.

## Getting Started

### Get Code
Download (clone code) from this repository and add Sever and Client folders to Server and Client machines respectively.

### Install Python 3.7.4
On all client machines and server machine install Python 3.7.4. Install from [here](https://www.python.org/downloads/release/python-374/)

### Install pip
for windows machines <br>
```
python get-pip.py
```

for mac/linux <br>
```
python3 get-pip.py
```

### Upgrade pip
for windows use <br>
```
pip install --upgrade pip
```

for mac/linux <br>
```
pip2 install --upgrade pip3
```

### Install Dependencies
for windows run <br>
```
pip install -r requirements.txt
```

for mac/linux <br>
```
pip3 install -r requirements.txt
```

make sure that requirements.txt is in your working directory.

### Setting Server
Go to settings.py file inside server (folder) and set all the variables are per requirements, make sure that EXCHANGE_SIZE has same value for server and all clients.

### Running Server
Go to directory where you saved server folder and run

for windows run <br>
```
python server
```

for mac/linux <br>
```
python3 server
```

On successful start you should get something like <br>
![Sever Success](https://raw.githubusercontent.com/NiveditJain/muZik/master/files/server_success.png)
Please note the address on which server is running you need to enter it in client files. Ours is running on 192.168.29.229:8080 (highlighted in red).

### Setting Clients
Go to settings.py from client folder and make necessary settings make sure that EXHANGE_SIZE must have same value for all clients and server

## How to Use?

## Working

## Contributors
+ [Nivedit Jain](https://github.com/NiveditJain) (B18CSE039)
+ [Eashan Jindal](https://github.com/eashanjindal) (B18CSE013)

### Note
This project was started at [IIT-Jodhpur](http://iitj.ac.in/) under guidance of [Dr. Ravi Bhandari](https://www.linkedin.com/in/ravi-bhandari-b1172415/) as course project for CS311-Data Communication, Pre-Final Year, BTech Computer Science and Engineering, Trimester 1 (September - November 2020).
