
def print_options():
    print("""
          What would you like to do? 
          1. View List
          2. Add To List
          3. Remove Item From List
          4. Exit""")



def add_to_list():
    # Keep asking until the user enters a valid integer
    while True:
        try:
            num_of_items = int(input("How many items would you like to add to the list? "))
            if num_of_items > 0:
                break
            else:
                print("Please enter an integer greater than 0")
        except ValueError:
            print("Please enter a valid integer")

    # Adds n items to list
    for i in range(num_of_items):
        list_item = input("What would you like to add to the list? ")
        with open("to-do-list.txt", "a") as f:
            f.write(f"{list_item}\n")


def to_do_list():
    print("Welcome to your to-do-list!")






    

