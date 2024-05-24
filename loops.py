def index_of_by_index(word, list, index):
    for position, element in enumerate(list):
        if element == word and index <= position :
            return position
    else:
        return -1


colors = ["Red", "Green", "", "White", "Black"]
for position, element in enumerate(colors):
    print(f"{position}: {element}")





def index_of_empty(list):
    for position, element in enumerate(list):
        if element == "":
            return position
    else:
        return -1


def index_of(word, list):
    index= 0
    for element in list:
        if element == word:
            return index
        index += 1
    else:
            return -1



def put(word, list):
    for position, element in enumerate(list):
        if element == "":
            list[position] = word
            return position
    else:
        return -1



def remove(word, list):
    repetidos = 0
    for position, element in enumerate(list):
        if word==element:
            list[position] = ""
            repetidos += 1
    return repetidos
