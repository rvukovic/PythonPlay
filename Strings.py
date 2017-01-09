
def reverse_sentace(str):
    revStr = ""
    for i in range(len(str)-1, -1, -1):
        revStr = revStr + str[i]
    return revStr


TST = "Some stentacne for reversing!"

print("Original sentance - ", TST)
print("Reversed sentance - ",reverse_sentace(TST))

# last elemnt in the range is not included and that is why we need -1 as the range end so we can get 0
#print(list(range(10,-1,-1)))