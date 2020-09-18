/*
The implementation a sliding window algorithm.  This solves a specific problem but the overall idea remains true
That you need some type of condition that you will move the left side unti lthe condition is satisfied and then so on.  Can be 
modified for your specific problem. 
*/

func lengthOfLongestSubstring(s string) int {
    count_chars:=make(map[byte]int)
    counter:=0
    left:=0
    right:=0
    best:=0
    // Iterate until end of string and increment counter when the character is already in the hashmap.
    for right<len(s) {
        ch:=s[right]
        if cnt,found:=count_chars[ch]; found {
            if cnt==1 {
                counter+=1
            }
            count_chars[ch]=count_chars[ch]+1
        } else {
            count_chars[ch]=1
        }
        // The counter is the number of numbers that are repeated in the string.  We want to move the left pointer
        // until there are 0 repeated characters in the string.  
        for counter > 0 {
            if cnt,found:=count_chars[s[left]]; found {
                if cnt==2 {
                    counter-=1
                    count_chars[s[left]]=count_chars[s[left]]-1
                } else if cnt==1 {
                    delete(count_chars,s[left])
                } else {
                    count_chars[s[left]]=count_chars[s[left]]-1
                }
                
            }
            left+=1
        }
        best=Max(best,right-left+1)
        right+=1
    }
    return best
}

func Max(x,y int) int {
    if x < y {
        return y
    }
    return x
}