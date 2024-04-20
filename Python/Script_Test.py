filenames = ['document','report','presentention']

for index,item in enumerate(filenames):
    item = item.title()

    print(f"{index}-{item}.txt")