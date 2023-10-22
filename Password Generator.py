import random
import string


def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    if length < 4:
        print("Length should be at least 4 to maintain complexity.")
        return


    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]


    for i in range(length - 4):
        password.append(random.choice(characters))


    random.shuffle(password)
    password = ''.join(password)

    return password


def main():
    try:
        length = int(input("Enter the desired password length:\n "))
        password = generate_password(length)

        if password:
            print(f"Generated Password: \n{password}")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
