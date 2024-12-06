def ele_list(list,indx=0):
    if indx==len(list):
        return
    print(list[indx])
    ele_list(list,indx+1)
x=["arvee",12,20.35,True,False]
ele_list(x)