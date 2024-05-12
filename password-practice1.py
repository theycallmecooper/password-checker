# assessment ...

password = input() #get password
print(len(password)) #will print the length of a string

#check if string contains a character
def check_for_exclamation(password):
    for character in password:
        if character == "!":
            return True

# isalpha() - checks if a string is alphanumeric
# isupper() - checks is a string is uppercase