label scene2_start:

# scene 2.0 script starts here

    scene sidewalk with fade
    play music "suburban.mp3" fadein 1.0

    "The cold breeze brushed past his shoulders and face."
    "It was a much needed welcome from the approaching fall, signaling an end to the summer heat that Chase considered to be inescapable."
    "He walked alongside the road, on the concrete sidewalk."
    "He was in his childhood suburban neighborhood."

    c "{i}I haven't been here since I left for school. I have no family left here, so there never was a reason to come back.{/i}"

    "He walked on the sidewalk , effortlessly avoiding from stepping on the cracks." 
    "He could recall at which he would hop and skip over as a kid."

    scene timmy_house with fade

    "He soon arrived at a house with a massive oak tree in the front yard." 
    "A little swing built into the tree, slightly swayed."
    "The house was decorated much differently than how he recalled."
    "It was like seeing a close friend who decided to completely overhaul their style."
    "Ivys grew above the front door creating a botanical archway."
    "A new sidewalk made of chiseled stone ran from that same front door to the sidewalk where he was stood."
    "And, for no apparent reason, many small statues of cute cartoonish forest animals were tucked between all of the flower pots lining the walls of the house." 
    "He chuckled at the playful change of theme to the house that he once recalled as plain and barebones."
    "As he walked up to the house, the woman who called him yesterday opened the front door."
    "A very warm and motherly smile greeted him"

    show c happy at left
    show m at right
    
    m "Chase, I'm so glad you could make it"

    "Chase could barely note the tired look in her eyes."
    "Chase nodded his head down and greeted back with a smile, albeit slightly sheepish."
    c "Good afternoon, Mrs. mom how are you holding up?"

    "The smile remained, but the warmth on Mrs. (blanks) face faded." 
    "Her eyes peered off"
    m "Oh, we are all doing our best. Trying to make sense of what's happening."
    m "I appreciate the concern, but please don't worry too much about me." 
    m "Please come on in, I have some tea if you'd like"

    "Chase gave a thank you and entered the once familiar house." 
    "As he passed through the doorway, he noted how much shorter it had become."

# scene 2.1 script starts here  

    scene black with scene_interlude
    scene timmy_living_room with fade

    "Unlike the outside of the house, the inside was relatively kept intact as it were in his memories."
    "Chase had difficulty holding a conversation with Timothy's mother, since he kept gettin goverwhelmed by the sensations of nostalgia."
    "There was a brown grand piano that took center stage in the living room on a beige persian rug."
    "The fishtanks where still there next to the kitchen door, their glass still covered in green algae."
    "The brown wooden bookshelfs of various sizes and shapes lined up alongside the dining table."
    "The voice of Timothy's mother snapped him back to their conversation."

    show c neutral at left
    show m at right

    m "He had been calling and sending photos the past few years. However, he never did visit. He must had been busy with school just like you were."

    # need to add updated eyebrow raise image here, WIP

    "Chase's eyebrows began to knit in confusion."

    c "But Mrs. (blank), did you not say Timmy never did end up going to college?"

    "Timothy's mother, now realizing her mistake, was briefly dumbounded."

    m "Ah. yes, sorry."

    "she smiled apolegetically."

    m "It seems these past 4 years, we thought our Timmy was going to school with you." 
    m "It's just hard to see it otherwise when he had been calling us that whole time. Talking about all the things he'd been learning and doing at school."
    m "Maybe he was lying this whole time or-"

    "Timothy's mother began to drift off with a look of concern."
    "Chase asked."

    c "When did you guys find out he'd been gone this whole time?"

    "Timothy's mother fixated her look on something off in the distance."

    m "It was about two weeks ago when he stopped all contact with us."
    m "We were worried if something happened to him, so we contacted the college."
    m "That's when they told us he was never a student to begin with-"

    "Timothy's mother tried looking for what to say next, but was too occupied trying to answer the questions on her mind."
    "As they came across a door on the second floor, they both came to a stop."
    "Timothy's mother opened the door."
    m "This is his room. We've kept it untouched for the most part, since he's left."

    "Chase found it difficult to enter the room."
    "He felt hesitant, like he needed Timothy's permission before entering."
    "He shrugged it off and entered the room."

    scene timmy_bedroom with fade

    show c neutral at left
    show m at right


    "Chase commented,"

    c "It's been a while since I've been here. Last time was..."

    hide m

    "Chase stopped walking for a moment."

    "He squinted his eyes."

    c "Gee, I can't remember."

    "He did not realize Timothy's mother walking out of the room until she spoke to him from the doorway."

    m "I'll be back in a moment, but please take a look around."
    m "Feel free to check anything you'd like. I'm just hoping it'll give you an idea or clue as to what happened to my boy."
    m "The computer on the table still works, but I can't quite figure out the password."

    "Timothy's mother smiled a goodbye and walked off; leaving Chase in a room he would never have imagined himself back in."

    c "{i}What happened all those years ago?{/i}"

    "He noticed all of the specks of dust floating in the room. They passed through the rays of light that entered through the slits of the window curtains."

    c "I honestly don't even know where to start with this"

    $ clickedGuitar = 0;
    #yaya

