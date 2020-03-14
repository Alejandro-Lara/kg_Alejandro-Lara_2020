import sys

str1 = sys.argv[1]
str2 = sys.argv[2]

if len(str1) != len(str2):
    print('false');
else:

    pairs = dict()

    for i in range(len(str1)):
        if str1[i] not in pairs:
            pairs[str1[i]] = str2[i] #associate these two characters together
        else:
            if pairs[str1[i]]!= str2[i]:
                #if the same character from str1 maps to multiple and different
                #characters in str2, then fail
                print('false')
                exit()
            
    print('true')
