from random import randint
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")

while True:
    print("Enter choise \n 1. Rock \n 2. paper \n 3. scrissor \n")

    choice = int(input("User turn: "))


    while choice > 3 or choice < 1:
        choice = int(input("Enter Invalid input: "))

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"

    print(f"User choice is :{choice_name}")
    print("\nNow is computer turn......")

    comp_choise = randint(1, 3)

    while comp_choise == choice:
        comp_choise = randint(1, 3)

    if comp_choise == 1:
        comp_choise_name = "Rock"
    elif comp_choise == 2:
        comp_choise_name = "Paper"
    else:
        comp_choise_name = "Scissor"

    print(f"Your choice {choice_name}")
    print(f"Computer choise is:{comp_choise_name}")
    print(f"{choice_name} Vs {comp_choise_name}")

    if ((choice == 1 and comp_choise == 2)) or (choice == 2 and comp_choise == 1):
        print("Paper Wins => ", end=" ")
        result = "Paper"
    elif ((choice == 1 and comp_choise == 3) or (choice == 3 and comp_choise == 1)):
        print("Rock Wins =>", end=" ")
        result = "Rock"
    else:
        print("Scissor Wins =>", end=" ")
        result = "Scissor"

    if result == choice_name:
        print("<==User Wins==>")
    else:
        print("<==Computer Wins==>")

    print("Do you want to play again? (Y/N)")
    ans = input().upper()

    if ans == "N":
        break

print("\nThanks for playing")
