'''
8. Class
8.4 클래스의 인자값 'self'
    - 특징 
        : 클래스 밖에서 값을 받아들일 때는 'self'인자를 사용한다.(옵션)
        : self를 사용할 때의 두 가지 유형
            ; 외부서 받아들인 값을 그냥 사용할 경우(메서드 안에만 'self'를 입력)
            class FourCal:
                def samadal(self, a, b):        # 외부에서 값(a, b)을 가져올 때
            ; 변수로 치환해서 사용할 경우(모든 변수에 'self'를 입력)
            class FourCal:
                def samadal(self, a, b):
                    self.a = a
                    self.b = b
                    return self.a + self.b
1)
class FourCal:
    def __init__(self, a, b):           
        self.a = a          
        self.b = b
    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    
a = int(input("정수1 입력 : "))
b = int(input("정수2 입력 : "))
c = input("기호 입력 : ")

cal = FourCal(a,b)

if c == "+":
    res = cal.sum()
elif c == "-":
    res = cal.sub()
elif c == "*":
    res = cal.mul()
elif c == "/":
    res = cal.div()
else: print("기호를 다시 입력하시오")

print("{} {} {} = {}".format(a, c, b, res))

2) 강사님
class _FC:                      # 1. 각 메서드 별로 초기값을 초기화
    def samadal(self):
        self.madal = 0          # 이 구문은 소스 실행에 영향을 주지 못한다.
    def sum(self, a, b):
        sums = a + b
        return sums
    def mul(self, a, b):
        sums = a * b
        return sums
    def div(self, a, b):
        sums = a / b
        return sums
    def sub(self, a, b):
        sums = a - b
        return sums
cal = _FC()
num1, num2 = int(input("숫자1 : ")), int(input("숫자2 : "))
print(cal.sum(num1, num2))
print(cal.mul(num1, num2))
print(cal.div(num1, num2))
print(cal.sub(num1, num2))

3) 강사님
class _FC:                      # 2. 초기자를 이용한 초기화
    def __init__(self, a, b):   # def samadal(self, a, b):  <- 이렇게 쓰면 오류발생
        self.a = a
        self.b = b
    def sum(self):
        sums = self.a + self.b
        return sums
    def mul(self):
        muls = self.a * self.b
        return muls
    def div(self):
        divs = self.a / self.b
        return divs
    def sub(self):
        subs = self.a - self.b
        return subs
    
num1, num2 = int(input("숫자1 : ")), int(input("숫자2 : ")) 
cal = _FC(num1, num2)

print(cal.sum())        # print(caa.sum(num1, num2)) 로 입력하면 오류가 발생한다.
print(cal.mul())        # 왜? sum()메서드는 인자값이 없이 초기자에서 값을 가져와서 실행하니까.
print(cal.div())
print(cal.sub())

- 실습
class Samadal:
    pass            # 수행할 내용이 없다'는 것을 말한다.
a = Samadal()       # <__main__.Samadal object at 0x00000207AC1EE680>
print(a)            # 문법상 오류는 아니지만 처리할 수 있는 객체(함수)가 없다.
print(type(a))      # <class '__main__.Samadal'>

- 함수만 사용한 경우와 클래스를 사용한 경우의비교
class Samadal:
    def py(self):
        print("Phython")
it = Samadal()
it.py()
Samadal().py()

- 클래스의 메서드로 대입되는 값의 유형을 알 수 없는 경우
class Samadal:
    def madal(self, a):         # 이 메서드는 정수를 대입하면 정수로, 문자열을 대입하면 문자열로 인식
        print(type(a))
        print("Phython")
pi = Samadal()
pi.madal('1')

- 클래스의 메서드에 조건문이 있는 경우
class Samadal:
    def it(self, madal):
        print(type(madal))
        for i in madal:
            print(i)
a = Samadal()
a.it("SAMADAL")
#a.it(123)           # 'int' object is not iterable (정수형 객체는 반복할 수가 없다.)

- 실습
 : 다음의 내용을 '일반식, 함수식(2가지), 클래스식(2가지)로 표현
 : 내 이름은 '사마달'이고 전화번호는 '010-1234-5678'입니다.
 
1)
 # 일반식
name = '사마달'
number = '010-1234-5678'
print("내 이름은 '{}'이고 전화번호는 '{}'입니다".format(name, number))

# 함수식
def pname():
    return '사마달'
def pnumber():
    return '010-1234-5678'
print("내 이름은 '{}'이고 전화번호는 '{}'입니다".format(pname(), pnumber()))

# 클래스식
str = "내 이름은 '사마달'이고 전화번호는 '010-1234-5678'입니다."
class cname:
    def fname(self, a):
        name2 = a[7:10]
        return name2
class cnumber:
    def fnumber(self, b):
        number2 = b[-18:-5]
        return number2

cn = cname().fname(str)
cb = cnumber().fnumber(str)   

print("내 이름은 '{}'이고 전화번호는 '{}'입니다".format(cn, cb))

2)
# 일반식
name = '사마달'
number = '010-1234-5678'
print("내 이름은 '{}'이고 전화번호는 '{}'입니다".format(name, number))
print("=" * 80)



def nt1():          # 함수식 1
    name2, tel2 = '사마달', '010-1234-5678'
    print("내 이름은 '{}'이고 전화번호는 '{}'입니다".format(name2, tel2))
nt1()
print("=" * 80)

def nt21(name):         # 함수식 2
    return name
def nt22(tel):
    return tel
a = '사마달'
b = '010-1234-5678'

c, d = nt21(a) , nt22(b)
print("내 이름은 '{}'이고 전화번호는 '{}'입니다".format(c, d))
print("=" * 80)

class _NT:            # 클래스식 1
    def nt31(self, name):         
        return name
    def nt32(self, tel):
        return tel
g = _NT()
e = '사마달'
f = '010-1234-5678'
h, i = g.nt31(e), g.nt32(f)
print("내 이름은 '{}'이고 전화번호는 '{}'입니다".format(h, i))
print("=" * 80)

class _NT2:            # 클래스식 2
    def nt4(self):         
        name, tel = '사마달', '010-1234-5678'
        print("내 이름은 '{}'이고 전화번호는 '{}'입니다".format(name, tel))
j = _NT2()
j.nt4()
print("=" * 80)

: 2. 구구단 중에서 5단만 출력하는 소스
1)
class _GUGU:
    def gugu(self, a):
        for i in range(1, 10, 1):
            res = a * i
            print("%d * %d = %d" % (a, i, res)) 
fn = _GUGU()
fn.gugu(5)

2) 강사님
odan = 5
def sam1():
    sam2()
def sam2():
    for i in range(1, 10):
        print("%d * %d = %d" % (odan, i, odan*i))
sam1()

class Dan:
    def sam1(self, oh):
        self.oh = oh       
    def sam2(self):
        for i in range(1, 10):
            print("%d * %d = %d" % (oh, i, oh*i))
oh = int(input("단 입력 :"))
a = Dan()
a.sam2()
: 3. 구구단 전체를 출력하는 소스
1)
class _GUGU2:
    def display(self):
        for k in range(1, 10, 1):
            for j in range(2, 10, 1):
                res2 = _GUGU2().mul(k, j)
                print("{} * {} = {}".format(j, k, res2), end='\t') 
            print("")
    def mul(self, a, b):
        return a * b
fn2 = _GUGU2()
fn2.display()

'''


class _GUGU2:
    def display(self):
        for k in range(1, 10, 1):
            for j in range(2, 10, 1):
                res2 = _GUGU2().mul(k, j)
                print("{} * {} = {}".format(j, k, res2), end='\t') 
            print("")
    def mul(self, a, b):
        return a * b
fn2 = _GUGU2()
fn2.display()

        





        
    
    