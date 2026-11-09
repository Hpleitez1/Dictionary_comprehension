student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


Nato = pandas.read_csv("nato_phonetic_alphabet.csv")
Nato_alpha = pandas.DataFrame(Nato)

nato_dictionary = {row.letter:row.code for (index,row) in Nato_alpha.iterrows()}

keep_running = True
while keep_running:
    user_input = input("Enter a word: ").upper().strip()
    print("To exit type 'q' to quit.\n")
    if user_input == "Q":
        keep_running = False
    else:

        nato_alpha_list = [nato_dictionary[letter] for letter in user_input if letter in nato_dictionary]

        print(nato_alpha_list)

