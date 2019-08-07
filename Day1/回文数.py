
def palindromes(sumnumber):
    total=0;
    num=sumnumber;
    while(num%10!=0):
        total=total*10+num%10
        num=num//10
    return True if total==sumnumber else False

print(palindromes(12321))