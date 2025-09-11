
def print_options():
    print("""
          What would you like to do? 
          1. View List
          2. Add To List
          3. Remove Item From List
          4. Exit""")

# Helper function to get valid integer input from user
def get_int(prompt):
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


def add_to_list():
    # Keep asking until the user enters a valid integer using helper function
    num_of_items = get_int("How many items would you like to add to the list? ")
    
    # Adds n items to list
    for i in range(num_of_items):
        list_item = input("What would you like to add to the list? ")
        with open("to-do-list.txt", "a") as f:
            f.write(f"{list_item}\n")
