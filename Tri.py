def selectMin(list):
    var=list[0]
    for i in list:
        if var>i:
            var=i
    return var

def triSelect(list):
    result=[]
    while len(list)>0:
        var=selectMin(list)
        list.remove(var)
        result.append(var)
    return result

print (selectMin([4,2,7,8]))

def fusion(list1,list2):
    return (list1+list2)


def triFusion(list):
    if len(list)>1:  
        list0=list[0:1]
        list1=list[2:3]
        
        l1=triFusion(list0)
        l2=triFusion(list1)
        return fusion (l1,l2)
    else:
        return list

print(triFusion(list))