
style mm_gui_text:
    color "#0099cc"#gui.cs.accent_color
    hover_color "#000000"
    font "gui/custom_gui/Calgary_DEMO.ttf"
    size 50

#transforms for custom main menu screens
transform title:
    xalign 0.5
    yalign 0.5

transform title_to_start:
    xalign 0.5
    yalign 0.5
    linear 1.0 xalign 0.5 yalign 0.0

transform title_to_load:
    xalign 0.5
    yalign 0.5
    linear 1.0 xalign 0.0 yalign 0.5
transform load_to_title:
    xalign 0.0
    yalign 0.5
    linear 1.0 xalign 0.5 yalign 0.5

transform title_to_settings:
    xalign 0.5
    yalign 0.5
    linear 1.0 xalign 1.0 yalign 0.5
transform settings_to_title:
    xalign 1.0
    yalign 0.5
    linear 1.0 xalign 0.5 yalign 0.5

transform title_to_quit:
    xalign 0.5
    yalign 0.5
    linear 1.0 xalign 0.5 yalign 1.0
transform quit_to_title:
    xalign 0.5
    yalign 1.0
    linear 1.0 xalign 0.5 yalign 0.5

#button that is always centered on screen. takes in y position, text to display, and action to perform when clicked
screen main_menu_button(xposs= 0.423, yposs=0, text="Start", actionChoice=NullAction()):
    # fixed:
    #     button:
    #         background "gui/custom_gui/mm_idle.png"
    #         hover_background "gui/custom_gui/mm_hover.png"
    #         xpos xposs
    #         ypos yposs
    #         focus_mask True
    #         action [actionChoice, Hide()]#actionChoice
    #         text [text]:
    #             xalign 1.0
    #             yalign 1.0
    #             style "mm_gui_text"
    fixed:
        xpos xposs
        ypos yposs
        xysize (325, 70)
        imagebutton auto "gui/custom_gui/menu_%s.png":
            focus_mask True
            action [actionChoice, Hide()]
        
        text "[text]":
            # xpos 0.45 
            xalign 0.5
            ypos 0.0
            style "mm_gui_text"
            # action actionChoice
 
screen custom_main_menu_navigation():
    
    fixed:
        use main_menu_button(0.423, 0.324, "New Game", Show("custom_main_menu_start"))
        use main_menu_button(0.423, 0.425, "Load Game", Show("custom_main_menu_load"))
        use main_menu_button(0.423, 0.509, "Settings", Show("custom_main_menu_settings"))
        use main_menu_button(0.423, 0.609, "Quit", Show("custom_main_menu_quit"))
screen custom_main_menu(transform=title):
    add "gui/custom_gui/c_main_menu.png":
        at transform
    add "gui/custom_gui/mm_ui.png" xalign 0.5 yalign 0.5
    use custom_main_menu_navigation

screen custom_main_menu_start():
    add "gui/custom_gui/c_main_menu.png":
        at title_to_start
    timer 3.0 action Start()

screen custom_load():
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on a button.
        button:
            style "page_label"

            key_events True
            xalign 0.5
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileLoad(slot)#FileAction(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        vbox:
            style_prefix "page"

            xalign 0.5
            yalign 1.0

            hbox:
                xalign 0.5

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()
                key "save_page_prev" action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()
                key "save_page_next" action FilePageNext()

            if config.has_sync:
                if CurrentScreenName() == "save":
                    textbutton _("Upload Sync"):
                        action UploadSync()
                        xalign 0.5
                else:
                    textbutton _("Download Sync"):
                        action DownloadSync()
                        xalign 0.5
screen custom_main_menu_load():
    add "gui/custom_gui/c_main_menu.png":
        at title_to_load
    use main_menu_button(0.423, 0.1, "Back", Show("custom_main_menu", transform=load_to_title)) 
    use custom_load

screen custom_settings(pos):

    drag:
        pos pos

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
screen custom_main_menu_settings():
    add "gui/custom_gui/c_main_menu.png":
        at title_to_settings
    use main_menu_button(0.423, 0, "Back", Show("custom_main_menu", transform=settings_to_title))

    frame:
        use custom_settings((500, 500))

screen custom_main_menu_quit():
    add "gui/custom_gui/c_main_menu.png":
        at title_to_quit
    use main_menu_button(0.423, 0.324, "Back", Show("custom_main_menu", transform=quit_to_title))     
    use main_menu_button(0.423, 0.425, "Quit", Quit(confirm=not main_menu))  



#needs work. too much repition

