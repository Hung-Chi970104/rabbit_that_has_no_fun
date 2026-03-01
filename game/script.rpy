# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define b = Character("bunny")
image b idle = "bunny.png"

define m = Character("mole")
image m idle = "mole.png"

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

    n "In a quiet meadow lived a bunny who loved to hop and play in the sun."

    n "Beneath that same meadow lived a mole who preferred the darkness of his tunnels."

    n "One day, Bunny noticed small mounds of dirt everywhere and went to investigate."

    n "Just then, out popped a tiny mole, covered in dirt and looking very confused."

    n "The two unlikely friends would soon discover they had more in common than they thought."
    
    show b idle

    b "Who is doing this to my beautiful meadow?"

    b "These holes are everywhere! I could twist my ankle!"

    b "Wait... you're actually a mole? I've never seen one before!"

    b "I'm sorry for being so harsh. Would you like to be my friend?"

    b "Come on, let me show you how wonderful the surface world can be!"

    show m idle

    m "I'm so sorry! I was just digging tunnels looking for food and worms."

    m "I didn't know anyone lived up here. I've never been above ground before."

    m "The darkness underground is all I've ever known. It feels safe down there."

    m "Really? You want to spend time with me even though I made those holes?"

    m "I'd love that! Maybe you could teach me about the sun and the grass!"

    # This ends the game.

    return
