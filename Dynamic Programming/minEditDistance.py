"""
Implementation of minimum edit distance dp table for a problem.
Top down approach for dp table. 
"""

def solve(source, target):
  s, t = len(source), len(target)
  dp = [[0]*(s+1) for _ in range(t+ 1)]
  # Represents the minimum number of edits necessary. 
  for i in range(t + 1):
  	dp[i][0] = i
  for j in range(s + 1):
  	dp[0][j] = j
  for i in range(t + 1):
    for j in range(s + 1):
      if i < t and j < s and target[i] == source[j]:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
  ans = []
  i, j = 0, 0
  while i < t and j < s:
    if target[i] == source[j]:
      ans.append(target[i])
      i += 1
      j += 1
    else:
      if dp[i+1][j] >= dp[i][j+1]:
        ans.append('-' + source[j])
        j += 1
      else:
        ans.append('+' + target[i])
        i += 1
  while i < t:
    ans.append('+' + target[i])
    i += 1
  return ans


"""
Bottom up approach for the table. 
"""

"""
def diffBetweenTwoStrings(source, target):
  s, t = len(source), len(target)
  dp = [[0]*(s+1) for _ in range(t+ 1)]
  # Represents the minimum number of edits necessary. 
  for j in range(s + 1):
    dp[t][j] = s - j
  for i in range(t + 1):
    dp[i][s] = t - i
  for i in range(t - 1, -1, -1):
    for j in range(s - 1, -1, -1):
      if target[i] == source[j]:
        dp[i][j] = dp[i+1][j+1]
      else:
        dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1])
  ans = []
  i, j = 0, 0
  while i < t and j < s:
    if target[i] == source[j]:
      ans.append(target[i])
      i += 1
      j += 1
    else:
      if dp[i][j+1] <= dp[i+1][j]:
        ans.append('-' + source[j])
        j += 1
      else:
        ans.append('+' + target[i])
        i += 1
  while i < t:
    ans.append('+' + target[i])
    i += 1
  return ans

"""





if __name__ == '__main__':
	# source = "ABCDEFG"
	# target = "ABDFFGH"
	# print(solve(source, target))
	source = "CBBC"
	target = "CABAABBC"
	print(solve(source, target))