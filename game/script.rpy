# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define b = Character("kx2bunny")
image b idle = "mole1.png"

define m = Character("mk47mole")
image m idle = "mole2.png"

define n = Character("narator")
image n idle = "placeholder"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show n idle

    # These display lines of dialogue.

    n "In a downtown toronto"

    n "kx2bunny was walkinh down queen st"

    n "kx2bunny sees mk47mole"

    n "they re from opposing gangs"

    n "The two unlikely friends would soon discover they had more in common than they thought."
    
    show b idle

    b "yo fam, nize your gerp"
    
    n "nunny says on the phone while walking alone the street"

    b "These pot holes are everywhere! I could twist my ankle!"

    n "The bunny sees the mole emerge from the ground. she thinks he caused the holes... What should she do?"

    menu:
        "Try to talk to him calmly":
            jump friendly_choice
        "Attack him in anger":
            jump angry_choice

    label friendly_choice:
        b "gerbert please stop making holes!"

        b "i might twist my ankle!"

        show m idle

        m "no fam, watch ur gaze or my holes will slime you"

        m "ur the real gerbert is you dont know that my holes take out whole gangs"

        b "yo watch your mouth or youll get sprayed"

        m "mk47mole runs these street cro, go anf call your uber"

        n "And so began a beautiful friendship between the bunny and the mole."

        jump ending

    label angry_choice:
        b "YOU! WATCH YOURSELF MANS"

        n "The bunny pulls out his blicky"

        b "Get out of my street right now!"

        show m idle

        m "nah, your a yute to these roads"

        b "im not a yute, you dess man"

        m "DESS MAN?? yo run up im cheesed"

        b "Wait... I... I'm sorry. That was too harsh. You didn't deserve that."

        b "wallahi i dont give a shite"

        n "mk47mole scares kx2bunny away, and peace is restored to toronto"

        jump ending

    label ending:
        n "Whether through kindness or redemption, the bunny and mole became true friends."

        n "They learned that understanding and forgiveness are the greatest gifts."

    # This ends the game.

    return
