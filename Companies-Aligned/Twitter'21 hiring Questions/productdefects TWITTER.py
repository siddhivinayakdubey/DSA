def LargestArea(samples):
 T = [[0 for x in range (len (samples [0]))] for y in range(len (samples))]

 max = 0
 for i in range (len(samples)):
  for j in range(len (samples [0])):

   T[i][j] = samples[i][j]

   if i > 0 and j > 0 and samples[i][j] ==1:


    T[i][j] = min(T[i][j - 1], T[i - 1][j], T[i - 1][j - 1]) + 1



   if max < T[i][j]:

    max = T[i][j]



 return max

samples=[[0,1,1],[1,1,0],[1,0,1]]
print(LargestArea(samples))