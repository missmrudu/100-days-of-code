
names = []
with open('./invited_names.txt', "r") as name_file:
    for line in name_file.readlines():
        names.append(line.strip())

with open('./starting_letter.txt') as letter_file:
    starting_letter = letter_file.read()

for name in names:
    personalized_letter = starting_letter.replace("[name]", name)
    with open(f'{name}_invite.txt', "w") as output_file:
        output_file.write(personalized_letter)
