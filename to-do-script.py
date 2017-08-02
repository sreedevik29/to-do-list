data = {}	
active = True

while active:
    activity = raw_input("Add an activity: ")
    category = raw_input("What type of activity is this? ")
    if data.keys().__contains__(category.lower()):
        data[category.lower()].append(activity)
    else:
        data[category.lower()] = [activity]
    more_activities = raw_input("Do you have more? Type 'yes' or 'y' to add more activities the to do list or type 'no' or 'n' to stop making the list: ")
    if more_activities == "no" or more_activities == "n":
        print("Here are the list of things you have to do: " + str(data))
        active = False

