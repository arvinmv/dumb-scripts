import os
import tabulate

use_current_directory = input('Do you want to use the current working directory? (Y/N) ')

if use_current_directory.upper() == 'Y':
    directory = os.getcwd()
else:
    directory = input('Enter the directory path: ')
    directory = os.path.abspath(directory)

all_files = [] 
for root, directories, files in os.walk(directory):
    for file in files:
        all_files.append(os.path.join(root, file))

extensions = {}
for file in all_files:
    extension = os.path.splitext(file)[1]
    if extension == '':
        extension = 'no-extension'
    if extension not in extensions:
        extensions[extension] = 1
    else:
        extensions[extension] += 1

print('Number of files for each extension:')
print(tabulate.tabulate(extensions.items(), headers=['Extension', 'Count']))