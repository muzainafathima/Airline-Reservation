import string
import random

def ticket(): #generates only digits
    s2=string.digits
    s3=list(s2)
    random.shuffle(s3)      
    tno="".join(s3[0:9])
    return tno
def flight(): #generates strings
    s1=string.ascii_letters
    s2=string.digits
    s=list(s1+s2)
    random.shuffle(s)
    fno="".join(s[0:6])
    return fno
def batch():
    st=string.digits
    a=list(st)
    random.shuffle(a)
    n=''.join(a[:3])
    return n
