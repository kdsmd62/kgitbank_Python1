'''
7. 함수
7.3 실습
- 다음의 주어진 값을 각각 10진수로 표현하는 값을 함수로 표현
    : 주어진 값(0o177, 0x8ff, 0xABC, 0b11011011)
    : 개별적인 함수로 표현해야 하고 출력문은 반드시 모두 함수 밖에서 표현
1) 내 코드
a, b, c, d = 0o177, 0x8ff, 0xABC, 0b11011011
dec = 0

def oct_to_dec(x):
    dec = int(x)
    return dec
def hex_to_dec(x):
    dec = "%d" % x
    return dec
def bin_to_dec(x):
    dec = "%d" % x
    return dec

print("8진수 %o를 10진수로 표현(%s)" % (a, oct_to_dec(a)))
print("16진수 %x을 10진수로 표현(%s)" % (b, hex_to_dec(b)))
print("16진수 %x을 10진수로 표현(%s)" % (c, hex_to_dec(c)))
print("2진수 b를 10진수로 표현(%s)" % bin_to_dec(d))
2) 강사님 코드
def bin():
    a = 0b11011011
    return a
def oct(b):
    bb = int(b)
    return bb
def hexa1():
    c = 0x8ff
    return int(c)
def hexa2(num):
    dd = ("%d" % num)
    return dd
aa = bin()
print(type(aa))
print("2진수 a를 10진수로 표현(%d)" % aa)
print("2진수 a를 10진수로 표현(%d)" % bin())

b = 0o177
print("8진수 b를 10진수로 표현(%d)" % oct(b))

c = hexa1()
d = 0xABC
print("16진수 c(%x)와 d(%x)를 10진수로 표현(%d, %d)" % (c, d, c, d))

 - 홍길동씨의 과목별 점수는 다음과 같다고 할 때 합계와 평균을 함수로 표현
    : 주어진 값(국어/85.5, 영어/79.3, 수학/95.4)
    
1) 내코드 (강사님 코드와 거의 흡사하여 강사님 코드 따로 필기안함)
a, b, c = 85.5, 79.3, 95.4

def sum(x, y, z):
    return x + y + z
def avg(result):
    return result / 3

res_sum = sum(a, b, c)
res_avg = avg(res_sum)

print("합계(%.1f) | 평균(%.1f)" % (res_sum, res_avg))

- 실습
def x(x):
    return x
def y(y):
    return y
        
a = int(input("a : "))
b = int(input("b : "))
aa, bb = x(a), y(b)

if aa > bb:
    print("x(%d)는 y(%d)보다 크다" % (aa, bb))
    
- 실습
def func(a):
    if a > 10 or a != 15: return True           # 조건문에 바로 return 사용 가능
    else: return False
a = int(input("정수 입력 : "))
d = func(a)
print("결과 : {}".format(d))            # 결과값이 bool 대수이므로 형을 지정할 필요없는 포맷함수 사용

-
madal = "KG It Bank Samadal"

# 첫번째 방법
def fs(string):
    if string in madal:
        return string
    else: 
        return ''

str = input("찾고자 하는 문자열 : ")

res = fs(str)

if res == str:
    print("찾는 문자열 %s는 있다" % str)
else: print("찾고자 하는 문자열 %s는 없다" % str)

# 두번째 방법
def fs(string):
    if string in madal:
        return True
    else: 
        return False

string = input("찾고자 하는 문자열 : ")

res = fs(string)

if res == True:
    print("찾는 문자열 %s는 있다" % string)
else: print("찾고자 하는 문자열 %s는 없다" % string)

- 두 개의 정수값을 입력 받고 비교한 후 큰 값과 작은 값을 출력
    : print()문의 경우 소스의 내용에 따라서 결과가 다르게 나올 수 있기 때문에
    : 가급적 함수 안에 넣지 않는 것이 좋다. 
    : 즉, 함수 안에는 변동이 없는 등이 내용으로 구성하는 것이 좋다.(상수 형태)
    : 그러나 조건식에 따라 함수 안에 출력문을 포함하는 것이 코딩에 유리한 경우도 있다.
1) 내 코드
num1, num2 = int(input("정수1 입력 : ")), int(input("정수2 입력 : "))

def comp(num1, num2):           # 어떻게 print문은 함수밖에서 실행할 것인가?
    if num1 > num2:
        print("큰 값 : %d | 작은 값 : %d" % (num1, num2))
    else:
        print("큰 값 : %d | 작은 값 : %d" % (num2, num1))
comp(num1, num2)
2) 내 코드2
def high(num1, num2):
    if num1 > num2:
        return num1
    else: return num2
def low(num1, num2):
    if num1 > num2:
        return num2
    else: return num1
        
num1, num2 = int(input("정수1 입력 : ")), int(input("정수2 입력 : "))

a = high(num1, num2)
b = low(num1, num2)

print("큰 값 : %d | 작은 값 : %d" % (a, b))

- 받아들인 값(기호)에 따라 사칙연산을 하는 소스
    : print()문의 경우 소스의 내용에 따라서 결과가 다르게 나올 수 있기 때문에
    : 가급적 함수 안에 넣지 않는 것이 좋다. 
    : 즉, 함수 안에는 변동이 없는 등이 내용으로 구성하는 것이 좋다.(상수 형태)
    : 그러나 조건식에 따라 함수 안에 출력문을 포함하는 것이 코딩에 유리한 경우도 있다.

'''

