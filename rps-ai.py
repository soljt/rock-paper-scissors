import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Possible moves
moves = ['rock', 'paper', 'scissors']
move_to_index = {'rock': 0, 'paper': 1, 'scissors': 2}
index_to_move = {0: 'rock', 1: 'paper', 2: 'scissors'}

# Generate counter move
def counter_move(move):
    if move == 'rock':
        return 'paper'
    elif move == 'paper':
        return 'scissors'
    else:
        return 'rock'

# Build the neural network
model = Sequential([
    Dense(32, input_dim=3, activation='relu'),
    Dense(32, activation='relu'),
    Dense(3, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Training data
X_train = []
y_train = []

# Main game loop
def play_game():
    global X_train, y_train
    
    player_move = input("Enter your move (rock, paper, scissors): ").lower()
    if player_move not in moves:
        print("Invalid move! Please try again.")
        return
    
    # Predict player's next move using the neural network
    if X_train:
        last_move_vector = np.zeros(3)
        last_move_vector[move_to_index[player_move]] = 1
        prediction = model.predict(np.array([last_move_vector]))[0]
        predicted_move_index = np.argmax(prediction)
        ai_move = counter_move(index_to_move[predicted_move_index])
    else:
        ai_move = random.choice(moves)
    
    print(f"AI chose: {ai_move}")
    
    result = determine_winner(player_move, ai_move)
    print(result)
    
    # Update training data
    if X_train:
        X_train.append(last_move_vector)
        y_train.append(move_to_index[player_move])
        model.fit(np.array(X_train), tf.keras.utils.to_categorical(y_train, num_classes=3), epochs=10, verbose=0)
    else:
        X_train.append(np.zeros(3))
        y_train.append(move_to_index[player_move])

# Run the game
while True:
    play_game()
