## Making an octave

One octave consists of 7 white notes and 5 black notes. If you look at the sketch, you can see that the blocks stretch from `x` to `x + 18`. The `for` loop needs to place a white key every 3 block-units on the `x` axis from `0` up to `18`.

- Now you can start making your octave function, placing a white key at every position provided by `i`.

	```python
	def make_octave(x, y, z):
		for i in range(0, 19, 3):
			white_key(player_x + i, player_y, player_z)
	```

- Save and run your code, then type `make_octave(player_x, player_y, player_z)` into the shell. You should see your white keys being placed in your Minecraft world.

- Next is the black keys. You can use the same system for placing these. Look at the sketch again. This time, the black keys need to be placed starting at `x = 2`. Within the `make_octave` function you can add another `for` loop.

	```python
	def make_octave(x, y, z):
		for i in range(0, 19, 3):
			white_key(player_x + i, player_y, player_z)
		for i in range(2, 18, 3):
			black_key(player_x + i, player_y, player_z)
	```

- Save and run your code again, then call the `make_octave` function.

- If you look at your octave, it's nearly done. There's just one key too many. A key has been placed at `x = 8`, and you need to make sure that this key is missed out. A little bit of conditional selection will help with this. If the value of `i` is `8` then the `black_key` function should not be called. Another way of putting this is *if i is not equal to 8" then the `black_key` function should be called.* Add this conditional to your function:

	```python
	def make_octave(x, y, z):
		for i in range(0, 19, 3):
			white_key(player_x + i, player_y, player_z)
		for i in range(2, 18, 3):
			if i != 8:	## leave a space as only 5 black keys
				black_key(player_x + i, player_y, player_z)
	```

- Save and run your code, and then call the `make_octave` function. You should see a piano octave being produced.

