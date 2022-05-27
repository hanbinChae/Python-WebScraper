# *args : position argument가 무한 반복
# ** kwargs : keyword argument가 dictionary 형태로 무한 반복
def plus(*args,**kwargs):
    result = 0
    for number in args:
        result +=number
    print('합계 :',result)

#plus(1,2,31,24,1,245,12,5,12,5,12,5,6,215)

class Car():
    def __init__(self,**kwargs):
        self.name = kwargs.get("name","Noname")
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color","white")
        self.price = kwargs.get("price","$20")

    def __str__(self):
        return f"Car with {self.wheels}"

class Convertible(Car):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time",10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"


porsche = Convertible(name='porsche',color="Green",price="$80")
print(porsche.color)

mini = Car(name='BMW mini')
