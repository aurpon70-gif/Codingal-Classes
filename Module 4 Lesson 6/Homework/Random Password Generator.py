import random
import string

def generate_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    
    all_characters = lower + upper + digits
    
    
    password_list = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    
    
    for _ in range(length - 3):
        password_list.append(random.choice(all_characters))
        
    
    random.shuffle(password_list)
    
    
    password = "".join(password_list)
    return password


print("Generated Password:", generate_password(10))