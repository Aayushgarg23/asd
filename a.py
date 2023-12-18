def arithmetic_arranger(list,results=False):
    list1=[]
    list2=[]
    list3=[]
    for item in list:
        item=item.split(" ")
        operand1=int(item[0])
        operand2=int(item[2])
        if operand1 < 10000:
            if item[1]=="+":
              operand2=operand2
            elif item[1]=="-":
              operand2=(-1)*operand2
            else:
                print("Error: Operator must be '+' or '-'.")
                exit()
        else:
            print("Error: Numbers must only contain digits.")
            exit()
        list1.append(operand1)
        if len(list1)>4:
            print("Error: Error: Too many problems.")
            exit()
        else:
            list2.append(operand2)
            list3.append(operand1+operand2)
            continue
    a=""
    b=""
    c=""
    d=""
    x=" "   #define a blank space
    y="-"   #define a strike
    for i in range(len(list1)):
        loop1=len(str(list1[i])) #number of digits of operand 1
        loop2=len(str(list2[i])) #number of digits of operand 2
        loop3=len(str(list3[i]))#number of digits of operand 3
        digit=max(loop1,loop2,loop3)  #largest number of digits between operand 1 and operand 2
        a=a+x*(2+digit-loop1)+str(list1[i])+x*4
        if list2[i]>0:
            b=b+"+"+x*(1+digit-loop2)+str(list2[i])+x*4
        else:
            b=b+"-"+x*(2+digit-loop2)+str((-1)*list2[i])+x*4
        c=c+x*2+y*digit+x*4
        d=d+x*(2+digit-loop3)+str(list3[i])+x*4
    print(a)
    print(b)
    print(c)
    if results==True:
        print(d)
    else:
        print("")

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)
