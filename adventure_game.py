# Gaming_time — A text-based adventure game!

# Infinite loop to let the player retry the game until they choose to quit
while True:
    # Welcome message and game intro
    print("\nWELCOME TO THE TRESSURE HUNT")
    print("WHERE YOUR MISSION IS TO FIND THE TRESSURE!")

    # Ask player if they're ready
    st = input("Type 'YES' when you're ready: ").upper()

    # If not ready, exit the loop this round
    if st != "YES":
        print("Come back whenever you're ready!")
    
    else:
        # Start of the actual adventure
        print("Your ship drowned in yesterday's tsunami, and now you're on an island.")

        # First choice: direction
        dir = input("You have 2 directions — where do you wanna go? 'left' or 'right'? ").upper()

        if dir == "LEFT":
            # Wrong path: captured by pirates
            print("You're arrested by pirates. GAME OVER!")

        elif dir == "RIGHT":
            # Correct path: move forward in the story
            print("Yes, right is always right.")
            print("You walked a mile and found a lake.")

            # Second choice: wait or swim
            boat = input("Will you 'wait' for a boat or 'swim' through it? ").upper()

            if boat == "SWIM":
                # Wrong decision: crocodiles eat the player
                print("You should've waited. The lake had crocodiles.")
                print("GAME OVER! (Death: Eaten by crocodiles)")

            elif boat == "WAIT":
                # Good decision: player advances
                print("Patience is good. You crossed the lake safely.")
                print("Now there are 3 doors. One hides the treasure.")

                # Bonus twist: Dragon appears!
                print("Unknowingly, you stepped on an ancient stone...")
                print("You heard a massive roar behind a mountain — a DRAGON is approaching!")

                # Dragon encounter choice
                diss = input("What are you gonna do? 'fight' or 'sneak' behind a rock? ").upper()

                if diss == "FIGHT":
                    # Brave but foolish — dragon wins
                    print("Bravo! You tried to fight the dragon but got toasted...")
                    print("GAME OVER!")
                elif diss == "SNEAK":
                    # Smart move: Dragon flies away
                    print("SMART MOVE! The dragon flew over and couldn't see you.")
                    print("Now you can access the 3 doors. One hides the treasure.")

                # Final decision: choose the right door
                door = input("Which door will you choose? 'RED', 'BLACK' or 'BLUE'? ").upper()

                if door == "RED" or door == "BLACK":
                    # Wrong door choice
                    print("Wrong choice.")
                    print("GAME OVER!")

                elif door == "BLUE":
                    # Entered the right door
                    print("Congratulations! You entered the blue room successfully!!!")
                    print("But inside, you see TWO chests...")
                    print("One is a SMALL, glowing chest.")
                    print("The other is a HUGE golden chest.")

                    # Final moral choice: Greed vs wisdom
                    greed = input("Which one do you choose? ('SMALL' or 'HUGE') ").upper()

                    if greed == "HUGE":
                        # Greedy choice = trap!
                        print("The moment you touched the huge chest, the floor opened beneath you...")
                        print("You fell into a chamber full of snakes! 🐍 (Punishment for being greedy)")
                        print("GAME OVER!")
                    elif greed == "SMALL":
                        # Wise choice: true treasure!
                        print("An angel appeared and said: 'You chose wisely!'")
                        print("Congratulations! You won the treasure! 🎉")

                    # ASCII treasure chest art for winners!
                    print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
                    print("YOU WON THE GAME! 🏆")

    # Ask player if they want to retry after game ends
    retry = input("\nDo you want to play again? (yes/no): ").lower()

    if retry != "yes":
        # Exit message and break loop if player says no
        print("Thanks for playing! See you next time, adventurer! 👋")
        break
