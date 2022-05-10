#----TEXT MESSAGE ABBREVIATIONS TRANSLATOR PROGRAM-----
#Summary:
'''
- This program will take a text message and translate into words
    your grandparents could understand.
    ex)
        - so funny LOL ROTFL
        becomes
        - So funny laughing out loud rolling on the floor laughing

- For this scenario we will start with a file that lists all the text message abbreviations and the translation
'''
#---------------QUESTIONS & FINDINGS AS I PROGRESS...
'''
How to remove spaces from string?
    - the python tuple is immutable, so we can't change it's value. Any function that manipulates string value
        returns a new string.
    - strip() 
                > python string strip() function will remove leading and trailing whitespaces
    - replace()
                > to remove all the whitespaces from the string. This function will remove whitespaces between
                words too ex. variable.replace(" ", "")
    - The replace method can be coupled with list comprehension to replace string in list... List comprehensions
        ...performs the task of iterating through the list and replaces the section of substring with another
Partition()
        > this method partitions the given string based on the first occurence of the delimeter and it generates
        tuples that contain three elements. First string, second, delimeter, third is string after first occurence of the delimiter
'''

def _main_():
    #setting initial variables
    user_dict = { }
    abbrivation = []
    meaning_list = []
    
    #next open the file containing all possible text acronyms and their translations
    with open("3000 Popular Text Acronyms in English.txt","r") as text_acronym_file:
        for line in text_acronym_file:#iterating through text abreviations file
            abbrivation = line.partition("\t")[0]#partitioning first column in the file as acronym abriviation - dict key
            meaning_list = line.partition("\t")[2]#partitioning second column(translated acronym) as abriviation meaning - dict value
            user_dict[abbrivation] = meaning_list

    infoMessage = print("\nWelcome to the TEXT ABBREVIATIONS TRANSLATOR\n"\
                         "INFO:----[This program takes your message and translates the text acronyms ]\n"\
                         "\nCURRENT FILE DIRECTORY: ~3000 Popular Text Acronyms in English 4.15.22~ \n"
                         "\nExample listed below:\n"\
                         "User message: 'Idk lol'\n"
                         "Output: 'I DON'T KNOW LAUGH OUT LOUD\n\n\n--------------------------------------------")

    user_msg = input("TYPE MESSAGE(do NOT include commas in sentence): ") 
    token_searchResults = [] #stores F(found) = if word is actuall text abriviation in our text abr. file

                        
    #the bulk of the progams logic, this function is intended to take the stored user input and compare that with our text abriviation file
    #Lastly the function changes the acronym(s) found in the user input to the translated meaning given user input message
    def word_translate(): 
        print ("\nYour input was... ['" + user_msg + "']\n")
        user_msg_list = user_msg.upper().split()
        
        for word in user_msg_list: #loop through user input str list
            for key in user_dict.keys(): #loop through dictionary keys for every str in user input list
                
                if word == key: #refrence user input and value key in dictionary
                    indexOfWord = user_msg_list.index(word) #find index of word in the user str list
                    user_msg_list[indexOfWord] = user_dict[key] #set word(abrivation) at index as value(translation)
                    token_searchResults.append(word)#if "F" - add word to token search count
                                    
        return(user_msg_list) #function then returns new translated list


    def list_translation(): #defining function that takes translated user list and converts into single sum string           
        user_str_translation = " "
        for word in word_translate():#looping through each word in user translated list
            number_of_keywords_count = len(token_searchResults)#initializing variable that tracks the number of keywords the user uses in
                                                                #input that is in dictionary
            
            user_str_translation += word + " " #adding each word in list to make up complete string of user translation
            
        print(token_searchResults)
        print("ACRONYMS FOUND: " + str(number_of_keywords_count )+"/" +str(len(user_dict))) #messge format
        print("\nRESULT: " + user_str_translation.upper()) #display the translated abriviation(s)(if any) in user input
        

    list_translation()

_main_()
