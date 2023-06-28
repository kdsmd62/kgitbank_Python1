'''
8. Class
8.4 클래스의 인자값 'self'
- 실습
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

2) 강사님
# 이중함수 사용
def gugu1():
    for i in range(1, 10, 1):
        for j in range(2, 10, 1):
            print("{} * {} = {}".format(j, i, i*j), end='\t') 
        gugu2()
def gugu2():
    print("")
gugu1()

3) 클래스 사용
class GC:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def gugu(self):
        for i in range(self.x, self.y):
            for j in range(2, 10):
                print("{} * {} = {}".format(j, i, i*j), end='\t') 
            print("")
num1, num2 = int(input("입력1 : ")), int(input("입력2 : "))
inst = GC(num1, num2)
inst.gugu()

: 클래스의 인스턴스 a에 samadal 메서드를 수행하지 않고(a.samadal(4,2)) 
: add 메서드를 수행(print(a.add()))하면 오류가 발생한다. 왜냐하면 samadal 메서드를 수행해야
: 객체 a의 객체변수 first와 second가 동작이 되기 때문이다.
: 이렇게 객체에 초기값을 설정해야 할 필요가 있을 때는 'samadal'과 같은 메서드를 호출하여 
: 설정하기 보다는 생성자를 구현하는 것이 안전한 방법이다.
: 생성자란 객체가 생성될 때(a = _ADD()) 자동으로 호출되는 메서드(samadal())를 의미한다.
: 생성자 이름은 일반적으로 '__init__' 을 사용한다.

    class _ADD:
        def samadal(self, first, second):
            self.first = first
            self.second = second
        def add(self):
            return self.first + self.second
    a = _ADD()
    a.samadal(4,2)
    print(a.add())
    
class FourCal:
    def __init__(self, first, second):          # 1. 생성자로 자동 인식되고
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def mul(self):
        return self.first - self.second
    def sub(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second
x, y = int(input("값1 : ")), int(input("값2 : "))
a = FourCal(x, y)           # 2. 객체가 생성되는 시점에 자동으로 호출된다.
                            # 클래스명 안에 값을 넣게 되면 '값'과 동일하게 인식되므로 자동적으로 클래스 안에 있는 
                            # 생성자와 해당 변수들을 자동 호출하게 된다.                            
caf = a.first               # 클래스를 직접 사용(caf = FourCal(x,y).first) 하지않고 인스턴스 객체(a)화해서
cas = a.second              # 사용하는 이유는, 클래스 안에 있는 요소(메서드, 변수 등)들을 사용할 수 있기 때문.
caadd = a.add()
camul = a.mul()
casub = a.sub()
cadiv = a.div()

print("%d + %d = %d" % (caf, cas, caadd))
print("%d - %d = %d" % (caf, cas, camul))
print("%d * %d = %d" % (caf, cas, casub))
print(f"{caf} / {cas} = {cadiv}")

- 실습(생성자에서 많이 사용되는 유형)
class ex1:
    def __init__(self):
        print("생성자는 객체 생성 시 자동으로 호출된다.")
_ex1 = ex1()
print("=" * 60)

x = "생성자는 객체 생성 시 자동으로 호출된다."
class ex2:
    def __init__(self, a):          # 생성자 선언
        self.a = a

_ex2 = ex2(x)                       # 클래스에 인수값을 대입한다.
madal = _ex2.a
print("%s" % madal)
print("=" * 60)

x = "생성자는 객체 생성 시 자동으로 호출된다."
class ex3:
    #def __init__(self, a):         # 생성자와 동일한 값을 호출하는 메서드가 있는 경우에는 한 곳에만 허용한다.
                                    # 즉, 하단에 이미 외부에서의 값을 호출했기 때문에 여기서는 생략해야 한다.     
    def __init__(self):          
        pass
    def out(self, a):
        self.a = a
        return self.a

_ex3 = ex3()
madal = _ex3.out(x)                 # 클래스 안에 있는 메서드에 인수값을 대입한다. (인수값과 인자값 둘 다 변수라고 생각하면 됨)
print("%s" % madal)
print("=" * 60)


class ex4:
    def __init__(self, a):        
        self.a = a                              
    def out(self):
        return self.a           # 2. 호출한 객체(madal) 에게 그대로 되돌려준다.
_ex4 = ex4(x)                   # 1. 여기서 받아드린 변수 x의 값을
madal = _ex4.out()              
print("%s" % madal)
print("=" * 60)


x = "사마달"

class ex5:
    def __init__(self, a):      # 생성자에서는 변수값을 받아들이거나 받아들인 값을 변수로 치환하는 작업만 한다. 
        self.ln = a[0]          # 인덱싱
        self.fn = a[1:]         # 슬라이싱
    def stra(self):
        return self.ln + self.fn
_ex5 = ex5(x)
madal1 = _ex5.ln
madal2 = _ex5.fn
madal3 = _ex5.stra()
print("%s%s" % (madal1, madal2))            # '사''마달'
print("{}".format(madal3))                  # '사' + '마달'  

x = "사마달"

class ex6:
    def __init__(self):    
        self.samadal = []        
    def stra(self, madal):
        self.samadal.append(madal)          # append는 단독으로 사용된느 함수이기 때문에 되돌려 줄 필요가
                                            # 없을 때 대입이 된다. 
                                            
        return self.samadal
        # return self.samadal.append(madal)       # 따라서 되돌려 줄 필요가 없는데도 되돌려주고 있기 때문에
                                                 # 소스는 문제가 없지만 정상적인 값이 출력이 안된다.(None)
                                                 # 함수 자체를 리턴하는거라 none 뜨는 듯 (아마도....?)
_ex6 = ex6()
madal = _ex6.stra(x)
print("%s" % madal)


8.8 클래스의 상속(Inheritance)
    - 개요
        : 일반적인 상속과 같은 의미이며 클래스에서도 이 개념이 적용된다.
        : 임의의 어떤 클래스를 생성할 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것을 말한다.
        : 클래스의 상속은, '상속해 주는 클래스(베이스 클래스)'와 '상속받는 클래스(파생 클래스)'로 구성한다.
        : 또한, 파생 클래스는 함수와 같은 형태를 하고 있다.
    - 상속을 사용하는 목적
        : 일반적인 상속은 기존 클래스(상속해 주는 클래스)의  내용 변경없이 그대로 사용하고자 할 때 사용한다.
        : 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.
        : 즉, 객체지향 언어(C/C++, Java, ...)에서의 '헤더파일(#inclue <stdio.h>)' 과 유사
        : 기존 클래스는 그대로 둔 채로 클래스의 기능을 확장할 때 많이 사용한다.
    - 실습
        : 상속해 주는 클래스
        : 상속 받는 클래스
            
'''
class FourCal:              # 상속해 주는 클래스
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
a = FourCal(4, 2)
caf = a.first
cas = a.second
caa = a.add()
print("{} + {} = {}".format(caf, cas, caa))

  
class MoreFourCal(FourCal):         # 상속 받는 클래스(FourCal 클래스의 모든 내용을 날로 먹겠다...)
    pass                            # '수행할 내용이 없다'는 말이다. 그러나 여기서의 의미는 상속해
                                    # 주는 클래스(FourCal)를 수행하지 않는다는 말이 아니라
                                    # 상속받는 클래스가 수행할 내용이 없다는 말이다.
                                    # 즉, 상속해 주는 클래스의 내용만을 사용할 것이기 때문에 상속받는
                                    # 클래스는 별도의 내용이 필요가 없다는 말이다.
