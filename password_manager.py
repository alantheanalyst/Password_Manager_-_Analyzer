import random
import string

# creates a function called password manager that generates a random password 
# and determines if it's strong or weak based on this criteria. 1 uppercase letter, 
# 1 lowercase letter, 1 numeric value, 1 special character, 
# and at least 8-12 characters
def password_manager():

# ensures that the generated password is between 8 and 12 characters
    length = random.randint(8, 12) 
    
# ensures that the generated password merges random uppercase and lowercase letters,
# numeric values, special characters, and a range of 8-12 characters.
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = length))

# uses the any function to loop over the generated password to check if it 
# includes uppercase and lowercase letters numeric values, special characters, 
# and is greater than or equal to 8 characters.   
    has_upper = any(i.isupper() for i in password)
    has_lower = any(i.islower() for i in password)
    has_numeric = any(i.isnumeric() for i in password)
    has_special = any(i in string.punctuation for i in password)
    has_length = len(password) >= 8
 
# returns the randomly generated password and it's length.
    print(password)
    print(length)
 
# returns strong password if all conditions are met and allows the user to add 
# the missing requirement if one or more of the conditions aren't met.
    if all([has_upper, has_lower, has_numeric, has_special, has_length]):
        return 'Strong password'
    elif not has_upper:
        return password + input('Password requires an uppercase letter: ')
    elif not has_lower:
        return password + input('Password requires a lowercase letter: ')
    elif not has_numeric:
        return password + input('Password requires a numeric value: ')
    elif not has_special:
        return password + input('Password needs a special character: ')
    elif not has_length:
        return 'Password is to short. Needs to be 8-12 characters'
    
print(password_manager())            