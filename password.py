import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

length = int(input("Enter the length of the password: "))
print("Generated Password: ", generate_password(length))
Expected Output:
perl
Copy code
Enter the length of the password: 12
Generated Password:  mA1pLz#9nK!w
