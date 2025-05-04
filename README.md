# FizzBuzz Game

## Project Overview
The FizzBuzz game is an interactive Python program where the user is prompted to guess the output based on divisibility rules of numbers. The game uses random number generation, evaluates conditions, and tracks the user’s score over 5 rounds.

## Features
- Generates a random number between 1 and 100 for each round.
- Asks the user to input "fizz", "buzz", or "fizzbuzz" based on the divisibility of the number.
- Tracks the score across 5 rounds.
- Provides feedback after each answer.
- Displays the final score after 5 rounds.

## Pros and Cons
### Pros:
- Easy to implement with basic Python concepts.
- Engages the user with a simple, fun game.
- Helps practice logical conditions and loops.

### Cons:
- Limited gameplay (only 5 rounds).
- No dynamic difficulty or challenge adjustments.

## How It Works

### 1. Importing the Random Library
The `random` module is imported to generate random numbers for the game.

### 2. Defining the Logic Function
This function checks various conditions:
- If the number is 3, returns "fizz fizz".
- If the number is 36, returns "fizz fizz buzz".
- If divisible by both 3 and 4, returns "fizzbuzz".
- If divisible by 3 or is 6 or 13, returns "fizz".
- If divisible by 4 or is 14, returns "buzz".
- If none of the above, returns the number itself.

### 3. Initializing the Score and Game Loop
- Initializes the score to 0 and sets up a loop to run 5 times.
- For each round, a random number between 1 and 100 is generated.
- Displays the number and asks the user for input (either "fizz", "buzz", or "fizzbuzz").

### 4. Checking User Input and Validation
- The logic function is called to get the correct answer based on the generated number.
- If the user's answer matches the correct answer, the score is incremented by 1.
- If the answer is incorrect, the user is given a "loser" message.

### 5. Displaying the Final Score
- After 5 rounds, the program displays the total score, showing how many correct answers the user gave.

## Example of Usage
1. **Run the Program**: Start the Python script.
2. **Game Rounds**: For each round, the program will generate a random number and ask the user to input the corresponding response: "fizz", "buzz", or "fizzbuzz".
3. **Answer Validation**: The program will compare the user’s input to the correct answer, providing feedback.
4. **Score Tracking**: The score is updated and displayed after each round.
5. **End of Game**: Once 5 rounds are completed, the total score is shown.

## Conclusion
This FizzBuzz game is a simple and fun Python project that helps the user practice number divisibility and logical conditions. It also demonstrates basic concepts like loops, user input, and conditional checks. While the game is straightforward, it can be extended with more features, such as more rounds, difficulty levels, or an improved interface.
