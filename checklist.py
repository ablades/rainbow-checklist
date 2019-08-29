
checklist = list()

# Create
def create(item):
    checklist.append(item)
    print("\033[1;35;40m" + "Created " + item + "\x1b[0m")

#Read
def read(index):
    print("\033[1;31;40m" + checklist[index] + " is at index " + str(index) + "\x1b[0m")
    return checklist[index]

#Update
def update(index, item):
    print("\033[1;33;40m" + "Updated " + checklist[index] + " to " + item + "\x1b[0m")
    checklist[index] = item

#Destroy
def destroy(index):
    print("\033[1;36;40m" + checklist[index] + " has been removed" + "\x1b[0m")
    checklist.pop(index)

#List
def list_all_items():
    index = 0
    for list_item in checklist:
        print("\033[1;32;40m" + "{} {}".format(index, list_item) + "\x1b[0m")
        index += 1

#Checkmark
def mark_completed(index):
    update(index, "√" + checklist[index])

def unmark_item(index):
    if "√" == checklist[index][0]:
        checklist[index] = checklist[index][1:]
    
    else:
        print("\033[1;34;40m" + "item is not checked" + "\x1b[0m")


#Selects from user input
def select(function_code):

    #Normalize input code
    function_code = function_code.upper()

    try:
        #Create item
        if function_code == "C":
            input_item = user_input("Input item: ")
            create(input_item)

        #Read item
        elif function_code == "R":
            item_index = user_input("Index Number?: ")
            read((int)(item_index))

        #List items
        elif function_code == "P":
            list_all_items()
        
        #Quit
        elif function_code == "Q":
            return False

        #Update item
        elif function_code == "U":
            item_index = user_input("Index of item to update?: ")
            item = user_input("Input update: ")
            update((int)(item_index), item)

        #Delete item
        elif function_code == "D" :
            item_index = user_input("Index of item to destroy: ")
            destroy((int)(item_index))

        #Unmark item
        elif function_code == "UN":
            item_index = user_input("Index of checkmark to remove")
            unmark_item((int)(item_index))

        else:
            print("Unknown Option")

        return True

    except IndexError:
        print("Invalid Index please try again")
        selection_prompt()



#Waits for user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

#Loop that prompts user
def selection_prompt():
    running = True
    while running:
        selection = user_input("Press C to add to list, U to update item in list, D to destroy item in list,"
         + "R to Read from list, P to display list, and Q to quit: ")
        print("\033[H\033[J")
        running = select(selection)

def test():
    create("purple sox")
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))
    list_all_items()
    mark_completed(0)
    list_all_items()
    #select("C")
    list_all_items()
    #select("R")
    list_all_items()

test()

selection_prompt()


