def categoryExists(user_input, data):
    # Check to see if user_input is a real category name
    if user_input.lower() in data.keys():
        return True
    return False

def getCategoryByAlias(user_input, data):
    # If not, check to see if user_input is referring to an aliased category
    for category in data.keys():
        # If you can find the user_input inside the aliases, 
        # return the name of the category, because that is
        # the category that the alias is referring to
        if user_input.lower() in data[category]['alias']:
            return category
    return ""

def main():
    data = {
        "dev": {
            "alias": ["coding", "development"],
            "activities": ["coding lesson", "textbook chapter"]
        }
    }
    active = True
    while active:
        activity = raw_input("Add an activity: ")
        category_name = raw_input("What type of activity is this? ")
        if categoryExists(category_name, data):
            data[category_name.lower()]["activities"].append(activity)
        elif getCategoryByAlias(category_name, data):
            aliased_category = getCategoryByAlias(category_name, data)
            data[aliased_category]["activities"].append(activity)
        else:
            category_data = {
                "alias": [],
                "activities": [activity]
            }
            data[category_name.lower()] = category_data
        print(data)
        more_activities = raw_input("Do you have more? Type 'yes' or 'y' to add more activities the to do list or type 'no' or 'n' to stop making the list: ")
        if more_activities == "no" or more_activities == "n":
            print("Here are the list of things you have to do: " + str(data))
            active = False

if __name__ == '__main__':
    main()