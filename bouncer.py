#ask for age
age = input("How old are you? ")

if age:
	age=int(age)
	
	#21, drink, normal entry
	if age >=21:
		print("You are good to enter and can drink!")
	#18-21 wristband
	elif  age >=18:
		print("You can enter, but need a wristband`")
	#too young, sorry
	else:
		print("You're too young. Sorry, little one.")
else:
	print("Please enter an age!")