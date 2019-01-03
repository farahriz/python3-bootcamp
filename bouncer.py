#ask for age
age = input("How old are you? ")

if age:
	age=int(age)
	#18-21 wristband
	if int(age) >= 18 and int(age) <21:
		print("You can enter, but need a wristband`")
	#21, drink, normal entry
	elif int(age) >=21:
		print("You are good to enter and can drink!")
	#too young, sorry
	else:
		print("You're too young. Sorry, little one.")
else:
	print("Please enter an age!")