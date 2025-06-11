import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid input. Please enter rock, paper, or scissors.")

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def get_round_limit():
    while True:
        choice = input("Choose round mode: Best of 3 or Best of 5? (3/5): ").strip()
        if choice == '3':
            return 2  # first to 2 wins
        elif choice == '5':
            return 3  # first to 3 wins
        else:
            print("Invalid input. Please enter 3 or 5.")

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    round_wins_needed = get_round_limit()

    user_score = 0
    computer_score = 0
    round_number = 1

    while user_score < round_wins_needed and computer_score < round_wins_needed:
        print(f"\n🔁 Round {round_number}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            user_score += 1
            print("✅ You win this round!")
        elif winner == "computer":
            computer_score += 1
            print("❌ Computer wins this round!")
        else:
            print("⚖️ It's a tie!")

        print(f"Score -> You: {user_score} | Computer: {computer_score}")
        round_number += 1

    print("\n🏁 Game Over!")
    if user_score > computer_score:
        print("🎉 Congratulations! You won the game!")
    else:
        print("💻 The computer wins! Better luck next time.")

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
