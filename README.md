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
Go to settings.py from client folder and make necessary settings make sure that EXCHANGE_SIZE must have same value for all clients and server. Also make sure that you have entered correct address of the server in settings.py (client).
<br>
We are now ready to start the clients!

## How to Use?
We have made a complete linux styled CLI. Mak sure to run these commands after completing all the above setups and starting server. Also ensure you are running these commands in directory where client folder is placed.<br>
**Note :** We are writing here commands for Windows for Linux or Mac just replace python with python3, all things would work same like any other CLI interface.

### Help 
```
python client --help
```
or 
```
python client -h
```
This will will be there to help you, you can run it anytime, it should show you
![Help](https://raw.githubusercontent.com/NiveditJain/muZik/master/files/help.png)

### Upload 
use to upload file to the server
```
python client -op/--operation upload -n/--name [music name] -p/--path [file path]
```
**Note :** / denotes or, you can use any one of the flag to specify the parameters. <br>
It will upload the file your music to the server <br>

`--n/--name` is required, denotes the name for your music <br>
`-p/--path` is required, denotes the file path of file on your system <br>

### List
displays you a list of songs in current playlist, in the format (Name - id - value)
```
python client -op/--operation list
```

### Playing
will get you the name of song which is currently being played
```
python client -op/--operation playing
```

### Local Play
will play the song on your local machine, getting file from the server
```
python client -op/--operation local_playing -id/--id [song id from list]
```
`-id/--id` is required, denotes the id of song to play, get id using the list feature

### Upvote
to upvote a song use 
```
python client -op/--operation upvote -id/--id [song id to upload]
```
`-id/--id` is required <br>
to play the song before upload add the flag `-l/--listen`
```
python client -op/--operation upvote -id/--id -l/--listen
```
it will play the song on your local machine till you press `ctrl + c (cmd + c)`

### Downvote
all working same as upvote just replace upvote to downvote all the commands,eg,
```
python client -op/--operation downvote -id/--id [song id to upload]
```

## Working
For each communication client sends a appropriate flag to server, which fires related communication functions in both server and client.
![Sever Success](https://raw.githubusercontent.com/NiveditJain/muZik/master/files/base.png)
Flags Presently in use,
| Flag | Used for indicate |
| :--: | :---------------: |
| $FLAG:00 | DISCONNECT |
| $FLAG:01 | CREATE_OBJ |
| $FLAG:02 | CREATE_UPVOTE |
| $FLAG:03 | CREATE_DOWNVOTE |
| $FLAG:04 | GET_LIST |
| $FLAG:05 | SUCCESS |
| $FLAG:08 | PLAYING |
| $FLAG:06 | NONE |
| $FLAG:09 | LISTEN |

### Upload
![Upload Working](https://raw.githubusercontent.com/NiveditJain/muZik/master/files/1.jpg)

### Upvote/Downvote
![Upvote Downvote Working](https://raw.githubusercontent.com/NiveditJain/muZik/master/files/2.jpg)

### Playing/List
![Playing List Working](https://raw.githubusercontent.com/NiveditJain/muZik/master/files/3.jpg)

### Listen
![Listen Working](https://raw.githubusercontent.com/NiveditJain/muZik/master/files/4.jpg)

## Code 

### Server
#### Directory structure
```
server
|___ __main__.py
|___ flags.py
|___ music.py
|___ request_handler.py
|___ runchecks.py
|___ settings.py
|___ setup.py
|
    
```
#### Dependencies and Responsibilities
| File | Responsibility | Dependent on |
| :--: | :------------: | :----------: |
| settings.py | allow user to make necessary settings | |
| runchecks.py | checks that all settings are proper | settings.py |
| setup.py | make necessary setups | settings.py |
| flags.py | contains all necessary flags | |
| music.py | contains Music and Playlist Class and running playlist | settings.py |
| request_handler.py | handles all communications and plays the appropriate song | flags.py, settings.py, music.py, playsound |
| __main__.py | starts server, fires all triggers and handles threading for requests | runchecks.py, setup.py, settings.py, request_handler.py |


### Client
#### Directory structure
```
client
|___ __main__.py
|___ flags.py
|___ client_functions.py
|___ runchecks.py
|___ settings.py
|___ setup.py
|___ utils.py
|
    
```
### Dependencies and Responsibilities
| File | Responsibility | Dependent on |
| :--: | :------------: | :----------: |
| settings.py | allow user to make necessary settings | |
| runchecks.py | checks that all settings are proper | settings.py |
| setup.py | make necessary setups | settings.py |
| flags.py | contains all necessary flags | |
| utils.py | provide some additional functionality features | settings.py |
| client_functions.py | handles all communications for client | flags.py, settings.py, utils.py, playsound |
| __main__.py | provide CLI interface and start all features| runchecks.py, setup.py, client_functions.py |



## Contributors
+ [Nivedit Jain](https://github.com/NiveditJain) (B18CSE039)
+ [Eashan Jindal](https://github.com/eashanjindal) (B18CSE013)

### Note
+ This project was started at [IIT-Jodhpur](http://iitj.ac.in/) under guidance of [Dr. Ravi Bhandari](https://www.linkedin.com/in/ravi-bhandari-b1172415/) as course project for CS311-Data Communication, Pre-Final Year, BTech Computer Science and Engineering, Trimester 1 (September - November 2020).
+ We would be further looking to make this a complete working product, to contribute or join us, please send an email on [jain.22@iitj.ac.in](mailto:jain.22@iitj.ac.in)
+ <a href="https://raw.githubusercontent.com/NiveditJain/muZik/master/files/beamed_note.png">Beamed Note Symbol</a> on our diagram, does not belongs to any institute or organization.
+ All our images in this ReadMe are made from free images collections from [Canva](https://www.canva.com/)