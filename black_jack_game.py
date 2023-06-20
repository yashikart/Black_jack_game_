#black_jack_game
import random
user_card=[]
computer_card=[]
is_game_over=True
def deal_cards():
  cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card
  
def calculate_score(cards):
  
  if sum(cards)==21 and len(cards)==2:
    total=0
    return total
  if 11 in cards and sum(cards)==21:
    cards.remove(11)
    cards.append(1)
    total=sum(cards)
    return total
  else:
    total=sum(cards)
    return total
  
def compare(user_score,computer_score):
  if user_score==computer_score:
    print(f"Game Draw...User Score {user_score} and Computer Score {computer_score}")
  elif user_score>21 or user_score > computer_score:
    print(f"User lose the Game ..User Score {user_score} and Computer Score {computer_score}")
  elif computer_score>21 or computer_score > user_score:
    print(f"Computer Lose the Game..User Score{user_score} and Computer Score {computer_score}")
  
for _ in range(2):
  user_card.append(deal_cards())
  computer_card.append(deal_cards())
  
while is_game_over:
  user_score=calculate_score(user_card)
  computer_score=calculate_score(computer_card)
  
  if user_score==0 or computer_score==0 or user_score==21:
    is_game_over=False
  else:
      print(f"Your card:{user_card} and your Score {user_score} ")
      print(f"Computer Card:{computer_card[0]}")
      choices=input("Type 'y' to draw card and 'n' for no cards. ")
      if choices=='y':
        user_card.append(deal_cards())
      if choices=='n':
        is_less=True
        while is_less:
          if computer_score < 17:
            computer_card.append(deal_cards())
            computer_score=sum(computer_card)
            is_game_over=False
          else:
            is_less=False
            is_game_over=False
compare(user_score, computer_score)
          
          
        
      
 


  

