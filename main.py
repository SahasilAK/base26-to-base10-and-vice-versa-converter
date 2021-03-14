def base10_valueGenerator(input_string,data):
    val = [data[i] for i in input_string]
    base10_value = sum(val[i]*26**(len(val)-i-1) for i in range(0,len(val)))
    return base10_value


def base26_valueGenerator(d1,data):
    run = True
    quo = d1
    base26_val = ''
    while run:
        rem = quo%26
        quo = int(quo/26)
        x = list(data.keys())[list(data.values()).index(rem)]
        base26_val = x + base26_val
        if quo in data.values():
            x = list(data.keys())[list(data.values()).index(quo)]
            base26_val = x + base26_val
            run = False
    return base26_val


def start_con():
    user_input = input('Enter choice: \n1-Base26 to Base10  \n2-Base10 to base 26\n')
    data={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    if user_input == '1':

        s=str(input("Enter the alphabet\n")).upper()

        result=base10_valueGenerator(s,data)
        print(result)
    elif user_input == '2':
        d1 = int(input("Enter first base10 value\t"))


        result = base26_valueGenerator(d1,data)
        print(result)

    else:
        print('wrong choice. Try again')
        start_con()

start_con()
