def signinout(logs, maxSpan):
    dictionary={}
    final=[]

    for i in range(0,n):
        [id,time,action]=logs[i].split(' ')
        if id not in dictionary:
            dictionary[id]=[int(time),action]
        else:
            obstime,obsaction=dictionary[id]
            if obsaction=='sign-in' and action=='sign-out':
                intime=int(time)-obstime
                if intime<=maxSpan:
                    final.append(id)
            elif obsaction=='sign-in' and action=='sign-in':
                intime=obstime-int(time)
                if intime<=maxSpan:
                    final.append(id)
    final.sort()
    return final



# def getUserIds(logs, maxSpan):
#     d = {}
#     res = []
#     for log in logs:
#         [user_id, timestamp, action] = log.split(' ')
#         if user_id not in d:
#             d[user_id] = [int(timestamp), action]
#         else:
#             recorded_time, recorded_action = d[user_id]
#             if recorded_action == 'sign-in' and action == 'sign-out':
#                 logged_time = int(timestamp) - recorded_time
#                 if logged_time <= maxSpan:
#                     res.append(user_id)
#             elif recorded_action == 'sign-out' and action == 'sign-in':
#                 logged_time = recorded_time - int(timestamp)
#                 if logged_time <= maxSpan:
#                     res.append(user_id)
#     res.sort()
#     res=list(map(str, res))
#     return res
n=7
logs=ogs = ["30 99 sign-in", "30 105 sign-out", "12 100 sign-in", "20 80 sign-in:", "12 120 sign-out","20 101 sign-out","21 110 sign-in"]
maxSpan=20
# print(getUserIds(logs,maxSpan))
print(signinout(logs,maxSpan))