screen custom_game_menu_navigation():
    fixed:
        use main_menu_button(0.03, 0.242, "History", Show("custom_game_menu_history"))
        use main_menu_button(0.03, 0.324, "Save Game", Show("custom_game_menu_save"))
        use main_menu_button(0.03, 0.425, "Load Game", Show("custom_game_menu_load"))
        use main_menu_button(0.03, 0.509, "Settings", Show("custom_game_menu_settings"))
        use main_menu_button(0.03, 0.609, "Title", MainMenu())
        use main_menu_button(0.03, 0.693, "Close", Return())
screen custom_game_menu():
    add "gui/custom_gui/c_game_menu_tint.png"
    add "gui/custom_gui/c_game_menu.png"

    use custom_game_menu_navigation

screen custom_history():
    hbox:
        frame:
            style "game_menu_navigation_frame"
        frame:
            style "game_menu_content_frame"
            viewport:
                yinitial 1.0
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                vbox:
                    spacing gui.history_spacing

                    for h in _history_list:

                        window:

                            ## This lays things out properly if history_height is None.
                            has fixed:
                                yfit True

                            if h.who:

                                label h.who:
                                    style "history_name"
                                    substitute False

                                    ## Take the color of the who text from the Character, if
                                    ## set.
                                    if "color" in h.who_args:
                                        text_color h.who_args["color"]

                            $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                            text what:
                                substitute False

                    if not _history_list:
                        label _("The dialogue history is empty.")
screen custom_game_menu_history():

    add "gui/custom_gui/c_game_menu_tint.png"
    add "gui/custom_gui/c_game_menu.png"
    use custom_history
    fixed:
        use main_menu_button(0.03, 0.324, "Save Game", Show("custom_game_menu_save"))
        use main_menu_button(0.03, 0.425, "Load Game", Show("custom_game_menu_load"))
        use main_menu_button(0.03, 0.509, "Settings", Show("custom_game_menu_settings"))
        use main_menu_button(0.03, 0.609, "Title", MainMenu())
        use main_menu_button(0.03, 0.693, "Close", Return())

screen custom_save():
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on a button.
        button:
            style "page_label"

            key_events True
            xalign 0.5
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileSave(slot)#FileAction(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        vbox:
            style_prefix "page"

            xalign 0.5
            yalign 1.0

            hbox:
                xalign 0.5

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()
                key "save_page_prev" action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()
                key "save_page_next" action FilePageNext()

            if config.has_sync:
                if CurrentScreenName() == "save":
                    textbutton _("Upload Sync"):
                        action UploadSync()
                        xalign 0.5
                else:
                    textbutton _("Download Sync"):
                        action DownloadSync()
                        xalign 0.5
screen custom_game_menu_save():
    add "gui/custom_gui/c_game_menu_tint.png"
    add "gui/custom_gui/c_game_menu.png"
    use custom_save
    fixed:
        use main_menu_button(0.03, 0.242, "History", Show("custom_game_menu_history"))
        use main_menu_button(0.03, 0.425, "Load Game", Show("custom_game_menu_load"))
        use main_menu_button(0.03, 0.509, "Settings", Show("custom_game_menu_settings"))
        use main_menu_button(0.03, 0.609, "Title", MainMenu())
        use main_menu_button(0.03, 0.693, "Close", Return())

screen custom_game_menu_load():
    add "gui/custom_gui/c_game_menu_tint.png"
    add "gui/custom_gui/c_game_menu.png"
    use custom_load
    fixed:
        use main_menu_button(0.03, 0.242, "History", Show("custom_game_menu_history"))
        use main_menu_button(0.03, 0.324, "Save Game", Show("custom_game_menu_save"))
        use main_menu_button(0.03, 0.509, "Settings", Show("custom_game_menu_settings"))
        use main_menu_button(0.03, 0.609, "Title", MainMenu())
        use main_menu_button(0.03, 0.693, "Close", Return())

screen custom_game_menu_settings():
    add "gui/custom_gui/c_game_menu_box.png"
    add "gui/custom_gui/c_game_menu_tint.png"
    add "gui/custom_gui/c_game_menu.png"
    use custom_settings((600, 200))
    fixed:
        use main_menu_button(0.03, 0.242, "History", Show("custom_game_menu_history"))
        use main_menu_button(0.03, 0.324, "Save Game", Show("custom_game_menu_save"))
        use main_menu_button(0.03, 0.425, "Load Game", Show("custom_game_menu_load"))
        use main_menu_button(0.03, 0.609, "Title", MainMenu())
        use main_menu_button(0.03, 0.693, "Close", Return())    















screen custom_game_menu_interface(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    # use navigation
    # use custom_navigation

    textbutton _("Return"):
        style "return_button"

        #action Return()
        action [ShowMenu("custom_game_menu"), Hide()]
    # frame:
    #     textbutton _("Return") action [ShowMenu("custom_game_menu"), Hide()]
    #     style "return_button"
        


    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

screen custom_about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use custom_game_menu_interface(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with bwababa {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
