with open("./Input/Letters/starting_letter.txt") as letter_file:
    content = letter_file.read()

with open("./Input/Names/invited_names.txt") as namesFile:
    names = namesFile.readlines()

for name in names:
    name = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{name}", mode='w') as letter_for_person_file:
        letter_for_person_file.write(content.replace("[name]", name))
