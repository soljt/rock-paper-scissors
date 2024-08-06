import random

moves = ['rock', 'paper', 'scissors']

def determine_winner(player_move, ai_move):
    if player_move == ai_move:
        return "It's a tie!"
    elif (player_move == 'rock' and ai_move == 'scissors') or \
         (player_move == 'scissors' and ai_move == 'paper') or \
         (player_move == 'paper' and ai_move == 'rock'):
        return "Player wins!"
    else:
        return "AI wins!"

# Main game loop
def play_game():
    player_move = input("Enter your move (rock, paper, scissors): ").lower()
    if player_move not in moves:
        print("Invalid move! Please try again.")
        return
    
    ai_move = random.choice(moves)
    print(f"AI chose: {ai_move}")
    
    result = determine_winner(player_move, ai_move)
    print(result)

# Run the game
if __name__ == '__main__':
    play_game()