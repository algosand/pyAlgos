"""
1520. Maximum Number of Non-Overlapping Substrings (Leetcode)
"""
from collections import Counter
class Solution:
    def maxNumOfSubstrings(self, s):
        counter = Counter(s)
        n = len(s)
        sub = []
        for i in range(n):
            tempCounter = Counter()
            finished = set()
            for j in range(i, n):
                char = s[j]
                tempCounter[char] += 1
                flag = True
                for c in tempCounter:
                    if c not in finished:
                        if tempCounter[c] != counter[c]:
                            flag = False
                            continue
                        finished.add(c)
                if flag:
                    sub.append(s[i:j+1])
        sub.sort(key=lambda x: len(x))
        ans = []
        seen = set()
        for string in sub:
            next = True
            for c in counter:
                if c not in string:
                    continue
                if c in seen:
                    next = False
                    break
            if next:
                for c in counter:
                    if c not in string:
                        continue
                    seen.add(c)
                ans.append(string)
        return ans



if __name__ == '__main__':
	sol = Solution()
	s = "pthcbsfxaeyeduoilykmojihgysmytnmrtptxttdrkmtwblvnshvqbefmljuwwsgkrcmxhurpcuavcbvklejoriebyipsrclibavwonuznvwapqpjenefgxxipppiexsemnzquphveygjgvkdrocqotdhsdpnqyhiaednfkmuuyamykvpfbquksybgpyerhvedxztsbcblripsiaigzuxpqqwlaufmrmhknbkwkcgbvmfuwmpigjmialshktarkjaqvogsponotnhxvbznbajbeuovjgabnvbmfrkxgwbezydhvtdpvwrzpgfzrsxzsxutivdtqwybqvackrkbdhdczxwkjkyuztffmhuwrmzradoukvqjlbtwhbilaoicjsorzvdsvazdsi"
	print(sol.maxNumOfSubstrings(s))