def getLargestString(s, k):
    freqarr = [0] * 26
    for i in range(len(s)):
        freqarr[ord(s[i]) -
                        ord('a')] += 1
    ans = ""
    i = 25
    while i >= 0:
        if (freqarr[i] > k):
            temp = k
            st = chr(i + ord('a'))

            while (temp > 0):

                ans += st
                temp -= 1

            freqarr[i] -= k

            j = i - 1

            while (freqarr[j] <= 0 and
                   j >= 0):
                j -= 1

            if (freqarr[j] > 0 and
                    j >= 0):
                str1 = chr(j + ord('a'))
                ans += str1
                freqarr[j] -= 1
            else:

                break

        elif (freqarr[i] > 0):

            temp = freqarr[i]
            freqarr[i] -= temp
            st = chr(i + ord('a'))
            while (temp > 0):
                ans += st
                temp -= 1
        else:
            i -= 1

    return ans