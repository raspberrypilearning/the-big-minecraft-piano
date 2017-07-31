## Clearing some space

- Depending on where you are in the Minecraft world, you might find your piano could be created in the middle of a mountain. To prevent this you can clear some space with a `bulldozer` function, that will fill a cube around the player with air.

	```python
	def bulldozer(x, y, z):
		mc.setBlocks(x - 30, y - 3, z - 30, x + 30, y + 20, z + 30, 0)
	```

- You can test this out by saving and running your code and then calling the function, with Steve's position, in the shell.

	```python
	>>> bulldozer(player_x, player_y, player_z)
	```

- You should see that the environment around Steve has been flattened.

