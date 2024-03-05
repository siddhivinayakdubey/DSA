from collections import Counter
def minDeletions(s):
    ans= 0
    letters = list(s)
    c = Counter(letters)
    freq=list(c.values())
    freq.sort(reverse=True)
    m=max(freq)
    f=Counter(freq)

    for i in range(m, 0, -1):
        if f[i] > 0:
            ans += f[i] - 1
            f[i - 1] += f[i] - 1
    return ans

