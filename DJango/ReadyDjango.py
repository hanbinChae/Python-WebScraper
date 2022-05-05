# *args : position argument가 무한 반복
# ** kwargs : keyword argument가 dictionary 형태로 무한 반복
def plus(*args,**kwargs):
    result = 0
    for number in args:
        result +=number
    print('합계 :',result)

plus(1,2,31,24,1,245,12,5,12,5,12,5,6,215)