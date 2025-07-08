import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = input("🪨 Rock, 📄 Paper, or ✂️ Scissors? ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice. Try again.")
        return None, None, None

    computer_choice = get_computer_choice()
    print(f"\n🧑 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    if winner == "user":
        print("🎉 You win this round!")
    elif winner == "computer":
        print("😢 Computer wins this round!")
    else:
        print("🤝 It's a tie!")
    return winner, user_choice, computer_choice

def main():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock-Paper-Scissors Game!")

    while True:
        print(f"\n🔁 Round {round_number}")
        winner, user_choice, computer_choice = play_round()

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        elif winner is None:
            continue  # Invalid input, repeat the same round
        round_number += 1

        print(f"\n📊 Scoreboard:")
        print(f"🧑 You: {user_score} | 💻 Computer: {computer_score}")

        play_again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n🏁 Game Over!")
            print(f"Final Scores -> 🧑 You: {user_score} | 💻 Computer: {computer_score}")
            if user_score > computer_score:
                print("🏆 You are the overall winner!")
            elif computer_score > user_score:
                print("💻 Computer wins the game!")
            else:
                print("🤝 It's a tie overall!")
            break

if __name__ == "__main__":
    main()

