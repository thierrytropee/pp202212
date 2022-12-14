import sys,time

def checkPalindrome(s,i): 
    global longestPalindrom, longestPalindromPos

    # Which length do I want to check for a better palindrom ? 

    if i%1 == 0:
        if longestPalindrom%2 == 0:
            firstSearch = longestPalindrom + 1
        else:
            firstSearch = longestPalindrom + 2
    else:
        if longestPalindrom%2 == 0: 
            firstSearch = longestPalindrom + 2
        else:
            firstSearch = longestPalindrom + 1

    if i%1 == 0: # integer ? 
        p1 = i - int(firstSearch/2) 
        p2 = i + int(firstSearch/2) 
    else:
        p1 = i - int(firstSearch/2) + 0.5
        p2 = i + int(firstSearch/2) - 0.5

    p1 = int(p1)
    p2 = int(p2)

    # Is it possible to get this large a palindrom from the pivot ? 

    if p1 < 0 or p2 > len(s) - 1: # out of range, impossible to get better 
        return True
    
    if s[p1] != s[p2]: # different characters, so no palindrom 
        return True

    # Is the string inside p1 and p2 a palindrom 

    s1 = p1 + 1
    s2 = p2 - 1
    letsloop = True
    while (s2 > s1 and letsloop):
        if s[s1] != s[s2]:
            letsloop = False
        s1+=1 
        s2-=1
    
    if not letsloop: # Not a palindrom, so we leave 
        return True

    # This is the longest palindrom 

    longestPalindrom = firstSearch
    longestPalindromPos = i

    # But can I get a even longer palindrom ? 

    s1 = p1 - 1 
    s2 = p2 + 1 

    letsloop = True
    while (s1 >= 0 and s2 <= len(s) -1 and letsloop):
        if s[s1] == s[s2]:
            s1 -=1
            s2 +=1
            longestPalindrom += 2
        else:
            letsloop = False 

# 
# Main 
# 

myS = sys.stdin.readlines()[0].rstrip()

longestPalindromPos = 0
if len(myS)%2 == 0:
    midPoint = len(myS)/2 - 0.5
    longestPalindrom = 0
else: 
    midPoint = int(len(myS)/2)
    longestPalindrom = 1 

theStartTime=time.time()
if midPoint != 0:
    i = midPoint 
    while i > 0: # from middle to left 
        checkPalindrome(myS,i)
        i -= 0.5

    i = midPoint + 0.5
    while i < len(myS): # from middle to right 
        checkPalindrome(myS,i)
        i += 0.5
theEndTime=time.time()

if longestPalindrom > 1 or midPoint == 0: 
    if longestPalindromPos%1 == 0:
        fromP = int(longestPalindromPos - int(longestPalindrom/2))
    else:
        fromP = int(longestPalindromPos - longestPalindrom/2 + 1)
    print(myS[fromP:fromP+longestPalindrom])