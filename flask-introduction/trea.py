sampledict = {"a":"apple","b":"ball"}

sampledict.update({"b":"ball","c":"cat"})


#print(sampledict["a"],sampledict.get("b"),sampledict.get("c"))


def mod(arg_list):
    arg_list = arg_list + [60 , 70,80]
    print("inside", arg_list)
    

i_list = [10,20,30,40,50]
#print("before", i_list)
#mod(i_list)
#print("after" , i_list)

mylist = [0]*5

for i in range(1,5):
    mylist[i] = (i-1)*i
    
#print(mylist)


def sample(value):
    sum1 = 0
    for i in value:
        
        if i%2 !=0:
            sum1 += value[i]
        else:
            sum1-=i
    print(sum1)
    
dict1 = {1:2,2:4,3:6,5:8}

sample(dict1)


list3 = [10,20,30,40,50]
list3.insert(7,90)


tuple1 = (10)
print(tuple1)

    