
checklist = list()

# Create
def create(item):
    checklist.append(item)

#Read
def read(index):
    item = checklist[index]
    return item

#Update
def update(index, item):
    checklist[index] = item

#Destroy
def destroy(index):
    checklist.pop(index)

#List
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

#Checkmark
def mark_completed(index):
    update(index, "√" + checklist[index])

#Selects from user input
def select(function_code):

    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index Number?")
        read(item_index)

    elif function_code == "P":
        list_all_items()

    else:
        print("Unknown Option")

#Waits for user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

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
    select("C")
    list_all_items()
    select("R")
    list_all_items()

test()


