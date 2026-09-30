# The main script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

 #Custom Audio Channels
init python:
    renpy.music.register_channel("ringtone", mixer="sfx", loop=True)

image c happy = Transform("chase_happy.png")

define c = Character("Chase")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show c happy at left

    # These display lines of dialogue.

    c "Hello, my name is Brandon."

    c "hello hahahaha"

    c "This is the beginning of the template."

    c "And now it's over. LOL. Now the actual game begins"

    #THIS IS A TEST OF THE MUSIC PUZZLE SCREEN. UNCOMMENT THE LINES BELOW TO TEST IT
    # highlight the lines below and press Ctrl + / to uncomment them
    ##
    #define intro_puzzle = {
    #"items": [
    #    {"id": "piano", "image": "images/piano.png", "x": 300, "y": 450},
    #    {"id": "drums", "image": "images/drums.png", "x": 1150, "y": 500}
    #],
    #"solution": ["drums", "piano"]
    #}
    #call screen music_puzzle(intro_puzzle)

    #play music "fantasy song demo.mp3"
    #c "I got it."
    ##



    # This ends the game.

    jump scene1_start



label endGame:
    
    "The game is over. Thanks for playing!"

    return
