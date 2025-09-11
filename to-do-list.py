
def print_options():
    print("""
          What would you like to do? 
          1. View List
          2. Add To List
          3. Remove Item From List
          4. Exit""")


def get_int(prompt):
    """Helper function to get valid integer input from user"""
    while True:
        try:
            num_of_items = int(input(prompt))
            if num_of_items > 0:
                break
            else:
                print("Please enter an integer greater than 0 ")
        except ValueError:
            print("Please enter a valid integer ")
    return num_of_items


def check_for_item(item):
    """Helper function that returns True if item is in list, False if item not in list"""
    with open("to-do-list.txt", "r") as f:
        list_items = [line.strip().lower() for line in f]
        if item.strip().lower() in list_items:
            return True
        else:
            return False


def remove_item(item):
    """HelperRemove item from list"""
    with open("to-do-list.txt", "r") as f:
        lines = f.readlines()
    with open("to-do-list.txt", "w") as f:
        for line in lines:
            if line.strip().lower() != item.strip().lower():
                f.write(line)


def add_to_list():
    """Adds item(s) to list"""
    num_of_items = get_int("How many items would you like to add to the list? ")
    
    # Adds n items to list
    for i in range(num_of_items):
        list_item = input("What would you like to add to the list? ")
        with open("to-do-list.txt", "a") as f:
            f.write(f"{list_item}\n")


def remove_from_list():
    """Removes item(s) from list"""
    num_of_items = get_int("How many items would you like to remove from the list? ")
    
    # removes n items from list
    for i in range(num_of_items):
        while True:
                item = input("What item would you like to remove from the list? ")
                if check_for_item(item) == True:
                    remove_item(item)
                    print(f"{item} has been removed from the list!")
                    break
                else:
                    print("That item is not in the list, please enter an item in the list.")


def show_list():    
    """Displays current to-do list to the user"""
    with open("to-do-list.txt", "r") as f:
        to_do_list = f.read()
        print(to_do_list)              
