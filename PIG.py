import random 

def roll():
    return random.randint(1, 6)

# Get number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        print("Invalid! Number of players must be between 2 and 4.")
    else:
        print("Invalid input! Please enter a number.")

print(f"\n🎲 Starting game with {players} players!\n")

max_score = 50
player_score = [0 for _ in range(players)]

# Game loop
while max(player_score) < max_score:
    for player_index in range(players):
        print(f"\n➡️ Player {player_index+1}'s turn")
        print("-" * 30)
        current_score = 0

        while True:
            should_roll = input("Roll the dice? (y/n): ")
            if should_roll.lower() != "y":
                print(f"Player {player_index+1} holds. Turn score = {current_score}")
                break

            value = roll()
            if value == 1:
                print("🎯 Oops! You rolled a 1. No points this turn.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"🎲 You rolled a {value}. Turn score = {current_score}")

        player_score[player_index] += current_score
        print(f"✅ Player {player_index+1}'s Total Score = {player_score[player_index]}")

        # Check win condition
        if player_score[player_index] >= max_score:
            print("\n" + "="*40)
            print(f"🏆 Player {player_index+1} wins with {player_score[player_index]} points!")
            print("="*40)
            exit()

    # Show leaderboard after each round
    print("\n📊 Leaderboard:")
    for i, score in enumerate(player_score, start=1):
        print(f"   Player {i}: {score} points")
