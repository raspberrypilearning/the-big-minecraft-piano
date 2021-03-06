from pythonosc import osc_message_builder
from pythonosc import udp_client
from mcpi.minecraft import Minecraft
from time import sleep

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
mc = Minecraft.create()

player_x, player_y, player_z  = mc.player.getTilePos()

def play_note(note):
    '''Take an integer note value and send it to sonic pi'''
    sender.send_message('/play_this', note)
    sleep(0.5)

def black_key(x, y, z):
    '''Take an x, y and z position in minecraft and build a black piano key'''
    mc.setBlocks(x, y - 1, z, x + 1, y - 1, z + 8, 49)

def white_key(x, y, z):
    '''Take an x, y, and z position in minecraft and build a white piano key'''
    mc.setBlocks(x, y - 1, z, x + 2, y - 1, z + 14, 44, 7)

def make_octave(x, y, z):
    '''Take an x, y, and z position in minecraft and build an octave of white and black keys'''
    for i in range(0, 19, 3):
        white_key(player_x + i, player_y, player_z)
    for i in range(2, 18, 3):
        if i != 8:  ##leave a space as only 5 black keys
            black_key(player_x + i, player_y, player_z)

def bull_dozer(x, y, z):
    '''take an x, y, and z position in minecraft and replace a large block of space with air'''
    mc.setBlocks(x - 30, y - 3, z - 30, x + 30, y + 20, z + 30, 0)


if __name__ == "__main__":
    ## Create the Piano
    bull_dozer(player_x, player_y, player_z)
    make_octave(player_x, player_y, player_z)
    mc.player.setPos(player_x + 8, player_y + 3, player_z + 12)

    ## Find the players relative position and block Steve's standing on
    ## Play the corresponding note
    while True:
        new_x, new_y, new_z = mc.player.getTilePos()
        block_below = mc.getBlock(new_x, new_y - 1, new_z)
        if block_below == 0: ##Needed because of height difference with black and white keys
            block_below = mc.getBlock(new_x, new_y, new_z)
        relative_position = player_x - new_x ## find the position on the piano
        white_notes = [60, 62, 64, 65, 67, 69, 71]
        black_notes = [61, 63, 0,  66, 68, 70]
        if block_below == 44: # if a white note
            notes_along = relative_position // -3
            play_note(white_notes[notes_along])
        if block_below == 49: # if a black note
            notes_along = ((relative_position - 1) // -3) - 1 
            play_note(black_notes[notes_along])

