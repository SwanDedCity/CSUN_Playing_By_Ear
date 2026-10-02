label scene1_start:

# scene 1.0 script starts here

    scene stage_lights with fade
    play music "orchestra tuning.ogg"

    "The sound of an orchestra ensemble tuning together began to grow louder and louder. 
    A mix of both harmonious and dissonant notes merging into one another."
    "As if the orchestra was all one giant beast waking up."

    "Chase untucked his tuxedo jacket from the chair he sat on, and then adjusted his seating position."
    "He straightened his back, tilted his head forward, and took a deep breath."
    "He paused for a moment, relaxing the twitch in his bowhand before picking up the violin."

    c "{i}I could not believe I could have it all.{/i}"

    "He looked all around him. The musical pantheon was filled with disciplined and prestigious musicians."

    c "{i}These talented and skilled individuals sat all around me, by no mere coincidence.{/i}"

    c "{i}We have been brought here by ruthless practice and an unwavering passion to perfect our art.{/i}"

    scene stage_main with fade 

    "He looked out to the sea of seats laid out in rows before the stage."

    c "{i}They were empty now, but by next week they will be filled with an eager audience dying to hear our performance.{/i}"

    c "{i}Just one more session, and I'll be finalized as an official member of this ensemble.{/i}"
    c "{i}You're almost there, Chase.{/i}"

    stop music fadeout 3.0

    "The roar of the giant beast came to an end. Everyone held their instruments ready, watching the conductor raise their baton." 
    "And with a deep breath out, he put into sound all the fervent passion and dedication trapped within him."

    scene black with scene_interlude

# scene 1.1 script starts here
    scene restroom with fade
    play music "bathroom.mp3"

    "In the stillness of the concert hall's restroom, only the soft hum the air condition could be heard now that the performance was over."
    "It was, until that stilness was broken by the loud bang of the door flying open."
    "Chase tensely walked up to a pristinely clean faucet in the middle." 

    play sound "sink.mp3"

    "He began to wash his face, a lack of care for the mess he was making on his jacket."

    scene image_chase_bathroom with fade

    c "That was brutal."

    "He sharply inhaled as he massaged his left hand under the cold running water."
    "He continued to scoff under a low volume"

    c "No passion? Tasteless performance? I've been doing this all my life. Who do they take me for?"

    "He turned off the faucet, and then buried his face in a towel that he picked up from his side."

    c "They don't see my plight. They don't get what I've gone through for this!"

    c "They simply can't recognize talent when it's in the room. Ha! That must be it."

    "That quick laugh vanished just as soon as it arrived. Making way to despair."
    "His head rushing with a million thoughts."

    c "What am I gonna do now?"

    "Silence, as no one had an answer, not even him."

    c "No, this isn't happening. I'm sure I can discuss with the director to reconsider; or to give me, at the very least, another audition."

    "He did not notice his heart beating thunderously loud in his chest."
    "His shoulders sagged in defeat."

    c "I don't even want this. I wasn't even able to play the way I want to."

    "He sighed as he listened to himself."

    c "Maybe they are right. Maybe my passion really is gone."

    "He stared at his own reflection in the mirror, beads of water dripping from his face. He searched that man's face for an answer."

    c "What was I doing all of this for?"

    scene restroom with fade

    show c grumpy formal at left

    play ringtone "phone ringing.mp3" volume 6
    "{b}RING RING RING{/b}"

    "He was interrupted by his phone's ringtone. It was an unknown number that had been calling him for the past week."

    c "{i}This again?{/i}"
    c "{i}They're persistent, I should block them at this point. {/i}"
    "Chase hovered his thumb over the red button to decline the call. He hesitated."
    c "{i}Well, now that my chances with the ensemble are in the gutter, I guess I have nothing but free time.{/i}"

    stop ringtone
    "Chase answered."

    c "Hey, why do you guys keep calling me?"

    "The voice of a woman answered with relief."

    w "Chase? Is that really you, Chase?"

    show c neutral formal at left
    
    "Chase was taken aback for a moment."
    "Her voice sounded familiar to him."
    "He briefly tried to recall if the voice belonged to an agent or a director he's previously worked with."

    c "Yes, yes, this is Chase."

    "Now holding the phone with both hands."

    c "I'm sorry but I can't recall who this is."

    "The woman sighs loudly."

    w "Ah, I'm glad to hear. No, I'm sorry. It's no surprise you don't recognize me. We haven't met since you and Timmy left."

    stop music fadeout 2.0
    stop sound

    show c surprised formal at left

    "{i}Timmy{/i}"

    "As if saying that name cast a spell; the soft lights in the bathroom, the soft hum of the AC, everything vanished." 
    "He felt transported to an empty vacuum in space."

    c "Timothy."

    "A name he hadn't heard in years."
    "A name belonging to someone who was once so important and dear to him."
    "Now resurfacing to his mind, as if it had been stuck at the bottom of a seabed for years."
    "From this vacuum of nothing he was cast to, he could faintly hear the woman continue to talk."

    show c neutral formal at left

    w "I apologize if you are busy, but please listen." 
    w "My dear Timmy is gone." 
    w "We don't know what really happen to him, but he's been gone for the past few years.-"

    c "{i}Maybe that's who I did this all for.{/i}"

    "The woman continued"
    w "You were the last person close to him."

    c "{i}Yes, it's coming back to me. I haven't thought about it since we parted ways.{/i}"

    w "Please if you could come by our house sometime this weekend."
    w "We have some things we'd like you to look at, to see if it'll give you an idea of where he could have gone."

    c "{i}But it's true.{/i}"
    c "{i}I'm only here{/i}"
    c "{i}because of him.{/i}"


# end of scene 1

    scene black with scene_interlude
    jump scene2_start

