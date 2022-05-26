names = []
with open("Input/Names/invited_names.txt", "r") as invited_names_file:
    for name in invited_names_file.readlines():
        i = name.replace("\n", "")
        names.append(i)


for name in names:
    with open("Input/Letters/starting_letter.txt", "r") as letter_folder:
        i = letter_folder.readline().replace("[name]", name)
        with open(f'Output/ReadyToSend/{name}_letter', 'w') as f:
            f.write(i + letter_folder.read())