label investRoom:
    window hide
    show screen room_main_interact
    pause
    jump investRoom

screen room_main_interact():
        modal True
        imagebutton:
                idle At("stuffed animal", shadow_soft)
                hover At("stuffed animal", shadow_hard)
                focus_mask True
                action Jump("stuffedAnimal"), renpy.hide_screen("room_main_interact")
        imagebutton:
                idle At("basketball", shadow_soft)
                hover At("basketball", shadow_hard)
                focus_mask True
                action Jump("basketball"), renpy.hide_screen("room_main_interact")
        imagebutton:
                idle At("guitar", outline_white_thick)
                hover At("guitar", outline_black_thick)
                focus_mask True
                action Jump("guitar"), renpy.hide_screen("room_main_interact")
        imagebutton:
                idle "hoop"
                #hover At("hoop", outline_black_thick)
                focus_mask True
                #action Jump("hoop"), Hide("room_main_interact")
        imagebutton:
                idle At("computer", outline_white_thick)
                hover At("computer", outline_black_thick)
                focus_mask True
                action Jump("computer"), Hide("room_main_interact")


label stuffedAnimal:
        c "{i}An old stuffed animal. It's once soft plush, now turned to a damp matte.{/i}"
        c "{i}I can't even read it's tag anymore.{/i}"
        c "{i}What is this even supposed to be?{/i}"
        jump investRoom

label basketball:
        #To do: easter egg basketball shot
        show screen hoop
        c "{i}Cool a basketball!{/i}"
        c "{i}I can't imagine Timmy playing outside. He was always here in his room practicing with his instruments.{/i}"
        hide screen hoop
        jump investRoom

screen hoop():
        imagebutton:
                idle At("hoop", outline_white_thick)
                hover At("hoop", outline_black_thick)
                focus_mask True
                action Jump("hoop"), renpy.hide_screen("room_main_interact")

label hoop:
        c "I think I have time for a swish."
        "Chase tossed the basketball across the room."
        "It was a fabulous miss!"
        "It made Chase wince in silence."
        c "I'm getting distracted. The ball was deflated anyways."
        jump investRoom

label guitar:
        if bool(clickedGuitar) is False:
                "Although the room with littered with all sorts of intruments. From a keyboard, to a small set of drums, and even a cello." 
                "There was one instrument that really caught Chase's eye."
                c "What happened to Tim."
                "He seemed to asking himself"
                c "Why didn't he go to music university?"
                c "He was so talented, he could pick up and play anything thrown at him. He put in so much time and effort too." 
                c "I mean, even the people I just played with at the concert hall could not have hold a candle to him."
                "It felt like the guitar was not acknlowledghing Chase. Looking past him."
                c "And this. Man, you could not separate the two."
                
                menu:
                        "Touch the guitar.":
                                $ clickedGuitar = 1;
                                "BAM!"
                                "Before Chase could even decide to play the guitar, it fell from its hook on the wall."
                                "The strings played out in a wail."
                                c "SHOOT!"
                                "Chase ran to the guitar; looking for any damage."
                                c "Huh. Seems to be alright. Just a dramatic fall."
                                "As he picked it up, he noticed a sticky note fell from the back of the guitar."
                                c "Wait. What is this?"
                                "On it was short and simple word. blank //make it something important"
                                c "I don't understand what this means. And why would he be hiding it? Must be for something important."
                                "After shaking off the questions in his head, he placed the sticky note back where he found it."
                                "He was able to hang the guitar back up on an empty hook."
                                c "Maybe I shouldn't mess with his things."

                        "Look elsewhere.":
                                jump investRoom

                jump investRoom
        if bool(clickedGuitar) is True:
                "Tim's guitar. I can't even believe it's here and not with him."
                "I shouldn't mess with it any futher."
                "Although I do recall the message behind it reading: blank"
                jump investRoom

label computer:
        "An old computer from the early 200s is tucked against the wall."
        "Chase moved some hats and shirts that were strewn on top of the monitor."
        c "{i}Something about this computer bothers me. I mean it's old and yellow.{/i}"
        "He sat down on a chair and scooted himself close to the computer."
        "He found the mouse and keyboard buried beneath a pile consisting of music sheets, a metronome, and many guitar picks."
        c "{i}Who knows, maybe it has info on Tim. Let's turn on this bad boy."

        play sound "computer startup.mp3"

        #add interface l8r

        "Like a zombie rising from the dead, the fans of the computer slowly came to life."
        "He could see the cobwebs and dust flying out from a side of the computer."
        "For a brief moment, the computer started up just fine."
        "Just fine until it startled Chase with distorted audio and a glitchy screen."
        c "Did this computer always do this?"
        "The computer then began to flicker a warped screen prompting him for a password."

        python:
                password = renpy.input("Enter password:")
                if password == "blank":
                        renpy.jump("computerAccept")
                else:
                        renpy.jump("computerReject")
label computerAccept:
        "YAY. You have made it into the computer"
        jump investRoom
label computerReject:
        c "Damn, seems I don't have an idea what it could be."
        c "Maybe I can find a clue somewhere in this room."
        jump investRoom


#jump endGame

