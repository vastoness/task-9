def manage_scoreboard(rounds: list[tuple[int, int]]) -> dict:
    scoreboard = {}
    for player, score in rounds:
        if player in scoreboard:
            scoreboard[player] += score
        else:
            scoreboard[player] = score
    return scoreboard
if __name__ == "__main__":
    rounds = []
    print("Enter rounds, points and type done when ur over")
    
    while True:
        user_input = input()
        if user_input.lower() == "done":
            break
        
        try:
            player, score = map(int, user_input.split())
            rounds.append((player, score))
        except ValueError:
            print("Invalid input. Please enter in the format 'player score'.")

    fscores = manage_scoreboard(rounds)
    print("final Scores:")
    for player, score in sorted(fscores.items()):
        print(f"Player {player}: {score}")