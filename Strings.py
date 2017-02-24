
def reverse_sentace(str):
    revStr = ""
    for i in range(len(str)-1, -1, -1):
        revStr = revStr + str[i]
    return revStr

def reverse_sentace_native(str):
    arr = list(str)
    arr.reverse()
    return "".join(arr)

TST = "Some sentace for reversing!"

print("Original sentance   - ", TST)
print("Reversed sentance   - ",reverse_sentace(TST))
print("Reversed sentance 2 - ",reverse_sentace_native(TST))

# last elemnt in the range is not included and that is why we need -1 as the range end so we can get 0
#print(list(range(10,-1,-1)))