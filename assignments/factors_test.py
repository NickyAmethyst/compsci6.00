factors = range(1, 10)
ints = list(range(0, 20))

# print(ints)

# multiples = list(range(0, 20, 2))
# print(multiples)

print(ints)
for i in factors:
    multiples = list(range(0, 20, i))
    for j in multiples:
        x = []
        for k in ints:
            
            if j != k:
                x.append(0)
            else:
                x.append(multiples[j])
        print(x)