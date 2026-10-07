init python:
    renpy.music.register_channel("instrument1", "sfx", loop=False)
    renpy.music.register_channel("instrument2", "sfx", loop=False)
    renpy.music.register_channel("instrument3", "sfx", loop=False)
# screen music_puzzle(puzzle):

#     modal True

#     default chosen = []
#     default hovered_item = None

#     $ complete = len(chosen) == len(puzzle["solution"])
#     $ correct = complete and chosen == puzzle["solution"]
#     $ wrong = complete and not correct

#     for item in puzzle["items"]:

#         imagebutton:

#             # if selected in wrong order all items will highlight red
#             if wrong:
#                 idle At(Transform(item["image"], zoom=0.5), outline_red_thick)
#                 hover At(Transform(item["image"], zoom=0.5), outline_red_thick)
#                 action NullAction()

#             # selected state
#             elif item["id"] in chosen:
#                 idle At(Transform(item["image"], zoom=0.5), outline_white_thick)
#                 hover At(Transform(item["image"], zoom=0.5), outline_white_thick)
#                 action NullAction()

#             # hover state
#             elif hovered_item == item["id"]:
#                 idle At(Transform(item["image"], zoom=0.5), outline_white_thin)
#                 hover At(Transform(item["image"], zoom=0.5), outline_white_thin)
#                 action SetScreenVariable("chosen", chosen + [item["id"]])

#             # normal state
#             else:
#                 idle Transform(item["image"], zoom=0.5)
#                 hover Transform(item["image"], zoom=0.5)
#                 action SetScreenVariable("chosen", chosen + [item["id"]])

#             hovered SetScreenVariable("hovered_item", item["id"])
#             unhovered SetScreenVariable("hovered_item", None)

#             focus_mask True
#             xpos item["x"]
#             ypos item["y"]
#             xanchor 0
#             yanchor 0

#     if wrong:
#         text "Try again!":
#             xalign 0.5
#             yalign 0.2

#         timer 1.0 action [SetScreenVariable("chosen", []), SetScreenVariable("hovered_item", None)]

#     if correct:
#         timer 0.1 action Return(True)

screen music_puzzle(puzzle):

    modal True
    default chosen = []
    default hovered_item = None

    $ complete = len(chosen) == len(puzzle["solution"])
    $ correct = complete and chosen == puzzle["solution"]
    $ wrong = complete and not correct
    default play_button = False



    vbox:
        align (0.5, 0.75)
        xysize (1150, 110)
        for item in puzzle["items"]:
            fixed:
                add "gui/music_mechanic/audio_template.png"
                text item["id"]:
                    xalign 0.1
                    yalign 0.0
                if item["id"] in chosen:
                    add "gui/music_mechanic/audio_selected.png"
    imagebutton auto "gui/music_mechanic/play_%s.png":
            focus_mask True
            action SetScreenVariable("play_button", True)


    for item in puzzle["items"]:

        imagebutton:

            # if selected in wrong order all items will highlight red
            if wrong:
                idle At(Transform(item["image"], zoom=0.5), outline_red_thick)
                hover At(Transform(item["image"], zoom=0.5), outline_red_thick)
                action NullAction()

            # selected state
            if item["id"] in chosen:
                idle At(Transform(item["image"], zoom=0.5), outline_white_thick)
                hover At(Transform(item["image"], zoom=0.5), outline_white_thick)
                action NullAction()

            # hover state
            elif hovered_item == item["id"]:
                idle At(Transform(item["image"], zoom=0.5), outline_white_thin)
                hover At(Transform(item["image"], zoom=0.5), outline_white_thin)
                action SetScreenVariable("chosen", chosen + [item["id"]])

            # normal state
            else:
                idle Transform(item["image"], zoom=0.5)
                hover Transform(item["image"], zoom=0.5)
                action SetScreenVariable("chosen", chosen + [item["id"]])

            hovered SetScreenVariable("hovered_item", item["id"])
            unhovered SetScreenVariable("hovered_item", None)

            focus_mask True
            xpos item["x"]
            ypos item["y"]
            xanchor 0
            yanchor 0

    if play_button:
        # text "play button clicked"
        if wrong: 
            text "try again!":
                xalign 0.5
                yalign 0.2
            timer 1.0 action SetScreenVariable("play_button", False)
            timer 1.0 action [SetScreenVariable("chosen", []), SetScreenVariable("hovered_item", None)]


        elif correct:
            text "yay you got it right"
            timer 5.0 action [Stop("instrument1"), Stop("instrument2"), Stop("instrument3")]
            timer 0.1 action [
                Play("instrument1", "audio/music_mechanic/Demo/Guitar.mp3"),
                Play("instrument2", "audio/music_mechanic/Demo/Vocals.mp3"),
                Play("instrument3", "audio/music_mechanic/Demo/Strings.mp3")
            ]
            timer 5.1 action Return(True)

        else:
            text "click everthing first"
            timer 1.0 action [SetScreenVariable("play_button", False)]


    else:
        text "not yet"
        