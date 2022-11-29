# Python3 program to get selected
# value(s) from tkinter listbox

# Import tkinter
from tkinter import *

# Create the root window
root = Tk()
root.geometry('380x450')

# Create a listbox
listbox = Listbox(root, width=40, height=10, selectmode=MULTIPLE)

# Inserting the listbox items
listbox.insert(1, "Data Structure")
listbox.insert(2, "Algorithm")
listbox.insert(3, "Data Science")
listbox.insert(4, "Machine Learning")
listbox.insert(5, "Blockchain")


# Function for printing the
# selected listbox value(s)
def selected_item():
    ret = {}
    for i in listbox.curselection():
        print(listbox.get(i))
    listbox.delete(0, END)
    listbox.insert(1, "Cheese plate")
    listbox.insert(2, "Rice")
    listbox.insert(3, "Salad")


# Create a button widget and
# map the command parameter to
# selected_item function
btn = Button(root, text='Print Selected', command=selected_item)

# Placing the button and listbox
btn.pack(side='bottom')
listbox.pack()

root.mainloop()


def select_entities(people, places, organizations):
    ret = {'people': [], 'places': [], 'organizations': []}
    if len(people) > 0:
        ret['people'] = ask_multi_choice("People", people.values)
    if len(places) > 0:
        ret['places'] = ask_multi_choice("Places", places.values)
    if len(people) > 0:
        ret['organizations'] = ask_multi_choice("Organizations", organizations.values)
    return ret


#def get_query():
#    return prompt([{'type': 'input', 'name': 'query',
#                    'message': 'Enter a list of entities:'}])['query']
