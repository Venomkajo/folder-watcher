import os

def main():
    current_data = ''
    saved_data = ''

    current_directory = os.getcwd()

    files_in_current_directory = os.listdir(current_directory)

    # print files currently in directory
    print('\nFiles in current directory:\n')
    for item in files_in_current_directory:
        print(item)

    # if savefile.txt exists print it out and copy contents to saved_data
    if os.path.exists('savefile.txt'):
        print('\nSaved data:\n')
        with open('savefile.txt', 'r') as file:
            data = file.read()
            saved_data = data
            print(data)

    # overwrite or create the savefile.txt
    with open('savefile.txt', 'w') as file:
        for item in files_in_current_directory:
            file.write(item + '\n')

    # get the current_data
    with open('savefile.txt', 'r') as file:
        current_data = file.read()

    # if contents were modified print out the missing content
    if (current_data == saved_data):
        print('\nNo changes to files.\n')
    elif saved_data:
        print('\nFiles were modified.\n')
        print('\nModified files:\n')

        modified_files = get_modified_files(current_data, saved_data)

        for file in modified_files:
            print(file)

    # restart the program by typing R
    if input('\nProgram finished.\n').upper() == 'R':
        main()

    return 0

# compare file lists and return the differences
def get_modified_files(string1, string2):
    returnValues = []

    list1 = string1.split('\n')
    list2 = string2.split('\n')

    for i in range(len(list1)):
        if list1[i] not in list2:
            returnValues.append(list1[i])

    for i in range(len(list2)):
        if list2[i] not in list1:
            returnValues.append(list2[i])

    return returnValues

main()