b = MoreFourCal(8, 5)               # 상속해 주는 클래스의 인스턴스 객체 생성의 유형을 사용하겠다. 
cafb = b.first                      # 상속해 주는 클래스의 초기값의 유형을 사용하겠다...
casb = b.second                      
caab = b.add()                      # 상속해 주는 클래스의 메서드를 사용하겠다...
print("{} + {} = {}".format(cafb, casb, caab))

class Samadal(FourCal):         # 상속 확장
    def pows(self):             # 상속 받는 것뿐만 아니라 별도의 메서드를 생성해서    
        result1 = self.first ** self.second     # 사용할 수도 있다. 상속받는 클래스 안에 별도의 추가되는 
        return result1                          # 내용을 '상속 확장'이라고 한다.

c = Samadal(2, 3)
print(c.pows())

class Etc(FourCal):
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second
d = Etc(2, 3)           
#d = Etc(2, 3)          # 주 클래스의 인스턴스 객체는 사용할 수가 없다.     
#print(d.mul())         # 왜? 주 클래스의 안에 있는 내용만 상속을 받는 것이지 주 클래스 밖에 있는 
print(d.mul())          # 것들도 상속받는 것이 아니기 때문이다.    
print(d.sub())          # 따라서 별도의 인스턴스 객체 생성과 값을 사용해야 한다.
print(d.div())
    


