'''This is code written by a 6th grader.  This student has had 4 weeks of coding. The assignment was to use:
loops, conditionals, input, f-strings and good variable names.  There was no code limit.'''

while True:
    title = "Life Simulator".center(50, "-")
    print(title)

    print("Welcome to life simulator.")
    print("A game that simulates life!")
    input("Press enter to continue.")
    while True:
        play_conf = input("Would you like a tutorial? (y or n to continue)").lower()
        if play_conf == "y":
            input("Press enter to begin the short tutorial.")
            input("Press 'y' or 'n' for 'yes' or 'no'.")
            input("Make the correct choices!")
            print("Tutorial done! Have fun playing.")
            input("And remember, make the right choices...")
            break

        elif play_conf == "n":
            break

        else:
            print("sorry. I didn't get that, please type y or n.")

    input("Ok! Welcome to Life Simulator. Press enter to start.")
    print("Before we officially begin, we would like for you to answer questions.")
    print("Who's life would you like to simulate?")
    name = input("Please enter a name.")
    print("Nice name! And a few more questions.")
    while True:
        pronoun = input(f"what gender is {name}? Please pick m, f, or x.")
        if pronoun == "m":
            pronoun_is = "he is"
            pronoun_was = "he was"
            pronoun_poss = "his"
            pronoun_gen = "male"
            pronoun_1 = "he"
            pronoun_2 = "him"
            break
        elif pronoun == "f":
            pronoun_is = "she is"
            pronoun_was = "she was"
            pronoun_poss = "her"
            pronoun_gen = "female"
            pronoun_1 = "she"
            pronoun_2 = "her"
            break
        elif pronoun == "x":
            pronoun_is = "they are"
            pronoun_was = "they were"
            pronoun_poss = "their"
            pronoun_gen = "genderqueer"
            pronoun_1 = "them"
            pronoun_2 = "they"
            break
        else:
            print("Sorry. I didn't get that. Please type m, f, or x.")
    print("Thank you for answering! And lastly...")
    location = input(f"Where is {name} located? Please enter a city in the US.")
    print("I would love to live there!")
    input(f"now loading you into {location}...")
    print("Great! We're here.")
    print("Since you know how to play, i'll leave you alone now.")
    divider = "-".center(50, "-")
    print(divider)
    print(f"{name}'s life")
    print("   ")
    print(f"{name} was born in {location} on july 14, 1992.")
    print(f"{pronoun_was} born into a nice family with 1 dad, 1 mom, and a brother.")
    input("First choice ahead!")
    input(f"-While {name}'s brother was feeding {name},")
    input(f" he picked up peas with the pink fork he was feeding {name}")
    input(f" The green balls looked disgusting to {name}.")
    print(" What do you do?")
    while True:
        choice_food1 = input(
            "(a) eat them anyways, (b) refuse to eat, or (c) flip the tray."
        )
        if choice_food1 == "a":
            while True:

                agup1a = input("Would you like to age up? y or n")
                if agup1a == "y":
                    print(f"Great! {name} is now 2 years old.")
                    break
                elif agup1a == "n":
                    print(f"Oopsies! Seems there was a glitch. {name} aged up anyways.")
                    print(f"Congradulations! {name} is now 2 years old.")
                    break
                else:
                    print("Sorry. Didn't get that. please type 'y' or 'n'.")
            break
        elif choice_food1 == "b":
            print(f"{name}'s brother shoved it into {pronoun_poss} moulth anyways.")
            while True:

                agup1b = input("Would you like to age up? (y or n)")
                if agup1b == "y":
                    print(f"Great! {name} is now 2 years old.")
                    break
                elif agup1b == "n":
                    print(f"Oopsies! Seems there was a glitch. {name} aged up anyways.")
                    print(f"Congradulations! {name} is now 2 years old.")
                    break
                else:
                    print("Sorry. Didn't get that. please type 'y' or 'n'.")
            break
        elif choice_food1 == "c":
            print("Oopsie! Seems there was a glitch in the system.")
            print("The system thinks you picked b, and I cant seem to change it.")
            input(f"Well, to make up for it, i'll age up {name}.")
            print("Let's see what would happen if you picked b.")
            print("NOW LOADING CHOICE_FOOD1B/C.py")
            input("RUNNING...")
            print(f"{name}'s brother shoved it into {pronoun_poss} moulth anyways.")
            while True:

                agup1c = input("Would you like to age up? (y or n)")
                if agup1c == "y":
                    print(f"Great! {name} is now 2 years old.")
                    break
                elif agup1c == "n":
                    print(f"Oopsies! Theres another glitch! {name} aged up anyways.")
                    print(f"Congradulations! {name} is now 2 years old.")
                    break
                else:
                    print("Sorry. Didn't get that. please type 'y' or 'n'.")
            break
        else:
            print("Sorry, Didn't get that. Please try again and type a, b, or c.")
    print(f"Congrats! {name} aged up. Ready for a new choice?")
    input("For your next choice, you get to choose wether you want it or not")
    while True:
        gamb_1 = input("Would you like to take a chance?")
        if gamb_1 == "y":
            print(f"{name} ate a crysanthemum.")

            while True:
                gamb_2 = input("would you like to take another chance?")
                if gamb_2 == "y":
                    input(f"{name} found a cuboard.")

                    while True:
                        cupbo2 = input(f"Should {name} open it?")
                        if cupbo2 == "y":
                            print("Sorry. Didn't get that.")
                            input("Oh, seems theres been another glitch!")
                            input("Sorry.")
                            print("Let me load that again...")
                            ("RUN CHOICE_FOOD1B/C.py")
                            print(">>>RUNNING")
                            cupbo2_dec = input(f"Should {name} open it?")
                            if cupbo2_dec == "y":
                                input("Ok.")
                                print(f"{name} opened the cupboard and found bleach.")
                                print("STOPRUN CHOICE_FOOD1B/C.py")
                                print("Yikes! If that kept on, it would've happened!")
                                break
                            elif cupbo2_dec == "n":
                                input("There seems to be another glitch!")
                                input("I'm sorry, but i'll make it up to you")
                                input(f"I'll age {name} up to make up or it.")
                                print("but we need to see")
                                print("what would happen if you picked yes.")
                                print("NOW LOADING CHOICE_FOOD1B/C.py")
                                input("RUNNING...")
                                print(f"{name} opened the cupboard and found bleach.")
                                print("STOPRUN CHOICE_FOOD1B/C.py")
                                print("Yikes! If that kept on, it would've happened.")
                                break

                            else:
                                print("sorry, I didn't get that. Type 'y' or 'n'")
                        elif cupbo2 == "n":
                            print("THANKSYO U")
                            print("Huh? that wasn't me. Must be another glitch.")
                            input("Gamble is over. No more chances are to be taken.")
                            break

                        else:
                            print("sorry, I didn't get that. Please type 'y' or 'n'.")
                elif gamb_2 == "n":
                    print("Ok, I guess its better to play it safe")
                    input("especially when theres another life on the line")
                    input(f"And it's not like {name} is real anyways!")
                    break

                else:
                    print("sorry, I didn't get that. Please type 'y' or 'n'.")

            break

        elif gamb_1 == "n":
            print("Ok, I guess its better to play it safe")
            input("especially when theres another life on the line")
            input(f"And it's not like {name} is real anyways!!")
            break

        else:
            print("sorry, I didn't get that. Please type 'y' or 'n'.")
    print(f"Alright. {name} aged up! {pronoun_1} is now 5 years old")
    input("Oh no! Theres been another glitch! Sorry.")
    print(f"I'm sorry to say, but {name} has been aged up to 18 years old.")
    print("And I can't seem to fix it!")
    input(f"Since I can't fix it, and {name} is already aged up to 18...")
    print(f"What college would you like {name} to attend?")
    while True:
        colle_nam1 = input("Harvard (h) or Yale (y)?")
        if colle_nam1 == "h":
            input(f"{name} didn't get accepted to Harvard.")
            break
            while True:
                colle_fr1 = print("Would you like to try another college?")
                if colle_fr1 == "y":
                    colle_nam2 = input("Yale (y)?")
                    input("It seems theres another glitch! I'm very sorry.")
                    print(f"{name} is now unemployed.")
                    break
                elif colle_fr1 == "n":
                    print(f"Okay, {name} is now unemployed.")
                    break
                else:
                    print("I didn't understand that. Please type 'y' or 'n'.")
                break
        elif colle_nam1 == "y":
            input(f"{name} didn't get accepted to Yale.")
            break
            while True:
                colle_fr1 = print("Would you like to try another college?")
                if colle_fr1 == "y":
                    colle_nam2 = input("Harvard (h)?")
                    input("It seems theres another glitch! I'm very sorry.")
                    print(f"{name} is now unemployed.")
                    break
                elif colle_fr1 == "n":
                    print(f"Okay, {name} is now unemployed.")
                    break
                else:
                    print("I didn't understand that. Please type 'y' or 'n'.")

        else:
            print("Sorry. I didn't get that.")
            input("Please type 'h' or 'y'.")
        break
    while True:
        print(f"{name} is unemployed, would you like to give {pronoun_2} a career?")
        print(f"What would you like {pronoun_2} to be?")
        while True:
            job_mcdo = input("Doctor (d), lawyer (l), or McDonalds Worker (m)?")
            if job_mcdo == "d":
                print(f"They didn't want {name} working as a doctor,")
                print(f"because {pronoun_1} didn't go to college.")
                input(f"{name}'s last resort was working at a McDonald's drive thru.")
                print(f"{name} is now succesfully employed!")
                break
            elif job_mcdo == "l":
                print("Oh no! It seems there has been another glitch!")
                input("The option to choose lawyer is unavailable :(")
                print("I'll reboot so you can take the doctor route instead.")
                print("NOW LOADING MCDO_JOBS/C.py")
                input("RUNNING...")
                print("Now running doctor route!")
                print(f"They didn't want {name} working as a doctor,")
                print(f"because {pronoun_1} didn't go to college.")
                input(f"{name}'s last resort was working at a McDonald's drive thru.")
                print(f"{name} is now succesfully employed!")
                break
            elif job_mcdo == "m":
                print(f"{name} is now employed and working at McDonalds.")
                input("Though, you could've chosen a higher paying job...")
                break
            else:
                print("Sorry. I didn't get that. Please choose d, l, or m.")
        break

    print("Another choice coming up!")
    while True:
        love_gen = input(f"What gender would you like {name}'s S/O to be?")
        if love_gen == "m":
            name_lo = 'Marco'
            lo_is = "he is"
            lo_was = "he was"
            lo_poss = "his"
            lo_gen = "male"
            lo_1 = "he"
            lo_2 = "him"
            break
        elif love_gen == "f":
            name_lo = 'Amy'
            lo_is = "she is"
            lo_was = "she was"
            lo_poss = "her"
            lo_gen = "female"
            lo_1 = "she"
            lo_2 = "her"
            break
        elif love_gen == "x":
            name_lo = 'Logan'
            lo_is = "they are"
            lo_was = "they were"
            lo_poss = "their"
            lo_gen = "genderqueer"
            lo_1 = "them"
            lo_2 = "they"
            break
        else:
            print("Sorry. I didn't get that. Please type m, f, or x.")

    input("Oh no! It appears there has been another glitch...")
    print(f"{name} has been aged up to 22!")
    print("I am so sorry for the inconvenience!")
    input(f"It is currently {name} and {name_lo}'s wedding.")
    print(f"You missed, but {name} was seeing someone. {lo_poss} name is {name_lo}")
    input("Oh no....")
    input("it appears that the couple didn't get their dog vaccinated and...")
    print(f"While their dog was passing flowers, it want insane and bit {name}.")
    print("I'm sorry, game over.")

    print(title)
    input("Thank you so much for playing!")
    input("I hope you enjoyed this little code~")
    print("But the game is over now...")
    input(f"Good job on {name}'s life. Would you like to start again with someone new?")
    while True:
        y_n_last = input("press y or n for the last time.")
        if y_n_last == 'n':
            print("Play again anyways~")
            print("Haha! Thank you for playing though!")
            break
            break
        elif y_n_last == 'y':
            print("Alright! Now restarting...")
            break
        else:
            print("It's your last time answering, and you still dont know how to?")
            print("Again, please type 'y' or 'n'.")
