label scene1_start:

# define characters

    define c = Character("Chase")

# scene 1 script starts here

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

    jump endGame
