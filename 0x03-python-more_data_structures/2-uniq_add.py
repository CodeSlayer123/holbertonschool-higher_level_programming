#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    newList = []
    for i in range(len(my_list)):
        flag = 1
        if my_list[i] not in newList:
            if my_list.count(my_list[i]) == 1:
                newList.append(my_list[i])
            else:
                flag = 0
        if flag == 0:
            newList.append(my_list[i])
    for i in range(len(newList)):
        sum += newList[i]
    return(sum)
