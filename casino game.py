import time
import random
current=0
def winner():
	global price
	global bet_amount
	global Name
	if a==num:
		with open("myacc.txt","a") as f:
			string=" "
			string +=str("\n")
			string +=str("\n Account Details : ")
			string +=str("\n")
			string += str(" You has credited :- ")+ str(" ")+ str(price)
			f.write(string)
def lose():
	if a!=num:
		with open("myacc.txt","a") as f:
			string=" "
			string +=str("\n")
			string +=str("\n Account Details : ")
			string +=str("\n")
			string +=str(" You has debited :- ")+   str(f"{initial_balance} - {bet_amount}.")+ str(" ")+ str(current)
			f.write(string)
			
def Multiplayer():
	print("\tMaximum 10 players are allowed")
	players=int(input("\tNumber of players : "))
	if players>10:
		print("\tYou excced extra number of player")
		print("\tTry for sinlge person game.")
		print("~~~~~~~~~~~~~~~~~-->~")
		menu()
	elif players<10:
		for i in range (players):
			accout()
		print("\tIts player 1 chance.")
		new_game()
		start_game()
		print("\tIts player 2 chance.")
		new_game()
		start_game()
		print("~~~~~~~~~~~~~~~~~-->~")
		menu()
#def account1():
#		R=open("detail.txt","r+")
#		con=R.read()
#		print(con)
#		R.close
		print("~~~~~~~~~~~~~~~~~-->~")
		menu()
		
def myaccount():
		f=open("myacc.txt","r+")
		c=f.read()
		print(c)
		
		f.close

"""def myaccount1():
		f=open("detail.txt","r+")
		con=f.read()
		print(con)
		f.close """
def clearacc():
		f=open("myacc.txt","r+")
		f.truncate()
		print("RECORDS CLEAR SUCCESSFUL!")
		f.close()
"""def clearacc1():
		f=open("detail.txt","r+")
		f.truncate()
		print("RECORDS CLEAR SUCCESSFUL!")
		f.close()"""
pnt("~~~~~~~~~~~~~~~~~-->~")


#common player game
def new_game():
	b=random.(1,11)
	print(f"\tComputer has assign you {b} table number  to play .")
	print("\tHow much do you want to bet...?")
	global bet_amount
	global initial_balance
	bet_amount=int(input())
	if bet_amount>initial_balance:
		print("\tYou can't play")
		menu()
#muliteplayer game		
def start_game():
	num=int(input("\tEnter the betting number : "))
	a=random.randint(1,10)
	print("\tplease wait, wheel your teammate will roll the wheel.")
	print("\tWheel is rolling..")
	print(time.sleep(1))
	if a!=num:
		print("\tbetter luck next time...")
		print("\tThe number arrived is : ", a)
		print("\tYou lose the game.")
		print("\tYou lost your amount ...")
		#menu()
	elif a==num:
		print("\tYou have a great luck,since you got a match.! ")
		print("\tWow!!!Amount has been cashed...")
		#amt=int(input("Enter the amount you betted..."))
		global price
		price=bet_amount *10
		print("Here's, your cash price ",price)
		#menu()
	else:
		print("~~~~~~~~~~~~~~~~~-->~")
		menu()		
	
def rules():
    print("Wel come to Rihan Casino\n")
    print("\nCASINO RULES\n")
    print("\n1] -->PLay safe\n2] -->Dont panic\n3]--> TAKE CARE of your BAnk BAlanCe\n4]--> Choose one number from 10\n5]--> One random number will be choosen\n6]If you win you will get 10 Times the amount you bet")


def start_game1():

	global num
	num=int(input("\tEnter the betting number : "))
	global a
	a=random.randint(1,10)
	print("\tplease wait, wheel is rolling.......")
	print(time.sleep(1))
	if a!=num:
		print("\tbetter luck next time...")
		print("\tThe number arrived is : ", a)
		print("\tYou lose the game.")
		print("\tYou lost your amount ...")
		print("~~~~~~~~~~~~~~~~~-->~")
		menu()
	elif a==num:
		print("\tYou have a great luck,since you got a match.! ")
		print("\tWow!!!Amount has been cashed...")
		price=bet_amount *10
		print("\tHere's,your cash price ",price)
		print("~~~~~~~~~~~~~~~~~-->~")
		menu()
	else:
		menu()
def accout():
	print("\tEnter  your details..")
	Name=str(input("\tWhats your Name? : "))
	mobile=int(input("\tNumber : "))
	Address=input("\tEnter your full address : ")
	with open("myacc.txt","a") as f:
		string= " "
		string +=str("\n")
		string +=str("\n Profile Details : ")
		string +=str("\n")
		string +=str("\tMy Name is :- ")+ str(" ")+str(Name)
		string +=str("\n")
		string +=str("\tMobile no :- ")+ str(" ")+str(mobile)
		string +=str("\n")
		string +=str("\taddress :- ")+ str(" ")+str(Address)
		string +=str("\n")
		#initial balance
		global initial_balance
		initial_balance=int(input("\tHow much amount do you have ? \n"))
		if initial_balance<=1999:
			menu()
		string +=("~~~~~~~~~~~~~~~~~-->~")
		f.write(string)
def accoun_details():
			if a==num:
				winner()
			elif a!=num:
				lose()
			menu()

		
		
	
def menu():
	
	print("\n Press 1 to play ==> single new game.\n press 2 to open ==> my account.\n Press 3 to play ==> Multiplayer game.\n Press 4 to ==> clear account info.\n Press 5 to ==> quit game. ")
	print("~~~~~~~~~~~~~~~~~-->~")
	user_in=int(input("\tEnter your choice : "))
	if user_in==1:
		accout()
		new_game()
		start_game1()
	elif user_in==2:
		myaccount()
		menu()
	#	myaccount1()
		
	elif user_in==3:
		Multiplayer()
		new_game()
		start_game()
	elif user_in==4:
		clearacc()
		menu()
	#	clearacc1()
	else:
		exit()	
		
rules()
print("~~~~~~~~~~~~~~~~~-->~")
menu()