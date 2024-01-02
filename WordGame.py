import random

def main():
    print("Welcome to the Text Adventure Game!")
    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name}!")

    while True:
        print("You find yourself in a dark forest. You can go 'left' or 'right'.")
        choice = input("Which way do you want to go? ").lower()

        if choice == "left":
            explore_left(player_name)
        elif choice == "right":
            explore_right(player_name)
        else:
            print("Invalid choice. Please enter 'left' or 'right'.")

def explore_left(player_name):
    print("\nYou venture deeper into the forest and stumble upon a mysterious cave.")
    print("You can 'enter' the cave or 'go back'.")
    choice = input("What will you do? ").lower()

    if choice == "enter":
        encounter_monster(player_name)
    elif choice == "go back":
        print("You decide not to enter the cave and return to the forest.")
    else:
        print("Invalid choice. Please enter 'enter' or 'go back'.")

def explore_right(player_name):
    print("\nAs you move to the right, you come across a tranquil river.")
    print("You can 'cross' the river or 'turn back'.")
    choice = input("What will you do? ").lower()

    if choice == "cross":
        print("You successfully cross the river and continue your journey.")
    elif choice == "turn back":
        print("You decide not to cross the river and return to the forest.")
    else:
        print("Invalid choice. Please enter 'cross' or 'turn back'.")

def encounter_monster(player_name):
    print("\nYou enter the dark cave and encounter a fearsome dragon!")
    print("You have no choice but to fight!")

    player_health = 100
    dragon_health = 150

    while player_health > 0 and dragon_health > 0:
        player_attack = random.randint(10, 25)
        dragon_attack = random.randint(5, 20)

        print(f"{player_name} attacks the dragon for {player_attack} damage.")
        dragon_health -= player_attack

        print(f"The dragon attacks {player_name} for {dragon_attack} damage.")
        player_health -= dragon_attack

        print(f"Your health: {player_health} | Dragon's health: {dragon_health}")

    if player_health <= 0:
        print("You have been defeated by the dragon. Game over!")
    else:
        print("You have defeated the dragon! Congratulations, you are victorious!")

if __name__ == "__main__":
    main()
