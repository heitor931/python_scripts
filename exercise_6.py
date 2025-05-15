user_input = input("Enter your phrase: ")

phrases = user_input.split(" ")

new_phrase = []
for f in phrases:
    new_phrase.append(f[::-1])
print(",".join(new_phrase).replace(",", " "))