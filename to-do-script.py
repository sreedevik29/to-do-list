to_do = {"Work": "", 
		"School": "",
		"Exercise": ""}			
active = True

while active:
    user_input = raw_input("Add an activity: ")
    input_type = raw_input("What type of activity is this? ")
    if input_type.lower() in ("work", "job"):
    	to_do.update({"Work": user_input})
    elif input_type.lower() in ("exercise", "workout"):
    	to_do.update({"Exercise": user_input})
    elif input_type.lower() in ("school", "uni"):
    	to_do.update({"School": user_input})
    else:
    	print("Sorry! That's not a category, please enter another category! ")
    more_activities = raw_input("Do you have more? Type 'yes' or 'y' to add more activities the to do list or type 'no' or 'n' to stop making the list: ")
    if more_activities == "no" or more_activities == "n":
        print("Here are the list of things you have to do: " + str(to_do))
        active = False

