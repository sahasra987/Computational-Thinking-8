home_points = 0
restaurant_points = 0


answer = input("Would you A eat pasta all day, or B sushi all day?")
if answer == "A" or answer == "a":
	home_points += 1
elif answer == "B" or answer == "b":
	restaurant_points += 1


answer = input("Do you A like eating out, or B eating at home?")
if answer == "A" or answer == "a":
	restaurant_points += 1
elif answer == "B" or answer == "b":
	home_points += 1


answer = input("Would you rather A eat by yourself, or B with a group?")
if answer == "A" or answer == "a":
	home_points += 1
elif answer == "B" or answer == "b":
	restaurant_points += 1
	

answer = input("do you like A Pagliacci pizza?, or do you like B homemade pizza?")

if answer == "B" or answer == "b":
	home_points += 1
elif answer == "A" or answer == "a":
	restaurant_points += 1
		

answer = input("would you rather A talk with other people?, or B not talk to others and be alone?")

if answer == "B" or answer == "b" and home_points:
	print ("You really like being at home!")
	home_points += 1
elif answer == "A" or answer == "a":
	restaurant_points += 1

#end of quiz:
if restaurant_points > home_points:
	print("You are a restaurant person")
elif home_points > restaurant_points:
	print ("You are a home person")