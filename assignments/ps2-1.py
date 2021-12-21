# Problem Set 1
# Problem 1
# Nicole Wakeman
# Time: 12:34 2021-12-15
#
# McNugget Diophantine equation

#Show that it is possible to buy exactly 50, 51, 52, 53, 54, and 55
# McNuggets by combinations of 6, 9, and 20 packs, show that it is possible to buy 56, 57,...,65 McNuggets.  In other words, show how given solutions for 50-55, one can derive solutions for 56-65.

#First, just exploring the problem. 

def sigma(i):
    return list(range(0, i))

def gamma(i):
    #returns the set of all i-tuples whoes elements are
    #in sigma(i)
    gam = []
    sig = sigma(i)
    for a in sig:
        for b in sig:
            for c in sig:
                gam.append((a, b, c))
    return gam

def dot(x, y):
    #returns the dot product of to array like objects
    assert len(x) == len(y), "dot product is only defined for vecters of equal dimention"
    dim = len(x)
    ans = 0
    for i in range(dim):
        ans += x[i]*y[i]
    return ans

packages = (6, 9, 20)

def possible(i):
    # returns solutions, n, to 6a + 9b + 20c = n
    # for max{a,b,c} = i - 1
    ans = {}
    gam = gamma(i)
    for abc in gam:
        n = dot( (6, 9, 20), (abc) )
        if ans.get(n, "empty") == "empty":
            ans[n] = [abc]
        else:
            ans[n].append(abc)
    return ans
#print(possible(12))
res = possible(12)
#possible = list(res.keys())
#print(x)
#possible.sort()
#print(x)
#print(len(x))

### ANSWER FOR Problem 1. PART A
for i in range(50,56):
    print("n =", i, ":","(a,b,c) =", res[i])

### ANSWER FOR Problem 1. PART B/ PROBLEM 2
"""
50, 51, 52, 53, 54, and 55 are solutions to the 
McDiophentine equation, with each solution coresponding 
to at least one 3-tuple of the form, (6a, 9b, 20c). If 
(6a1, 9b1, 20c1) corresponds to n1, then replacing a1
with a1 + 1, will correspond to n1 + 6. So then if
n0 + 0, n0 + 1, n0 + 2,..., n0 + 5 are solutions, then
n0 + 6, n0 + 7, n0 + 8,..., n0 + 11 are solutions as well.

"""

# Problem 3
# Write an itterative program that finds the largest
# number of McNuggets that connot be bought in an exact quantity

# constrained version = for a given max number of packs

# Function to find first five in a row
# Takes a 1D arrary of arrbitrary length
def str8five(A):
    sequential = False
    l = len(A)
    print(l)
    for i in range(l):
        five = A[i:i + 5]
        print(list(five))
        # Test for sequential
        for j in range(1,5):
            #print(list(range(1,5)))
            print(five[j],five[j-1])
            if five[j] - five[j-1] == 1:
                print('true')
                sequential = True
            else:
                print('false')
                sequential = False
                break
        if sequential:
            print('five in a row at index', i, 'through', i+4)
            print('largest number not in set is', A[i] - 1)
            return A[i] - 1
        
A = range(20)
print('calling str8five')
#out = str8five(A)
possible = list(possible(4).keys())
possible.sort()
print(possible)
largestNonAnswer = str8five(possible)
#print(list(out))

