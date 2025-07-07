# 7-7-25, Monday;
# File Handling.

# f = open("test.txt", "r")
# age = int(input("Enter your age: "))
# f.write(f"\nage: {age}")
# print("Data is written...")
# print(f.readlines())
# f.close()

# -------------------------------------------

# Implement the following:
# 1. add contact: name, email, number
# 2. view contacts
# 3. search contacts.

f = open("contact.txt", "a")
print("Add contact:")
name = input("Enter your name: ")
email = input("Enter your email: ")
number = input("Enter your number: ")
f.write(f"\nName: {name} Email: {email} Number: {number}")
print("Data is written...")
f.close()

f = open("contact.txt", "r")
print("View contacts:")
print(f.read())
f.close()

# Search contact based on the name:
# f = open("contact.txt", "r+")
# print("Search contacts:")
# search = input("Enter your name: ")
# f.seek(0)
# print(f.read().find(search))
# f.close()

# Search contact by name (GPT logic.)
with open("contact.txt", "r") as f:
    print("\nSearch contacts:")
    search = input("Enter your name: ").strip()
    lines = [line.strip() for line in f.readlines() if line.strip()]  # remove empty lines

    found = False
    for i in range(len(lines)):
        if lines[i].lower().startswith("name:") and search.lower() in lines[i].lower():
            print("\nContact found:")
            print(lines[i])                      # Name
            if i + 1 < len(lines): print(lines[i + 1])  # Email
            if i + 2 < len(lines): print(lines[i + 2])  # Number
            found = True
            break

    if not found:
        print("Contact not found.")
