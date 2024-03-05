#### Removed Plagarism
def bracket_match(text):
    count = 0
    final = 0
    n=len(text)
    for i in range(0,n):
        if text[i]=='(':
            count+=1
        else:
            if count >0:
                count-=1
            else:
                final+=1
    return final+count






####Main Code
# def bracket_match(text):
#     left_cnt = 0
#     ans = 0
#     for c in text:
#         if c == "(":
#             left_cnt += 1
#         else:
#             if left_cnt > 0:
#                 left_cnt -= 1
#             else:
#                 ans += 1
#
#     return ans + left_cnt