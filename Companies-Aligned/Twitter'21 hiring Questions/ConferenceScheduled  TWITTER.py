# class meeting:
#
#     def __init__(self, start, end, pos):
#         self.start = start
#         self.end = end
#         self.pos = pos
#
#
# # Function for finding maximum
# # meeting in one room
# def maxMeeting(l, n):
#     # Initialising an arraylist
#     # for storing answer
#     ans = []
#
#     # Sorting of meeting according to
#     # their finish time.
#     l.sort(key=lambda x: x.end)
#
#     # Initially select first meeting
#     ans.append(l[0].pos)
#
#     # time_limit to check whether new
#     # meeting can be conducted or not.
#     time_limit = l[0].end
#
#     # Check for all meeting whether it
#     # can be selected or not.
#     for i in range(1, n):
#         if l[i].start > time_limit:
#             ans.append(l[i].pos)
#             time_limit = l[i].end
#
#     # Print final selected meetings
#
#     print(len(ans))
#
#     print()
#
#
# # Driver code
# if __name__ == '__main__':
#
#     # Starting time
#     s = [1,3,3,5,7]
#
#     # Finish time
#     f = [2,2,1,2,1]
#
#     # Number of meetings.
#     n = len(s)
#
#     l = []
#
#     for i in range(n):
#         # Creating object of meeting
#         # and adding in the list
#         l.append(meeting(s[i], f[i], i))
#
#     # Function call
#     maxMeeting(l, n)




def universityCareerFair(arrival, duration):
    aux = sorted(
        list(zip(arrival, duration)),
        key=lambda p: (sum(p), p[1])
    )
    ans, end = 0, -float('inf')
    for arr, dur in aux:
        if arr >= end:
            ans, end = ans + 1, arr + dur
    return ans

s = [1,3,5]

    # Finish time
f = [2,2,2]

print(universityCareerFair(s,f))