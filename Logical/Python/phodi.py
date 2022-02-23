text = input()
new_text = ''

for i, letter in enumerate(text):
    if i and letter.isupper():
        new_text += ' '

    new_text += letter
    new_text=new_text.lower()

print(new_text)