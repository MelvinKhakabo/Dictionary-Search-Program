#object oriented programming in python

#import the json module to read the data
import json

#load JSON data in the pyhon directory
def load_dictionary():
    with open('data.json') as file:
        data = json.load(file)
    return data

#test if data loads properly
dictionary = load_dictionary()
print(dictionary)


#create function to return a words definition
def get_definition(word, dictionary):
    # Lowercase the word to handle case insensitivity
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        return "The word doesn't exist in the dictionary."

#test thiis function
dictionary = load_dictionary()
word = input("Enter a word: ")
print(get_definition(word, dictionary))


#handling words not in the dictionary
def get_definition(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        return "Sorry, the word does not exist. Please check your spelling."


#handling upper, lower, or mixed case input
def get_definition(word, dictionary):
    word = word.lower()  # Ensure the word is treated case-insensitively
    if word in dictionary:
        return dictionary[word]
    else:
        return "Sorry, the word does not exist in the dictionary."



#suggest correct word spelling
import difflib


#implement word suggestion:
def get_definition(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        # Get close matches to the word
        close_matches = difflib.get_close_matches(word, dictionary.keys())
        if close_matches:
            suggestion = close_matches[0]
            return f"Did you mean '{suggestion}'? If yes, the definition is: {dictionary[suggestion]}"
        else:
            return "Sorry, the word does not exist and no close matches were found."
        

#add user interaction:
import json
import difflib

# Load the dictionary data
def load_dictionary():
    with open('data.json') as file:
        data = json.load(file)
    return data

# Function to get the word definition
def get_definition(word, dictionary):
    word = word.lower()  # Normalize input case
    if word in dictionary:
        return dictionary[word]
    else:
        # Suggest a close match if word not found
        close_matches = difflib.get_close_matches(word, dictionary.keys())
        if close_matches:
            suggestion = close_matches[0]
            return f"Did you mean '{suggestion}'? The definition is: {dictionary[suggestion]}"
        else:
            return "Sorry, the word does not exist in the dictionary and no close matches were found."

# Main program logic
if __name__ == "__main__":
    dictionary = load_dictionary()
    
    while True:
        word = input("Enter a word to search for (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        definition = get_definition(word, dictionary)
        print(definition)



