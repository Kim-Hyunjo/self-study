import sys
a= input()

A_Index = list(filter(lambda x: a[x] == 'A', range(len(a))))

if A_Index[0] < 2:
        print('NP')
        sys.exit()

for i in A_Index:
    try:
        if a[i-2] and a[i-1] and a[i+1] == 'P':
            indexes= [i-2, i-1, i]
            a= "".join([char for idx, char in enumerate(a) if idx not in indexes])
            print(a)
        else:
            print('NP')
            sys.exit()
    except IndexError:
        print('NP')
        sys.exit()
        
if a == 'P':
    print('PPAP')
else:
    print('NP')
