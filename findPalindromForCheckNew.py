import sys,time

def checkPalindrome(s,i,direction): 
    global longestPalindrom, longestPalindromPos

    # Which length do I want to check for a better palindrom ? 
    
    if direction == 'right':
        if i%1 == 0:
            if longestPalindrom%2 == 0:
                lengthToSearch = longestPalindrom + 1
            else:
                lengthToSearch = longestPalindrom + 2
        else:
            if longestPalindrom%2 == 0: 
                lengthToSearch = longestPalindrom + 2
            else:
                lengthToSearch = longestPalindrom + 1
    else: 
        lengthToSearch = longestPalindrom
        if i%1 == 0:  # 真ん中
            if lengthToSearch == 0:
                lengthToSearch = 3
            else:
                if longestPalindrom%2 == 0: # The previous palidrom was found on a 間
                    lengthToSearch += 1 
        else:
            if lengthToSearch == 0:
                lengthToSearch = 2 
            else: 
                if longestPalindrom%2 != 0: # The previous palidrom was found on a integer, we are now in the 間
                    lengthToSearch +=1 

    if i%1 == 0: # integer ? 
        if lengthToSearch == 0: # to manage the first searches until we get a first palindrom
            p1 = i - 1
            p2 = i + 1 
        else:          
            p1 = i - int(lengthToSearch/2) 
            p2 = i + int(lengthToSearch/2) 
    else:
        p1 = i - int(lengthToSearch/2) + 0.5
        p2 = i + int(lengthToSearch/2) - 0.5

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

    longestPalindrom = lengthToSearch
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
#myS = '12214334'
#myS = '43343321'
print('myS:',myS)

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
        checkPalindrome(myS,i,'left')
        i -= 0.5

    i = midPoint + 0.5
    while i < len(myS): # from middle to right 
        checkPalindrome(myS,i,'right')
        i += 0.5
theEndTime=time.time()

if longestPalindrom > 1 or midPoint == 0: 
    if longestPalindromPos%1 == 0:
        fromP = int(longestPalindromPos - int(longestPalindrom/2))
    else:
        fromP = int(longestPalindromPos - longestPalindrom/2 + 1)
    #print(myS[fromP:fromP+longestPalindrom])
    print('My answer is:',myS[fromP:fromP+longestPalindrom])
    print('This palindrom was found from position',fromP,'with a pivot',longestPalindromPos,'for a length of',longestPalindrom)
    print('The length of the initial string was ',len(myS),' and the answer was found in' ,theEndTime - theStartTime)