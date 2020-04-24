
from data.capitals import states
import random
import sys

for state in states:
  state['incorrect'] = 0
  state['correct'] = 0


game_init = True
game_play = False
game_replay = False


while game_init:
  print("Welcome to the State Capitals game, where everything is geography and the points don't matter!")
  user_input = input("Test your knowledge --> Match as many Capitals to their States as you can <-- Press <y> to Start   ")
  if user_input == "y":
    print("Starting game...")
    game_play = True
    game_init = False
  else:
    game_init = False
    print("Goodbye!")
    sys.exit()

  while game_play:
    correct = 0
    incorrect = 0
    random.shuffle(states)
    for state in states:
      index = states.index(state)
      user_guess = input(f"What is the capital of {state['name']}?   ")
      if user_guess.upper() == state['capital'].upper():
        print("Way to go!")
        correct += 1
        state['correct'] += 1
        print(f"Your Score: {correct}/{index + 1}")
      else: 
        print(f"Hit the books! The correct answer is {state['capital']}")
        incorrect += 1
        state['incorrect'] += 1
        print(f"Your Score: {correct}/{index + 1}")
    print(f"That's all 50 states! Your final score is {correct}/{index + 1}")
    game_play = False
    game_replay = True

    while game_replay:
      user_input = input("Thanks for playing, press y to play again!   ")
      if user_input == "y":
        game_replay = False
        game_init = True
      else:
        if (incorrect >= 30):
          print(f"You only guessed {correct} correctly, you should really play again for more practice.")
        else:
          print("Thanks for playing -- Goodbye!")
          game_play = False
          sys.exit()



