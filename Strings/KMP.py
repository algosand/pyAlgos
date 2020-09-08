"""
Implementation of KMP algorithm: 
https://www.youtube.com/watch?v=iZ93Unvxwtw&feature=youtu.be
avoids backup
deterministic finite state machine
"""
def prefix_array(self,w):
	n=len(w)
	prefArray=[0]*n
	length=0
	for i,ch in enumerate(w):
		if ch==w[length]:
			length+=1
			prefArray[i]=length
		else:
			if length!=0:
				length=prefArray[length-1]
				i-=1
			else:
				prefArray[i]=0
	return prefArray

def kmp(self,s,w):
	"""
	s -> string
	w -> substring
	"""
	prefArray=self.prefix_array(w)
	i,j=0,1
	n,m=len(s),len(w)
	while i<n:
		if s[i]==w[j]:
			i+=1
			j+=1
		if j==m:
			print(i-j)
		elif i<n and w[j]!=s[i]:
			if j!=0:
				j=prefArray[j-1]
			else:
				i+=1


"""
KMP algorithm for finding if a substring repeats in a string, the substring that you want to match will be the substring
at beginning of string. 
https://leetcode.com/problems/repeated-substring-pattern/
"""
class Solution:
    def repeatedSubstringPattern(self, s):
        n=len(s)
        pattern=[0]*n
        # start the substring as first character in string
        i,idx=1,0
        while i<n:
            if s[i]==s[idx]:
                idx+=1
                pattern[i]=idx
                i+=1
            else:
                if idx>0:
                    idx=pattern[idx-1]
                else:
                    i+=1
        return True if pattern[-1] and pattern[-1]%(n-pattern[-1])==0 else False

"""
"""