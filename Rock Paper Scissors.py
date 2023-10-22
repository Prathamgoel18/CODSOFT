import random


def get_user_choice():
    print("\nChoices: \n1. Rock \n2. Paper \n3. Scissors")
    choice = input("Enter your choice (1/2/3): \n")

    choices_dict = {'1': 'Rock', '2': 'Paper', '3': 'Scissors'}

    return choices_dict.get(choice, None)


def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])


def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    if (user == 'Rock' and computer == 'Scissors') or \
            (user == 'Scissors' and computer == 'Paper') or \
            (user == 'Paper' and computer == 'Rock'):
        return "User"
    else:
        return "Computer"


def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        if not user_choice:
            print("Invalid choice. Please choose 1, 2, or 3.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        print(f"\nUser's Choice: {user_choice}")
        print(f"Computer's Choice: {computer_choice}")

        if winner == "User":
            print("You Win!")
            user_score += 1
        elif winner == "Computer":
            print("Computer Wins!")
            computer_score += 1
        else:
            print("It's a Tie!")

        print(f"\nScore: \nUser: {user_score} \nComputer: {computer_score}\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
