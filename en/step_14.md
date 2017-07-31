## Playing your piano

The next step is to have the piano play a note when Steve walks over a key.

- To begin you'll need an infinite loop that will constantly get Steve's latest position. All your code from now on needs to be placed **inside** this `while True` loop.

	```python
	while True:
		new_x, new_y, new_z = mc.player.getTilePos()
	```

- Next, you need to find the block below Steve's feet. The problem is that the white keys are only half a block in height. If Steve is standing on a white tile, because of their smaller height `block_below` ends up being the air that's beneath the piano. You can handle this with a conditional, and check if the block below is not a white or black key.

	```python
		block_below = mc.getBlock(new_x, new_y - 1, new_z)
		if block_below != 44 and block_below != 49:
			block_below = mc.getBlock(new_x, new_y, new_z)
	```

- You can now find Steve's position relative to the piano's position. The piano was placed at `player_x`, but Steve is now standing at `new_x`. Subtracting one from the other will tell you where Steve is standing on the piano octave.

	```python
		relative_position = player_x - new_x ## find the position on the piano
	```

- Now you can make a list of the notes to be played. Starting from middle C, the white notes have MIDI values of 60, 62, 64, 65, 67, 68, and 71. The black notes are the MIDI values in between the white notes. You can place a 0 into the `black_notes` as there are only 5 of them on the keyboard.

	```python
		white_notes = [60, 62, 64, 65, 67, 69, 71]
		black_notes = [61, 63, 0,  66, 68, 70]
	```

- The specific white note to play, if Steve is standing on the white note, can be found by dividing his relative `x` position by 3 and then ignoring the remainder. This is called floor division, and can be done in Python using the `//` operator.

	```python
		if block_below == 44:
			notes_along = relative_position // -3
			play_note(white_notes[notes_along])
	```

- You can find the black note to play by subtracting `1` from Steve's relative position, floor dividing by 3, and then subtracting `1` again. This is because the notes are only 2 blocks wide.

	```python
		if block_below == 49:
			notes_along = ((relative_position - 1) // -3) - 1
			play_note(black_notes[notes_along])
	```

- And that's it. Try running your code and then moving over the blocks. So long as Sonic Pi is open and running your initial script, you should hear the piano being played each time Steve is on a particular key.

