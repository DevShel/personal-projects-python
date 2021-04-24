import random

contact_list = []
grab_num = 0
requestLeave = False
 
def contact_grab_num():
    grab_num = input("What number contact would you like to grab?")
    return(grab_num)
def name_add(name_selection):
    contact_list.insert((len(contact_list)+1),str(name_selection))

while (requestLeave == False):
    if ((len(contact_list))>0):
        print("There are " + str(len(contact_list)) + " contacts to pick from")
        if (input("Would you like to add a contact? ") =="yes"):
            name_search = str(input("Type the name of a contact")) 
        else:
            grab_num = contact_grab_num()
    else:
        print("There are no contacts, why don't you add one?")
        if (input("Would you like to add a contact? ") == "yes"):
            name_selection = str(input("Type the name of a contact")) 
            name_add(name_selection)
    print(contact_list)
    
    if (input("Would you like to continue to look through your contact book? ") =="yes"):
            name_search = str(input("Type the name of a contact")) 
    else:
            print("Goodbye")
            leave = True


