## Receiving messages in Sonic Pi

The first step in this project is to try and send notes from Python to Sonic Pi. This is possible because Sonic Pi uses Open Sound Control (OSC). This is a way for sound synthesizers to communicate with each other over a network.

- The first thing to do is to tell Sonic Pi to listen out for messages. Load up Sonic Pi by clicking on `Menu` > `Programming` > `Sonic Pi`, and then click into `Buffer 0` to start writing code.

- You just need a few lines of code in your Sonic Pi file, which are explained below.

	```ruby
	live_loop :listen do
	    use_real_time
	    note = sync "/osc*/play_this"
	    play note[0]
	end
	```

	1. `live_loop :listen do` starts a *live loop* that will run forever. Live loops need their own unique names, so this one has been called `listen`.
	1. `use_real_time` ensures that Sonic Pi will play the note as soon as the message is received.
	1. `note = sync "/osc*/play_this"` creates a variable when the message `/osc*/play_this` is heard by Sonic Pi. The `message` will be a list.
	1. `play note[0]` will play the MIDI value that was sent.

- You can now run this script. Nothing will happen yet, because Sonic Pi is not receiving any messages.

