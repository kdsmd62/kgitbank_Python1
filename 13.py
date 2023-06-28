'''
7. 함수
7.3 실습
- 기본실습1.
x, y = 4, 2
         
def num1(a, b):   
    c = a + b
    return c 
def num2(a, b):   
    return a - b  

d = num1(x, y)  
print(d)
print(num2(x, y))

- 기본실습2.
a, b = 3, 4
def sum(a, b):
    c = a + b
    print("%d + %d = %d" % (a, b, c))
sum(a, b)   

- 기본실습3
def sum(a,b):
    return a +b
a, b = 3, 4
c = sum(a, b)
print(c)

- 기본실습4
def sum(*args):         # Argument(인수)s : 입력값이 몇 개인지 모를때 // 3. 입력받은 값은 기본적으로 값을 받아들이는 인수(변수)가 있어야 하지만 
    sum = 0             # 인수와 상관없이 무관하게 어떤 값이든 받아서 처리할 수 있게 하기 위해 예약어인 '*args' 를 사용한다.
    for i in args:      
        sum += i            # sum = sum + i
    return sum
a, b, c = 3, 4, 5           # 1. 변수에 값을 입력
d = sum(a, b, c)            # 2. 입력받은 3개의 값을 받아서 처리할 함수 호출
print(d)         

- 응용실습1
a = "KgItBank2022121"
b, c, d, e = a[:8],a[8:12],a[12:13],a[13:15]

def str(b, c, d, e):
    print("%s %s년 %s월 %s일" % (b, c, d, e))
str(b, c, d, e)

def str2(b, c, d, e):
    return "{} {}년 {}월 {}일".format(b, c, d, e)
print(str2(b, c, d, e))

def pyt():              # 강사님 코드1
    a = "KgItBank2022121"
    b, c, d, e = a[:8],a[8:12],a[12:13],a[13:15]
    print("%s %s년 %s월 %s일" % (b, c, d, e))
pyt()

def pyt(v):         # 강사님 코드2
    b, c, d, e = a[:8], a[8:12], a[12:13], a[13:15]
    print("%s %s년 %s월 %s일" % (b, c, d, e))
    
a = "KgItBank2022121"
pyt(a)

- 임의의 값을 받아 들인 후 10으로 나눴을 때 몫과 나머지를 구하는 소스

num = int(input("값 입력 : "))

def div(a):
    tmp1 = a // 10
    tmp2 = a % 10
    print("몫 : %d | 나머지 : %d" % (tmp1, tmp2))
    
def div2(a):            # 그냥,, 리스트가 좋아서
    list = []
    tmp1 = a // 10
    tmp2 = a % 10
    list.append(tmp1)
    list.append(tmp2)
    return list

div(num)
print("몫 : %d | 나머지 : %d" % (div2(num)[0], div2(num)[1]))

def madal():                # 강사님 코드(왜 while문을 사용했는지는 이해안감)
    num = int(input("값 입력 : "))
    while True:
        tmp1 = num // 10
        tmp2 = num % 10
        print("입력값(%d) : 몫(%d), 나머지(%d)" % (num, tmp1, tmp2))
        break
    print("프로그램 종료")
madal()
            
'''
def madal():                # 2. 인수가 없기 때문에 
    num = int(input("숫자 입력 : "))            # 3. 함수안에 있는 내용의 결과를
    return num          # 3. 호출한 곳으로 리턴한다.
num = madal()           # 1. 함수를 호출하고 결과값을 변수로 치환
tmp1 = num / 10         # 5. 받아 온 값을 처리
tmp2 = num % 10
print("입력값(%d) : 몫(%d) | 나머지(%d)" % (num, tmp1, tmp2))





         