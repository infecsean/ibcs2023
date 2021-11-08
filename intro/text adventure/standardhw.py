def user_input() -> int:
    try:
        return int(input("Do something: "))
    except (ValueError, TypeError):
        return -1


def start():
    print(
        """
        You enter a 7-11, you see a man pointing a knife at the cashier.
        He doesn't seem to notice you tho.

        What do you do?

            1. Recall the video you watched on youtube on how to disarm a person and try to recreate it
            2. Go look for the thing you wanted to buy
            3. "Fuck this" and run away
            4. Call the police
        """
    )

    choice = -1
    while choice < 1 or choice > 4:
        choice = user_input("Do something: ")

        if choice == 1:
            tryHero()
        elif choice == 2:
            sigma()
        elif choice == 3:
            coward()
        elif choice == 4:
            call911()
        else:
            print("Please choose 1, 2, 3, or 4")


def tryHero():
    print(
        """
        You cant seem to remember, so you open youtube on your phone
        You forgot to turn off the volume before you play
        The loud dubstep intro music gets the attention of the man and the cashier
        He says: "What the fuck are you watching? You tryna get killed?"

        What do you do?

            1. Walk over and try to disarm him
            2. Excuse yourself

        """
    )

    choice = -1
    while choice < 1 or choice > 2:
        choice = user_input("Do something: ")

        if choice == 1:
            tryHero2()
        elif choice == 2:
            coward()
        else:
            print("Please choose 1 or 2")


def tryHero2():
    print(
        """
        You walk over and grab his arm
        He instantly shakes you off and cuts of your arm in one swift swing
        You say: "Thats impossible! The force of your swing couldnt have possib-"
        He sticks the knife up your throat and says: "Shut the fuck up, please"
        You gargle in your own blood and falls to the ground
        
        """
    )


def sigma():
    print(
        """
        You ignore them and go to the chip isle.
        You grab two party sized sour flavored lays chip that is 2/3 air
        The man is still pointing the knife at the cashier
        
        What do you do?

            1. You still pay for your stuff like a good citizen
            2. You take advantage of the situation and walk right out
        """
    )
    choice = -1
    while choice < 1 or choice > 2:
        choice = user_input("Do something: ")

        if choice == 1:
            goodguy()
        elif choice == 2:
            coward()
        else:
            print("Please choose 1 or 2")


def coward():
    print(
        """
            You walk out and get hit by a car.
            karma lol, dont be a coward
        
        """
    )


def call911():
    print(
        """
        You pull out your phone and dial 911
        Someone picks up the phone and says:
        "You see, in Taiwan, we use 119. You made a mistake and you will face the punishment."
        Your phone explodes into your face, you fly backwards and die
    
        """
    )


def goodguy():
    print(
        """
        You wait behind the man and say:
        "You gonna pay or what?"
        He turns around and says:
        "Nah, you can go first"
        You walk in front of him and pay for your snacks
        You walk away with two bags of party sized chips in your arms, 
        *This is the good ending*(Not for the cashier tho)
        """
    )


if __name__ == "__main__":
    start()
