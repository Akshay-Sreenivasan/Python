# def create():
#     f=open('file1.txt','x')
# def read():
#     p=open('file1.txt',"r")
#     print(p.read())
# def add():
#     w = open("file1.txt", "a")
#     w.write("\nNow the file has more content!")
#     w.close()

# while True:
#     print('Select from the list')
#     print('1).Create file')
#     print('2).Add Content')
#     print('3).Read file')
#     print('6).Exit')
#     print(' ')
#     n=int(input('Enter the choice: '))
#     if n==1:
#         create()
#     elif n==2:
#         add()
#     elif n==3:
#         read()
#         print('\n')
#     elif n==6:
#         print('****Exiting from the menu****')
#         break



import os
def create_file(filename):
    try:
        with open(filename, 'w') as file:
            print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Content written to '{filename}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

def append_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write('\n',content)
            print(f"Content appended to '{filename}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

def delete_file(filename):
    os.remove(filename)

while True:
    print("\nMenu:")
    print("1. Create a new file")
    print("2. Read a file")
    print("3. Write to a file")
    print("4. Append to a file")
    print("5. Delete a file")
    print("6. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        filename = input("Enter the filename to create: ")
        create_file(filename)
    elif choice == '2':
        filename = input("Enter the filename to read: ")
        read_file(filename)
    elif choice == '3':
        filename = input("Enter the filename to write to: ")
        content = input("Enter the content to write: ")
        write_to_file(filename, content)
    elif choice == '4':
        filename = input("Enter the filename to append to: ")
        content = input("Enter the content to append: ")
        append_to_file(filename, content)
    elif choice == '5':
        filename = input("Enter the filename to be deleted: ")
        delete_file(filename)
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
