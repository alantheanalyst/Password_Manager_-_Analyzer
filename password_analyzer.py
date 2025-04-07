import string 

# Creates a function that checks the strenght of a password based on this criteria
# includes 1 uppercase letter, 1 lowercase letter, 1 numeric value, 1 special character,
# and is 8 characters or more
def password_analyzer():

# The while loop continues iterating over the function until all conditions are met
    while True:
# takes password as user input
        password = input('Please enter a password. Must include, 1 uppercase, 1 lowercase, 1 numeric value, 1 special character, and be at least 8-12 characters long: ')

# uses the any function to loop over the generated password to check if it 
# includes uppercase and lowercase letters numeric values, special characters, 
# and is greater than or equal to 8 characters.  
        has_upper = any(i.isupper() for i in password)
        has_lower = any(i.islower() for i in password)
        has_numeric = any(i.isnumeric() for i in password)
        has_special = any(i in string.punctuation for i in password)
        has_length = len(password) >= 8

# Returns Strong password if all conditions are met, tells the user the missing requirement, 
# and tells the user to create a password until all conditions are met.
        if all([has_upper, has_lower, has_numeric, has_special, has_length]):
            return 'Strong password'
        if not has_upper:
            print('Password requires an uppercase letter')
        if not has_lower:
            print('Password requires a lowercase letter')
        if not has_numeric:
            print('Password requires a numeric value')
        if not has_special:
            print('Password needs a special character')
        if not has_length:
            print('Password is to short. Needs to be 8-12 characters')
    
print(password_analyzer())