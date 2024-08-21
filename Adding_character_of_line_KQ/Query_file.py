# Specify the file name
file_name = 'List_of_node.txt'

# The word you want to add
word_to_add_before ='\''
word_to_add ='\','

# Open the file and read its contents
with open(file_name, 'r') as file:
    lines = file.readlines()

# Modify each line
modified_lines = [word_to_add_before + line.strip() + '' + word_to_add + '\n' for line in lines]

# Write the modified lines back to the file
with open(file_name, 'w') as file:
    file.writelines(modified_lines)

print("Word added to each line successfully!")
