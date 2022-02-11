from os import system
pause = lambda:system("pause")
def b_m_m(a,b):
    if a%b==0:
        return b
    return b_m_m(b,a%b)

a=int(input("number 1 = "))
b=int(input("number 2 = "))
x=b_m_m(a,b)
print("b_m_m=",x)
print("k_m_m=",a*b/x)
pause()
