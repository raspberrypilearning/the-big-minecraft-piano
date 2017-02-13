# The Big Minecraft Piano

In this project, you're going to create a piano keyboard in Minecraft that can be played when Steve walks over the keys.

This project uses Sonic Pi to play the music, Minecraft to visualise the piano and act as your input, and Python to build the piano and act as a way for Sonic Pi and Minecraft to communicate with each other.

## Receiving messages in Sonic Pi

The first step in this project is to try and send notes from Python to Sonic Pi. This is possible becuase Sonic Pi has Open Sound Control server, that can listen out for messages sent by other pieces of software.

1. The first thing to do is to tell Sonic Pi to listen out for messages. Load up Sonic Pi by clicking on `Menu` > `Programming` > `Sonic Pi`

1. You just need a few lines of code in your Sonic Pi file, which are explained below.

	```ruby
	set_sched_ahead_time! 0
	live_loop :listen do
	  message = sync "/play_this"
	  note = message[:args][0]
	  play note
	end
	```
	1. `set_sched_ahead_time! 0` tells Sonic Pi to keep listening without any delay, so the notes are played quickly.
	1. `live_loop :listen do` starts a *live loop* that will run forever. Live loops need there own unique names so this one has been called `listen`
	1. `message = sync "/play_this"` creates a variable when the message `/play_this` is heard by sonic pi. The `message` will be a dictionary.
	1. `note = message[:args][0]` picks out the contents of the message that was sent. In this case the dictionary contains a *key* called `args`. The value of the key is going to be a list. As you'll be sending one note at a time, the list will only have a single number at position 0.
	1. `play note` will play the midi value that was sent.

1. You can now run this script. Nothing will happen yet, because Sonic Pi is not receiving any messages.

## Sending messages to Sonic Pi

1. Open up a new Python3 file by clicking `Menu` > `Programming` > `Python 3 (IDLE)`, then clicking on `File` > `New File`

1. You'll need the `python-osc` module for this project, so make sure you have installed it by following the instructions on the ![software](software.md) page.

1. The first few lines you need just import the neccessary methods from the module.

	```python
	from pythonosc import osc_message_builder
	from pythonosc import udp_client
	```
	
1. Next you need to creat an object that will send the message. OSC uses the UDP protocol. As you're comminicating with Sonic Pi locally, you can use the *home* address of the Raspberry Pi, which is 127.0.0.1. Sonic Pi will be listening on port 4559.

	```python
	sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
	```

1. Save and run your code (`ctrl`+`s` and then `F5`). Nothing will happen yet, but you can test out the connection in the shell. Switch over to the shell and type the following.

	```python
	>>> sender.send_message('/play_this', 60)
	```

1. You should hear the note *60* being played, which is middle C

1. You can now turn this into a function. Go back to your Python3 file and create a function that takes a single argument `note` and plays that note.

	```python
	def play_note():
		'''Take an integer note value and send it to sonic pi'''
		sender.send_message('/play_this', note)
		sleep(0.5)
	```
	
1. If you save and run your code, you can then test out your function is the shell. For instance, each of these lines should play a note.

	```python
	>>> play_note(60)
	>>> play_note(61)
	>>> play_note(62)
	```
