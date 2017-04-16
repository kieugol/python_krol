def breaking(stuff):
    words = stuff.split(' ')
    return words

def sorting(words):
    return sorted(words)

def sort_all(sentence):
    words = breaking(sentence)
    return sorting(words)

sentence = " xx cc abc def"
result = sort_all(sentence)
print(result)