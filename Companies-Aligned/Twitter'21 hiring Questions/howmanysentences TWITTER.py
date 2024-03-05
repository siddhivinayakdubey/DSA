def countSentences(wordSet, sentences):
    # first of all sort each w and r every w
    d = {}
    for k in wordSet:
        k = "".join(sorted(k))
        if k in d:
            d[k] = 1 + d[k]
        else:
            d[k] = 1
    array = []
    # for every sentence
    for j in sentences:
        w = j.split(' ')
        r = 0
        for k in w:
            k = "".join(sorted(k))
            if k in d and d[k] > 1:
                r = r + d[k]
        array.append(r)

    return array

wordSet={'listen','silent','it','is'}
sentences='listen it is silent'
print(countSentences(wordSet,sentences))

# word = []
# sentences = []
# n = int(input())
# for i in range(n):
#     str = input()
#     word.append(str)
# m = int(input())
# for i in range(m):
#     str = input()
#     sentences.append(str)
#
# arr = countSentences(word, sentences)
# for i in arr:
#     print(i)
