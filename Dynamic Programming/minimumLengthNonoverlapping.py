'''Given you an array boxes and a target. Boxes[i] means that there are boxes[i] pens in the ith box. Subarray [i, j] is valid if sum(boxes[i] + boxes[i+1] + ... + boxes[j]) == target. Please find two not overlapped valid subarrays and let the total length of the two subarrays minimum. Return the minimum length. If you can not find such two subarrays, return -1.

______  ____
    _____
    


hashmap
{0: -1}
ans = inf
best = [inf]*len(arr)
iterate through prefix sum array:
  if current_value - target in hashmap:
    left = hashmap[current_value - target]
    if right > -1:
    

best=[inf,2,2,1]

[1,2,2,1,1,1] 3
= [1,3,5,6,7,8]

best[1] = 2 [1, 2]
ans = inf
indexMap = {1: 0, 3: 1, 5: 2, 6: 3, 7: 4, 8: 5}
ans = min(ans, current_idx - indexMap[current_val - target] + best[-1])

current_length < best[-1]:
  best[current_idx] = current_length
else:
  best[current_idx] = best[-1]
  
best = [inf, 2,1,1,1]

[1,2,3,1,1,1]
   i j
  (2) 
[INF,2,1,1,1]
target = 6
[1,1,1,2,2,2,4,4]  ans = 6
        3<-|--> 2
best = [inf, inf, inf, inf, 4, 3, 2, 2]


{0:1}
i = 1
v = 3
v-target = 0


for i, v in enumerate([1,3,6,7,8,9]):
                      
[1,2,3,1,1,1]  sum = 3  [2] ans = 3   [1]
     lr
       LR        sum = 2  [1]

best = [inf,2,1,1,1]     the min subarray s[0:i]
                         the min subarray s[i+1:-1]
best_backwards = [1,1,1,3,inf,inf]   the min subarray s[-1:i+1]

[1,2,3,1,1,1] 

[1,1,1,1,3,2] 
           lr
for i -> len(best)-1:
  ans = min(ans, best[i]+best_backward[i+1])
   
           
ans = min(ans, end_index - i + best[-1])
"""



