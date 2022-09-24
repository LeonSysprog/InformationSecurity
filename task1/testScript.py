container = open("container.txt", 'rb+')
for text in container:
    text = list(text)
    print(text)

print('\n')

stegoContainer = open("stegoContainer.txt", 'rb+')
for text in stegoContainer:
    text = list(text)
    print(text)