## Making the octave again

- Let's tie all that together now. At the end of all the functions you've made, you can now call the functions in your code, and use three lines to set it all up. First bulldoze the area, then make the piano, and then on the last line set the player's position, so that Steve moves to the middle of the piano.

	```python
	bulldozer(player_x, player_y, player_z)
	make_octave(player_x, player_y, player_z)
	mc.player.setPos(player_x + 8, player_y + 3, player_z + 12)
	```

- Now when you save and run your code a piano octave should appear beneath your feet. Each time you run the code, a new octave will be produced.

