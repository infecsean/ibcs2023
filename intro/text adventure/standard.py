def user_input() -> int:
    try:
        return int(input("Make a choice: "))
    except (ValueError, TypeError):
        return -1


def start():
    print(
        """
        It's a dark and stormy night and you believe you're home alone.
        You are sitting on your bed watching Youtube videos.
        You hear a sound coming from the other room.
        What do you do?

                1. Turn up the volume
                2. Listen carefully for the sound
                3. Investigate the sound
        """
    )

    choice = -1
    while choice < 1 or choice > 3:
        choice = user_input("Make a choice: ")

        if choice == 1:
            volume()
        elif choice == 2:
            listen()
        elif choice == 3:
            investigate()
        else:
            print("Please choose 1, 2, or 3")


def volume():
    pass


def listen():
    print(
        """
        You listen carefully to the sounds in your house.
        After a few minutes you hear a strange noise coming from the other room.
        You believe someone is moving in that room.

        What do you want to do?

            1. Lock your door
            2. Investigate the intruder
            3. Turn the volume even louder
        """
    )
    choice = -1
    while choice < 1 or choice > 3:
        choice = user_input("Make a choice: ")

        if choice == 1:
            lock_door()
        elif choice == 2:
            investigate()
        elif choice == 3:
            volume()
        else:
            print("Please choose 1, 2, or 3")


def lock_door():
    print(
        """

        Turns out its the lock picking lawer, he picks your lock and kills you
        """
    )


def investigate():
    print(
        """
    
        You go and see the thing...
    
        """
    )


if __name__ == "__main__":
    start()
