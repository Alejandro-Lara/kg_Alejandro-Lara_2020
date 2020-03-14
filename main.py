import sys

if(len(sys.argv) != 3):
    print('ERROR: This script requires exactly two arguments')
else:
     
    str1 = sys.argv[1]
    str2 = sys.argv[2]

    if len(str1) != len(str2):
        print('false');
    else:

        pairs = dict()
        oneToOne = True

        for i in range(len(str1)):
            if str1[i] not in pairs:
                pairs[str1[i]] = str2[i] #associate these two characters together
                
            elif pairs[str1[i]]!= str2[i]:
                    #if the character from str1 previously mapped to a different
                    #character in str2, then it's false
                    oneToOne = False
                    break
    
        if oneToOne:      
            print('true')
        else:
            print('false')
