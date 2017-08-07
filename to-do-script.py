data = {}   
active = True

while active:
    activity = raw_input("Add an activity: ")
    category = raw_input("What type of activity is this? ")
    if data.keys().__contains__(category.title()):
        data[category.title()].append(activity.title())
    else:
        data[category.title()] = [activity.title()]
    more_activities = raw_input("Do you have more to add? Type 'yes' or 'y' to add more activities the to do list or type 'no' or 'n' to stop making the list: ")
    if more_activities == "yes" or more_activities == "y":
        print("Here are the list of things to do so far with the categories: ")
        print(data)
    else: 
        print("Here are the list of things you have to do: " + str(data))
        active = False