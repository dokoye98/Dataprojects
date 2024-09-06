from flask import Flask,request,render_template

def mill(list_num):
    result_s = 0
    for num in list_num:
        result_s += num
    res_av = result_s/len(list_num)
    return res_av
    
mill([5,8,5])
print("hello {0[0]} and {0[1]}".format('foo','bin'))