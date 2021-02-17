## Building piano keys

It may seem a little daunting to try and build a piano in Minecraft, so it's easier to try and break down the problem into much smaller chunks. This is a process that computer scientists call *decomposition.*

A piano keyboard is made up of repeating groups of 7 white keys and 5 black keys. This is called an **octave**. Building each of these elements one at a time will allow you to easily build a keyboard.

- Start by creating a new Minecraft world. Click on `Menu` > `Games` `Minecraft`, then click on `Start Game` and finally `Create New World`.

- To begin with, you need to import the Minecraft Pi module and get the player's current position. Add a few more lines of code so that the start of your file looks like this:

	```python
	from pythonosc import osc_message_builder
	from pythonosc import udp_client
	from mcpi.minecraft import Minecraft
	from time import sleep

	sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
	mc = Minecraft.create()

	player_x, player_y, player_z  = mc.player.getTilePos()
	```

