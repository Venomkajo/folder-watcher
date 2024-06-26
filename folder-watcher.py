import os

SAVE_FILE = 'savefile.txt'
TEMP_SAVE_FILE = 'tempsavefile.txt'

def folder_watcher():
    try:
        current_data = ''
        saved_data = ''
        argument = get_argument()

        current_directory = os.getcwd()
        files_in_current_directory = os.listdir(current_directory)

        # use functions based on the argument
        # compare the files and immediately overwrite the savefile
        if argument == 'A':
            print_files(files_in_current_directory)
            saved_data = read_savefile(SAVE_FILE)
            create_savefile(files_in_current_directory, SAVE_FILE)
            current_data = get_current(SAVE_FILE)
            print_modified(current_data, saved_data)
        # only overwrite the save file
        elif argument == 'W':
            create_savefile(files_in_current_directory, SAVE_FILE)
        # read the file without overwriting the save file, using a temp file to guarantee formatting
        elif argument == 'R':
            print_files(files_in_current_directory)
            saved_data = read_savefile(SAVE_FILE)
            create_savefile(files_in_current_directory, TEMP_SAVE_FILE)
            current_data = get_current(TEMP_SAVE_FILE)
            delete_file(TEMP_SAVE_FILE)
            print_modified(current_data, saved_data)
        else:
            print('Error! Invalid argument.')

        # restart the program by typing R
        if input('\nProgram finished. Press R to restart.\n').upper() == 'R':
            folder_watcher()

        return 0
    
    except Exception as e:
        print(f'\nAn error has occured: {e}\n')
        return 1

# get the argument
def get_argument():
    while True:
        argument = input('\nArguments: W-Write, R-Read, A-All\n').upper()
        if argument in ['W', 'R', 'A']:
            return argument

# print files currently in directory
def print_files(files_list):
    print('\nFiles in current directory:\n')
    for file in files_list:
        print(file)

# if savefile.txt exists print it out and copy contents to saved_data
def read_savefile(file_path):
    if os.path.exists(file_path):
        print('\nSaved data:\n')
        with open(file_path, 'r') as file:
            data = file.read()
            print(data)
            return data
    return ''
        
# overwrite or create the savefile
def create_savefile(files_list, file_path):
    with open(file_path, 'w') as file:
        for item in files_list:
            file.write(item + '\n')

# delete the temporary file
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

# get the current_data
def get_current(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return ''
    
# if contents were modified print out the missing content
def print_modified(current_data, saved_data):
    if (current_data == saved_data):
        print('\nNo changes to files.\n')
    elif saved_data:
        print('\nFiles were modified.\n')
        print('\nModified files:\n')

        modified_files = get_modified_files(current_data, saved_data)

        for file in modified_files:
            print(file)

# compare file lists and return the differences
def get_modified_files(string1, string2):
    return_values = []

    list1 = string1.split('\n')
    list2 = string2.split('\n')

    for item in list1:
        if item and item not in list2:
            return_values.append(item)

    for item in list2:
        if item and item not in list1:
            return_values.append(item)

    return return_values

folder_watcher()
