import emoji

x = input("Input: ")

try:
    x = emoji.emojize(x)
except ValueError:
    pass
else:
    x = emoji.emojize(x, language = "alias")

print(x)
