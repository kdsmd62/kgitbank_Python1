'''
8. class
8.3 실습

1)
class FourCal2:
    #def __self__(self):         # 기본 생성자(__init__)만 사용할 경우에는 이렇게 임의로 설정해도 된다.
                                    # FourCal2라는 클래스 자체를 하위의 함수들이 사용하게 하겠다.
    
    def add(self, first, second):              # 이 메서드는 실제 소스에는 영향을 전혀 미치지 못한다.
        self.first = first
        self.second = second
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first - self.second
        return result
    def sub(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
fc = FourCal2()
add = fc.add(4,2)
print(add)
print(fc.mul())
print(fc.sub())
print(fc.div())

- 한 개의 클래스로 구성되어 있는 소스를 4개의 클래스로 분리해서 코딩
1) 나
class Cal1:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):             
        result = self.first + self.second
        return result
class Cal2:
    def mul(self, first, second):
        self.first = first
        self.second = second
        result = self.first - self.second
        return result
class Cal3:
    def sub(self, first, second):
        self.first = first
        self.second = second
        result = self.first * self.second
        return result
class Cal4:
    def div(self, first, second):
        self.first = first
        self.second = second
        result = self.first / self.second
        return result

add = Cal1(4, 2).add()
print(add)
mul = Cal2().mul(4,2)
print(mul)
sub = Cal3().sub(4,2)
print(sub)
div = Cal4().div(4,2)
print(div) 

2) Madal's
class _ADD:
    def madal(self, first, second):
        self.first = first
        self.second = second
    def add(self):             
        return self.first + self.second

a = _ADD()
a.madal(4, 2)
print(a.add())

class _MUL:
    def mul(self, first, second):
        self.first = first
        self.second = second
        return self.first - self.second
    
b = _MUL()
print(b.mul(5, 3))

class _SUB:
    def dals(self, first, second):
        self.first = first
        self.second = second
    def sub(self):
        return self.first * self.second
    
c = _SUB()
c.dals(7, 3)
print(c.sub())

class _DIV:
    def __init__(self):
        self.result = 0
    def div(self, first, second):
        self.first = first
        self.second = second
        return self.first / self.second
    def div2(self, first, second):
        return first + second           #self 써서 치환하지 않은 경우엔 그냥 변수명 입력
    
print(_DIV().div(8, 4))
print(_DIV().div2(8, 4))

- 문자열(KgItBank20221218)을 일반코드, 함수코드, 클래스코드로 출력하는 소스를 코딩
str = 'KgItBank20221218'

# 일반코드
company = str[:8]
date = str[8:]
print(company + date)

# 함수코드
def div(a):
    com = a[:8]
    day = a[8:]
    mul(com, day)
def mul(c, d):
    print(c + d)

div(str)

# 클래스모드
class _PNT:
    def __init__(self, b):
        self.string = b
    def div2(self):
        self.com = self.string[:8]
        self.date = self.string[8:]
        return self.com + self.date

fn = _PNT(str)
print(fn.div2())   

- 3개의 정수값을 입력받고 비교한 수 가장 큰 값과 가장 작은 값만을 출력
1)나
a = int(input("정수1 입력 : "))
b = int(input("정수2 입력 : "))
c = int(input("정수3 입력 : "))

class _COMP:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def comp_high(self):
        max = self.a
        if self.b > self.a:
            max = self.b
        if self.c > max:
            max = self.c
        return max
    def comp_low(self):
        min = self.a
        if self.b < self.a:
            min = self.b
        if self.c < min:
            min = self.c
        return min
    
fn = _COMP(a, b, c)
print("큰 값 : {} | 작은 값 : {}".format(fn.comp_high(), fn.comp_low()))

2)Madal's
a = int(input("정수1 입력 : "))
b = int(input("정수2 입력 : "))
c = int(input("정수3 입력 : "))

class _X:
    def max(self, num1, num2, num3):
        if num1 > num2 and num1 > num3:
            num_max = num1
            return num_max
        elif num2 > num1 and num2 > num3:
            num_max = num2
            return num_max
        elif num3 > num1 and num3 > num2:
            num_max = num3
            return num_max
class _Y:
    def min(self, num1, num2, num3):
        if num1 < num2 and num1 < num3:
            num_min = num1
            return num_min
        elif num2 < num1 and num2 < num3:
            num_min = num2
            return num_min
        elif num3 < num1 and num3 < num2:
            num_min = num3
            return num_min
xmax = _X()
ymin = _Y()
x = xmax.max(a,b,c)
y = ymin.min(a,b,c)
print("가장 큰 값(%d) | 가장 작은 값(%d)" % (x, y))

- 1개의 정수값(1~24)을 입력 받고 시간을 출력
    : 정오(12시), 자정(24시), 오전(1시~11시), 오후(13시~23시)
'''
'''
nlist = []

while True:
    tmp = input("정수를 입력 : ")
    nlist.append(tmp)
    if len(tmp) == 0:
        break

class _COMP:
    def __init__(self, a):
        self.a = a

    def comp_high(self):
        for i in self.a:   
            max = self.a[i]
            if self.a[i+1] > max:
                max = self.[i+1]
        return max
    def comp_low(self):
        for i in self.a:   
            min = self.a[i]
            if self.a[i+1] < min:
                min = self.[i+1]
        return max
    
fn = _COMP(nlist)
print("큰 값 : {} | 작은 값 : {}".format(fn.comp_high(), fn.comp_low()))
''' 
'''   
time = int(input("시간을 입력하시오 : "))     

class _TIME:
    def time124(self, t):           # 제발!!
        if 1 <= t <= 24:            # 클래스 안에 정의되어 있는 메서드의 첫 항목은 무조건 'self'가 와야 한다.
            if t == 12 : print("정오")
            elif t == 24 : print("자정")
            elif 1 <= t <= 11 : print("오전")
            elif 13 <= t <= 23 : print("오후")
        else: print("값을 다시 입력하세요")
ti = _TIME()
ti.time124(time)
'''
nlist = []

while True:
    tmp = input("정수를 입력 : ")
    nlist.append(tmp)
    if len(tmp) == 0:
        break

class _COMP:
    def __init__(self, a):
        self.a = a

    def comp_high(self):
        for i in self.a:   
            max = self.a[i]
            if self.a[i+1] > max:
                max = self.a[i+1]
        return int(max)
    def comp_low(self):
        for i in self.a:   
            min = self.a[i]
            if self.a[i+1] < min:
                min = self.a[i+1]
        return int(min)
    
fn = _COMP(nlist)
print("큰 값 : {} | 작은 값 : {}".format(fn.comp_high(), fn.comp_low()))             