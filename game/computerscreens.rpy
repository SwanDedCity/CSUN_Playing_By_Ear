default player_input = ""
screen computer_password():
    fixed:
        add "gui/custom_gui/computer/computer_password.png"
        vbox:
            text "Enter password:"
            input:
                value VariableInputValue("player_input")
                action Return(player_input)
            align (0.5, 0.5)
            
screen computer_home():
    modal True
    fixed:
        add "gui/custom_gui/computer/computer_apps.png"
        imagebutton auto "gui/custom_gui/computer/photos_%s.png":
            focus_mask True
            action Jump("computerReject")
        imagebutton auto "gui/custom_gui/computer/music_%s.png":
            focus_mask True
            action [Show("computer_music"), Hide()]
        imagebutton auto "gui/custom_gui/computer/trash_%s.png":
            focus_mask True
            action Jump("computerReject")



screen computer_music():
    default song_choice = "Select A Song"
    default song_selected = False

    imagebutton auto "gui/custom_gui/computer/music_%s.png":
        focus_mask True
        action SetScreenVariable("song_choice", "Song 1")
        xpos -500
        ypos -800
    fixed:
        text [song_choice]:
            xalign 0.5
            yalign 0.6
        imagebutton auto "gui/music_mechanic/play_%s.png":
            focus_mask True
            xpos 700
            # action SetScreenVariable("play_clicked", True)
            action If(
                song_choice == "Song 1",
                Play("sound", "audio/Just You And Me 4.mp3"),
                Play("sound", "audio/error_sound.mp3")
            )
            