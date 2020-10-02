print("\t\t\t Welcome to Snake, Water and Gun Game\n")

import random
lst=["Snake", "Water", "Gun"]
print(lst)
chances= "10 chances"
u="You have %s"% (chances)
print(u)
no_of_chances=10
human_score=0
computer_score=0
print("Guess,S for Snake , W for Water and G for Gun.")
while(no_of_chances<=10 and no_of_chances>0):
			print("Enter the guess from above:")
			a=input()
			#print(a.capitalize())
			rand=random.choice(lst)
			#user enter Snake
			if a=="S" and rand=="Gun":
				info=f"Your guess is {a} and computer guess is {rand}."
				print(info)
				computer_score=computer_score+1
				print("Computer score is :",computer_score)
				no_of_chances=no_of_chances-1
				print("no_of_chances left are :" ,no_of_chances)
			elif a=="S" and rand=="Water":
				info=f"Your guess is {a} and computer guess is {rand}."
				print(info)
				human_score=human_score+1
				print("human_score is :",human_score)
				no_of_chances=no_of_chances-1
				print("no_of_chances left are :" ,no_of_chances)
				#user enter water
			elif a=="W" and rand=="Gun":
				info=f"Your guess is {a} and computer guess is {rand}."
				print(info)
				human_score=human_score+1
				print("Human score is :",human_score)
				no_of_chances=no_of_chances-1
				print("no_of_chances left are :" ,no_of_chances)
			elif a=="W" and rand=="Snake":
				info=f"Your guess is {a} and computer guess is {rand}."
				print(info)
				computer_score=computer_score+1
				print("Computer score is :",computer_score)
				no_of_chances=no_of_chances-1
				print("no_of_chances left are :" ,no_of_chances)
				#user enter gun
			elif a=="G" and rand=="Water":
				info=f"Your guess is {a} and computer guess is {rand}."
				print(info)
				computer_score=computer_score+1
				print("computer_score is :",computer_score)
				no_of_chances=no_of_chances-1
				print("no_of_chances left are :" ,no_of_chances)
			elif a=="G" and rand=="Snake":
				info=f"Your guess is {a} and computer guess is {rand}."
				print(info)
				human_score=human_score+1
				print("Human_score is :",human_score)
				no_of_chances=no_of_chances-1
				print("no_of_chances left are :" ,no_of_chances)
			elif a==rand:
				info= f"Your guess is {a} and computer guess is {rand} is same."
				print(info)
				no_of_chances=no_of_chances-1
				print("no_of_chances left are :" ,no_of_chances)
				info=f"You got 0 and computer got 0 point for this guess."
				print(info)
			elif a!=lst:
				print("You enter wrong input")
				print("Try Again!")
				no_of_chances=no_of_chances-1
				print("no_of_chances left are :" ,no_of_chances)
		
			if (no_of_chances<=0):
							if human_score==computer_score:
								print("Score equal!\nGame Over!")
								break
							elif human_score>computer_score:
								info=f"human_score is {human_score} and computer_score is {computer_score}."
								print(info)
								print("You are Winner!")
								break
							if human_score<computer_score:
									info=f"computer_score is {computer_score} and human_score is    {human_score}."
									print(info)
									print("You lose!")
									break