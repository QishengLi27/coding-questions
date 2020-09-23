# Given a prefix and a documents, 
# find the index of each occurrence of the word start with the prefix.
# (case insensitive)

# documetn = "a aa Aa"
# prefix = 'aa'

# result: [2, 5]

#TODO: use Trie
def find_words_with_prefix(doc, prefix):
    res = []
    i = 0
    while i<len(a):
        if a[i].isalpha():
            j = i
            while a[j].isalpha() and j<len(a)-1:
                j+=1
            word = a[i:j+1].lower()
            if word.startswith(prefix.lower()):
                res.append(i)
            i=j+1
            print(word)
        else:
            i+=1

    return res

print(find_words_with_prefix('aaa bbb cccc Aa aa', 'aa')) #[0, 13, 16]