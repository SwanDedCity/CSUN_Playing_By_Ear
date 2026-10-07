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

# mom
image m neutral = Transform("sprites/mom_neutral.PNG")
image m happy = Transform("sprites/mom_happy.PNG")
image m concerned = Transform("sprites/mom_concerned.PNG")
image m sadSmile = Transform("sprites/mom_sadSmile.PNG")

# mom placeholder
image m = Transform("sprites/mom.png")

# sirenbird placeholder
image b happy = Transform("sprites/bird_happy.PNG")
image b surprised = Transform("sprites/bird_surprised.PNG")
image b sad = Transform("sprites/bird_sad.PNG")
image b covered = Transform("sprites/bird_covered.PNG")

# siren older placeholder
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

    scene stage_lights

    # This shows a character sprite. 

    show c happy at left
    show b happy at right

    # These display lines of dialogue.

    c "This is the of beginning script.rpy. Don't mind the bird's position, I'll change that later lol"


    #THIS IS A TEST OF THE MUSIC PUZZLE SCREEN. UNCOMMENT THE LINES BELOW TO TEST IT
    # highlight the lines below and press Ctrl + / to uncomment them
    ##
    define intro_puzzle = {
    "items": [
       {"id": "Guitar", "image": "items/piano.png", "x": 300, "y": 450},
       {"id": "Vocals", "image": "items/drums.png", "x": 1150, "y": 500}
    ],
    "solution": ["Guitar", "Vocals"]
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
