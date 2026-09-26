import random


def predict_ball(user_num):
    computer_game = random.randint(1, 6)
    print(f"You played: {user_num}")
    print(f"Computer played: {computer_game}")

    if user_num == computer_game:
        print("OUT! 🏏")
        return "out"
    else:
        print(f"Runs scored: {user_num}")
        return user_num


user_num = int(input("Enter a number (1-6): "))
result = predict_ball(user_num)
print(f"Result: {result}")