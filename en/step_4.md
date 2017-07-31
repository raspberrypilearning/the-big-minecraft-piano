## Receiving messages in Sonic Pi

The first step in this project is to try and send notes from Python to Sonic Pi. This is possible because Sonic Pi uses Open Sound Control (OSC). This is a way for sound synthesizers to communicate with each other over a network.

- The first thing to do is to tell Sonic Pi to listen out for messages. Load up Sonic Pi by clicking on `Menu` > `Programming` > `Sonic Pi`, and then click into `Buffer 0` to start writing code.

- You just need a few lines of code in your Sonic Pi file, which are explained below.

	```ruby
	set_sched_ahead_time! 0
	live_loop :listen do
	  message = sync "/play_this"
	  note = message[:args][0]
	  play note
	end
	```

	1. `set_sched_ahead_time! 0` tells Sonic Pi to keep listening without any delay, so the notes are played quickly.
	1. `live_loop :listen do` starts a *live loop* that will run forever. Live loops need their own unique names, so this one has been called `listen`.
	1. `message = sync "/play_this"` creates a variable when the message `/play_this` is heard by Sonic Pi. The `message` will be a dictionary.
	1. `note = message[:args][0]` picks out the contents of the message that was sent. In this case, the dictionary contains a *key* called `args`. The value of the key is going to be a list. As you'll be sending one note at a time, the list will only have a single number at position 0.
	1. `play note` will play the MIDI value that was sent.

- You can now run this script. Nothing will happen yet, because Sonic Pi is not receiving any messages.

