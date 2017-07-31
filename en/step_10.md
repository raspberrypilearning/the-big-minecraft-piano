## Building white keys

- Have a look at the first white key in the sketch. It's three blocks wide and 15 blocks long. This time, you need to set blocks from `x` up to `x + 2`, and from `z` up to `z + 14`.

	You can write a function to do this using the white tile block, which has a `blockId` of `44, 7`. The `44` is the tile block, and the `7` tells Minecraft that it should be white.

	```python
	def white_key(x, y, z):
		mc.setBlocks(x, y - 1, z, x + 2, y - 1, z + 14, 44, 7)
	```

- Again, you can run your code and then type the following into the shell to see the white key being produced.

	```python
	>>> white_key(player_x, player_y, player_z)
	```

