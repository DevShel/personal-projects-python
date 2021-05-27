import requests
# The purpose of this program is to find unclaimed github usernames using common english words
all_usernames = []
available_list = []


#word list copied from: https://github.com/mahsu/IndexingExercise/blob/master/5000-words.txt

words = open("C:/Users/Sheldon/Desktop/words.txt", "r")

#function for minimizing future code if needed to run through list multiple times
def run_through_text():
    for line in words:
        all_usernames.append(line.strip())

#function that searches using common english words and exports to an outputted list
def generate_username_list():
    print("Checking for users")
    #try catch for index error that could possibly occur
    try:
        for i in range(len(all_usernames)-1):
            
            current_user = all_usernames[i]
            availability_check = requests.get("https://github.com/" + current_user + "/")

            #if the username does not currently exist for whatever reason
            if availability_check.status_code == 404:
                print("User '" + str(current_user) + "' is not taken and has been added to unclaimed username list")
                available_list.append(current_user)
                
            else:
                print("User '" + str(current_user) + "' is unfortunately taken.")
    except IndexError:
        print("You have reached the end of the list")
    
run_through_text()
generate_username_list()
print("Unclaimed Usernames: ")
print(available_list)