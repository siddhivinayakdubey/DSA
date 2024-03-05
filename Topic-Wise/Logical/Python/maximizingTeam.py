n=int(input())
m=int(input())
def canFormTeam(n, m):
    if (n >= 1 and m >= 2):
        return True
    if (m >= 1 and n >= 2):
        return True
    return False

def maxTeams(n, m):
    count = 0
    while (canFormTeam(n, m)):
        if (n > m):
            n -= 2
            m -= 1
        else:
            m -= 2
            n -= 1
        count += 1
    return count
print(maxTeams(n, m))


