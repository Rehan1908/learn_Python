import random;

computer_score = 0
user_score = 0


def user_redoornot (decision):
        print(f"You {decision}")
        print(f"the score is Computer : {computer_score} , User : {user_score}")
        print("if you want to play again press y")
        play_again = input()
        play_again.lower
        if play_again == "y":
            return "yes"
        else:
            return "no"
        

is_game_playing = True

while is_game_playing:
 
   
    
    print("Pick a move from Rock (r), paper(p) or scissors(s):")
    
    user1_move = input()
    user1_move.lower()

    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = "r"
    elif random_number == 2:
        computer_move = "p"
    elif random_number == 3:
        computer_move = "s"


    if user1_move == computer_move:
        if user_redoornot("Tied") == "yes":
           continue
        else:
           break
    elif user1_move == "r" and computer_move == "p" or  user1_move == "p" and computer_move == "r" or user1_move == "s" and computer_move == "p":
       user_score += 1
       if user_redoornot("won") == "yes":
        continue
       else:
        break
    else:
      print("Computer Won")
      computer_score += 1
      if user_redoornot("Lost") == "yes":
           continue
      else:
           break
    