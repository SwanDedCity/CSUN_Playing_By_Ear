label scene1_start:

# define characters

    define c = Character("Chase")
    define w = Character("???")
    define scene_interlude = Fade(2.0, 0.5, 0.0)

# scene 1.0 script starts here

    scene stage_lights with fade
    play music "orchestra tuning.ogg"

    "The ensemble of instruments tuning started to grow all louder. 
    A mix of both harmonious and dissonant notes merging into one another. 
    As if the orchestra was all one giant beast waking up."

    "Chase untucked the jacket of his tuxedo from the seat, and adjusted his position."
    "He straightened his back, tilted his head forward, and took a deep breath. 
    He paused for a moment, relaxing the twitch in his bowhand before picking up the violin."

    c "{i}I could not believe I could have it all{/i}"

    "He looked all around. The musical pantheon of discipline and prestige."

    c "{i}Talents sat all around me, by no mere coincidence.{/i}"

    c "{i}We have been brought here by ruthless practice and an unwavering passion to perfect our art.{/i}"

    scene stage_main with fade 

    "He looked out to the sea of seats laid out in rows before the stage."

    c "{i}They were empty now, but by next week they will be filled with an eager audience dying to hear our performance.{/i}"

    stop music fadeout 1.0

    "The roar of the giant beast came to an end, and he joined the rest of the orchestra in silence, waiting for the conductor to begin the performance. 
    And with a deep breath out, he put into sound all of the fervent passion and dedication trapped within him."

    scene black with scene_interlude

# scene 1.1 script starts here
    scene restroom with fade
    play music "bathroom.mp3"

    "The stillness of the concert hall's restroom was broken by the loud bang of the door flying open."
    "Chase came to a pristinely clean faucet in the middle." 

    play sound "sink.mp3"

    "He began to wash his face, a lack of care for the mess he was making on his jacket."

    c "That was brutal."

    "He sharply inhaled as he massaged his left hand under the cold running water."
    "He continued to scoff under a low volume"

    c "No passion? Tasteless performance? I've been doing this all my life. Who do they take me for?"

    "He turned off the faucet, and then buried his face in a towel that he picked up from the side."

    c "They don't see my plight. They don't get what I've gone through for this!"
    c "They simply can't recognize talent when it's in the room. Ha! That must be it"

    "That quick laugh vanished just as soon as it arrived. Making way to despair."
    "His head rushing with a million thoughts."

    c "What am I gonna do now?"

    "Silence, as no one had an answer, not even him."

    c "No, this isn't happening. I'm sure I can discuss with the director to reconsider or for, at the very least, another audition."

    "He did not notice his heart beating thunderously loud in his head."
    "His shoulders sagged in defeat."

    c "I don't even want this. I won't be able to play the way I want here."
    c "Maybe they are right. Maybe my passion really is gone"

    "He stared at his own reflection in the mirror, beads of water dripping from his face. He searched that man's face for an answer."

    c "What was I doing all of this for?"

    "{b}RING RING RING{/b}"

    "He was interrupted by his phone's ringtone. It was an unknown number that had been calling him for the past week."

    c "{i}They're persistent, I should block them at this point. {/i}"
    c "{i}...{/i}"
    c "{i}Now that my chances with the rehearsal are in the gutter, I might as well.{/i}"

    "Chase answered."

    c "Hey, why do you guys keep calling me?"

    "The voice of a woman answers relief"

    w "Chase? Is that really you Chase?"

    "Chase gets taken aback for a moment."
    "Her voice sounded familiar to him."
    "He briefly tries to recall if the voice belonged to an agent or director he's previously worked with."

    c "Yes, yes, this is Chase"

    "now holding the phone with both hands"

    c "I'm sorry but I can't recall who this is."

    "The woman sighs loudly"

    w "Ah, I'm glad to hear. No, I'm sorry. It's no surprise you don't recognize me since we haven't met since you and Timmy left."

    stop music
    stop sound

    "{i}Timmy{/i}"

    "As if saying that name was a spell; the soft lights in the bathroom, the soft hum of the ac, everything vanished." 
    "He felt transported to an empty vacuum in space."

    c "Timothy."

    "A name he hadn't heard in years."
    "A name belonging to someone who was once so important and dear to him."
    "Now resurfacing to his mind, as if it had been stuck at the bottom of a seabed for centuries."
    "From this vacuum of nothing he was cast to, he could faintly hear the woman continue to talk."

    w "I apologize if you are busy, but please listen." 
    w "My dear Timmy is gone." 
    w "We don't know was really happen to him, but he's been gone for the past few years.-"

    c "{i}Maybe that's who I did this all for.{/i}"

    "The woman continued"
    w "You were the last person close to him."

    c "{i}Yes, It's coming back to me. I haven't thought about it since we parted way.{/i}"

    w "Please if you could come by our house sometimes this weekend."
    w "We have some things we'd like you to look at, to see if it'll give you an idea of where he could have gone"

    c "{i}But it's true.{/i}"
    c "{i}I'm only here{/i}"
    c "{i}because of him{/i}"


# end of scene 1

    scene black with scene_interlude
    jump scene2_start

