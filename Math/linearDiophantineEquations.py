"""
Solving a linear diophantine equation of two variables (ax+by=c), where a,b,c are integers.
Interesting properties are the following:
(1) c is a multiple of the gcd(a,b), where gcd is the greatest common denominator

Some more interesting things to do with these results would be to graph them.  

"""
def gcd(a,b):
    if not b:
        return a
    return gcd(b,a%b)

def solve(a, b, c):
    g = gcd(a,b)
    # The linear diophantine equation requires that c is a multiple of the gcd(a,b)
    assert(c%g==0)
    # arbitrary range, hopefully find a 2 solutions. 
    cnt = 0
    X = []
    Y = []
    for x in range(2000):
        y = (c-a*x) / b
        if y==int(y):
            cnt+=1
            X.append(x)
            Y.append(y)
        if cnt==2:
            break
    assert(len(X)==2 and len(Y)==2)
    u = X[1]-X[0]
    v = Y[1]-Y[0]
    # solutions will be x=X[0]+uk
    for k in range(10):
        print(solution(X[0], Y[0], u, v, k))
# x0, and y0 are the initial values
def solution(x0, y0, u, v, k):
    return (int(x0+u*k), int(y0+v*k))

if __name__ == '__main__':
    # 3x+9y=18
    # finding solution for k = [0,9]
    solve(3, 9, 18)