import random

def roll():
    min_raqam = 1
    max_raqam = 6
    roll = random.randint(min_raqam, max_raqam)

    return roll

while True: 
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else: 
            print("Must be between 2 - 4 players.")

    else:
        print("Invalid, try again!")

max_score = 20
player_scores = [0 for _ in range(players)]

while max(player_scores)< max_score:

    for player_id in range(players):
        print(f"\nPlayer {player_id + 1} turn has just started!")
        print(f"Your total score: {player_scores[player_id]} \n")
        current_score = 0 

        while True:
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower()!= 'y':
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is: ", current_score)

        player_scores[player_id] += current_score
        print("Your total score is: ", player_scores[player_id])

max_score = max(player_scores)
winning_id = player_scores.index(max_score)
print(f"Player number {winning_id +1} is the winner with a scoreof: {max_score}")

