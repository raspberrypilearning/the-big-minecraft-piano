## Building black keys

- You can use a function to build your first black key. A function is a block of named code that performs some task. You can call this one *black_key*. The function will need to know where to build the black piano key, so it will need three parameters. These parameters will be the x, y, and z position in the Minecraft world where the key needs to be built.

	```python
	def black_key(x, y, z):
	```

- The next step is to use the `setBlocks` function, to set a few black Minecraft blocks. If you look at the black key on the far left, you can see that it's 2 blocks wide and 9 blocks long. So if the first block is placed at an `x` and `z` coordinate, then you need the one to its right to be placed at `x + 1`, and the ones below it to be placed at `z + 1` up to `z + 8`. All the blocks can be placed at 1 block below the player's position - `y - 1`.

	Obsidian seems like a sensible material to build the blocks from. This has a `blockId` of `49`.

	```python
	def black_key(x, y, z):
		mc.setBlocks(x, y - 1, z, x + 1, y - 1, z + 8, 49)
	```

- Test your code by running it, and then type the following into the shell to *call* your function. Make sure you've moved Steve to a clear bit of space first.

	```python
	>>> black_key(player_x, player_y, player_z)
	```

- Move Steve around and you should be able to see a black piano key in the Minecraft world.

