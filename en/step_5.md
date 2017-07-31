## Sending messages to Sonic Pi

- Open up a new Python 3 file by clicking `Menu` > `Programming` > `Python 3 (IDLE)`, then clicking on `File` > `New File`.

- You'll need the `python-osc` module for this project, so make sure you have installed it by following the instructions on the [software](https://projects.raspberrypi.org/en/projects/the-big-minecraft-piano/requirements/software/) page.

- The first few lines you need just import the necessary methods from the module.

	```python
	from pythonosc import osc_message_builder
	from pythonosc import udp_client
	```

- Next, you need to create an object that will send the message. Open Sound Control uses a method of communicating called [UDP](https://simple.wikipedia.org/wiki/User_Datagram_Protocol) (User Datagram Protocol). This is a method computers often use to talk to each other over the internet. You could use this to get two different Raspberry Pis to talk to each other, but your Python program and Sonic Pi script are both running on the same machine.

	As both programs are on the same Raspberry Pi, you can use the *home* address of the Raspberry Pi to tell Python where to send the message. A computer always gives itself the same IP address for programs to talk to each other, which is `127.0.0.1`.

	Messages sent using UDP also need to include a port number. Port numbers let programs know that the message was meant for them. Sonic Pi is going to listen for messages using port number `4559`, so your Python program needs to use this port number in its messages.

	```python
	sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
	```

- Save and run your code (`Ctrl`+`S` and then `F5`). Nothing will happen yet, but you can test out the connection in the shell. Switch over to the shell and type the following:

	```python
	>>> sender.send_message('/play_this', 60)
	```

- You should hear the note *60* being played by Sonic Pi, which is middle C.

- You can now turn this into a function. Go back to your Python 3 file and create a function that takes a single argument `note` and plays that note.

	```python
	def play_note(note):
		'''Take an integer note value and send it to Sonic Pi'''
		sender.send_message('/play_this', note)
		sleep(0.5)
	```

- If you save and run your code, you can then test out your function in the shell. For instance, each of these lines should play a note.

```python
>>> play_note(60)
>>> play_note(61)
>>> play_note(62)
```

