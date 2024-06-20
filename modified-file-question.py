import os

current_data = ''
saved_data = ''

current_directory = os.getcwd()

files_in_current_directory = os.listdir(current_directory)

print('\nFiles in current directory:\n')
for item in files_in_current_directory:
    print(item)

if os.path.exists('savefile.txt'):
    print('\nSaved data:\n')
    with open('savefile.txt', 'r') as file:
        data = file.read()
        saved_data = data
        print(data)

with open('savefile.txt', 'w') as file:
    for item in files_in_current_directory:
        file.write(item + '\n')

with open('savefile.txt', 'r') as file:
    current_data = file.read()

if (current_data == saved_data):
    print('\nNo changes to files.\n')
else:
    print('\nFiles were modified.\n')

input('Program finished.')
