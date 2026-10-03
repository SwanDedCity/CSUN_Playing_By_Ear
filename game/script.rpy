# The main script of the game goes in this file.

# Define character images

# chase
image c neutral = Transform("sprites/chase_neutral.PNG")
image c happy = Transform("sprites/chase_happy.PNG")
image c surprised = Transform("sprites/chase_surprised.PNG")
image c upset = Transform("sprites/chase_upset.PNG")
image c grumpy = Transform("sprites/chase_grumpy.PNG")

# chase formal
image c neutral formal = Transform("sprites/chase_neutral_formal.PNG")
image c happy formal = Transform("sprites/chase_happy_formal.PNG")
image c surprised formal = Transform("sprites/chase_surprised_formal.PNG")
image c upset formal = Transform("sprites/chase_upset_formal.PNG")
image c grumpy formal = Transform("sprites/chase_grumpy_formal.PNG")

 # mom placeholder
image m = Transform("sprites/mom.png")

# sirenbird
image s neutral = Transform("sprites/sirenbird.PNG", xalign=0.5, yalign=0.5)

# Define characters for dialogue
define c = Character("Chase")
define w = Character("???")
define m = Character("Timothy's mother")

# Other definitions

define scene_interlude = Fade(2.0, 0.5, 0.0)

 #Custom Audio Channels
init python:
    renpy.music.register_channel("ringtone", mixer="sfx", loop=True)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. 

    show c happy at left

    # These display lines of dialogue.

    c "This is the of beginning script.rpy"


    #THIS IS A TEST OF THE MUSIC PUZZLE SCREEN. UNCOMMENT THE LINES BELOW TO TEST IT
    # highlight the lines below and press Ctrl + / to uncomment them
    ##
    define intro_puzzle = {
    "items": [
       {"id": "piano", "image": "items/piano.png", "x": 300, "y": 450},
       {"id": "drums", "image": "items/drums.png", "x": 1150, "y": 500}
    ],
    "solution": ["drums", "piano"]
    }
    call screen music_puzzle(intro_puzzle)

    play music "fantasy song demo.mp3"
    c "I got it."
    ##
    

    "Now it's over. The actual begins begins."
    "We jump to scene 1 in the events folder"
    jump scene1_start


#This ends the game
label endGame:
    "The game is over. Thanks for playing!"
    return
