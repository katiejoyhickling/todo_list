"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""
    print "Here are the current items in your todo list:"

    

    user_item = raw_input("What would you like to add to the list? ")
    user_item = user_item.capitalize()
    user_item_index = raw_input("What number would you like this item to be in your list? ")
    user_item_index = int(user_item_index)


    my_list.insert(user_item_index, user_item)

    print "{} has been added to your todo list.".format(user_item)


def view_list(my_list):
    """Print each item in the list."""

    for index in range(len(my_list)):
        print "{}. {}".format(index,my_list[index])


def delete_item(my_list):
    """Deletes an item from the list per user input."""

    print "Here are the current items in your todo list:"

    for index in range(len(my_list)):
        print "{}. {}".format(index,my_list[index])

    user_delete = raw_input("Enter the item number which you would like to delete: ")
    user_delete = int(user_delete)

    print "{} has been deleted from the todo list.".format(my_list[user_delete])

    my_list.pop(user_delete)


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""
    playing = True

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Delete an item
    D. Quit the program
    """
  
    while playing:
        print user_options
        user_choice = raw_input(">>> " ).capitalize()
        if user_choice == "A": 
            add_to_list(my_list)
        elif user_choice == "B":
            view_list(my_list)
        elif user_choice == "C":
            delete_item(my_list)
        else:
            playing = False
        # Collect input and include your if/elif/else statements here.
      

#-------------------------------------------------

karas_list = []
display_main_menu(karas_list)


