#First example of string manipulation with external input

def who_do_you_know():
    people = input("Enter the names of people you know, spearated by commas: ")
    people_without_spaces = [person.strip() for person in people.split(",")]   
        
    return people_without_spaces

def ask_user():
    person = input("Enter Name of a person you Know: ")
    if person in who_do_you_know():
        print(" YOU Know {}!".format(person))

ask_user()

