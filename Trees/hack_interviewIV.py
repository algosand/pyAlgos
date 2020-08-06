# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'performOperations' function below.
# #
# # The function is expected to return a LONG_INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. INTEGER N
# #  2. INTEGER_ARRAY op
# #

# def performOperations(N, op):
#     arr = [i for i in range(1, N + 1)]
#     elemPresent = set(arr)
#     res = sum(arr)
#     ans = []
#     for oper in op:
#         if oper in elemPresent:
#             arr[0], arr[-1] = arr[-1], arr[0]
#         else:
#             elemPresent.remove(arr[-1])
#             elemPresent.add(oper)
#             res = res - arr[-1] + oper 
#             arr[-1] = oper
#         print(arr)
#         ans.append(res)
#         # print(res)
#     return ans
            
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     N, M = map(int, input().split())

#     op = []
#     for _ in range(M):
#         op.append(int(input()))
#     result = performOperations(N, op)


#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()


# if __name__ == '__main__':

#     N, M = map(int, input().split())

#     op = []
#     for _ in range(M):
#         op.append(int(input()))
#     result = performOperations(N, op)


#     res = ('\n'.join(map(str, result)))
#     print(res)


# import java.io.*;
# import java.math.*;
# import java.security.*;
# import java.text.*;
# import java.util.*;
# import java.util.concurrent.*;
# import java.util.function.*;
# import java.util.regex.*;
# import java.util.stream.*;
# import static java.util.stream.Collectors.joining;
# import static java.util.stream.Collectors.toList;

# class Result {

#     /*
#      * Complete the 'performOperations' function below.
#      *
#      * The function is expected to return a LONG_INTEGER_ARRAY.
#      * The function accepts following parameters:
#      *  1. INTEGER N
#      *  2. INTEGER_ARRAY op
#      */

#     public static List<Long> performOperations(int N, List<Integer> op) {
#         HashSet<Long> contained = new HashSet<>();
#         List<Long> arr = new ArrayList<Long>();
#         long sum = 0;
#         for (long i = 1; i <= N; i++) {
#             sum = sum + i;
#             arr.add(i);
#             contained.add(i);
#         }
#         List<Long> ans = new ArrayList<Long>();
        
#         for (long val : op) {
#             if (contained.contains(val)) {
#                 Collections.swap(arr, 0, N - 1);
#             } else {
#                 long lastElem = arr.get(N - 1);
#                 sum = sum - lastElem + val;
#                 contained.remove(lastElem);
#                 contained.add(val);
#                 arr.remove(N - 1);
#                 arr.add(val);
#             }
#             ans.add(sum);
#         }
#         return ans;
#     }

# }

# public class Solution {
#     public static void main(String[] args) throws IOException {
#         BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
#         BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        
#         String str = bufferedReader.readLine();
#         // String[] sa = new String[str.length()];
#         String[] sa = str.split(" ");
        
#         int N = Integer.parseInt(sa[0]);
#         int M = Integer.parseInt(sa[1]);
        
#         List<Integer> op = new ArrayList<Integer>();
#         for (int i = 0; i < M; i++){
#             int v = Integer.parseInt(bufferedReader.readLine());
#             op.add(v);
#         }
        

#         List<Long> result = Result.performOperations(N, op);
        
#         bufferedWriter.write(
#             result.stream()
#                 .map(Object::toString)
#                 .collect(joining("\n"))
#             + "\n"
#         );

#         bufferedReader.close();
#         bufferedWriter.close();
#     }
# }

import math
import os
import random
import re
import sys

#
# Complete the 'countCups' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY balls
#  3. 2D_INTEGER_ARRAY swaps
#  4. 2D_INTEGER_ARRAY queries
#

class SegTree:
    def __init__(self, arr, n):
        self.m = 2**math.ceil(math.log2(n))
        self.arr = arr
        self.n = n
        self.tree = [0]*2*self.m
        self.build()
        
    def build(self):
        for i in range(self.n):
            self.tree[i + self.m] = self.arr[i]
        for i in range(self.m - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
        
    def update(self, a, b):
        am = a - 1 + self.m
        bm = b - 1 + self.m
        self.tree[am], self.tree[bm] = self.tree[bm], self.tree[am]
        
        i, j = am, bm
        while i > 1 or j > 1:
            if i > j:
                self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
                i >>= 1
            else:
                self.tree[j >> 1] = self.tree[j] + self.tree[j ^ 1]
                j >>= 1
    
    def query(self, l, r):
        l -= 1
        l += self.m
        r += self.m
        res = 0
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
            
        return res

def countCups(n, balls, swaps, queries):
    arr = []
    balls = set(balls)
    for i in range(n):
        if i + 1 in balls:
            arr.append(1)
            continue
        arr.append(0)
    st = SegTree(arr, n)
    for a, b in swaps:
        st.update(a, b)
    res = []
    for l, r in queries:
        res.append(st.query(l, r))
    return res
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    q = int(first_multiple_input[3])

    balls = list(map(int, input().rstrip().split()))

    swaps = []

    for _ in range(s):
        swaps.append(list(map(int, input().rstrip().split())))

    query = []

    for _ in range(q):
        query.append(list(map(int, input().rstrip().split())))

    result = countCups(n, balls, swaps, query)
    print(" ".join(map(str, result)))

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

