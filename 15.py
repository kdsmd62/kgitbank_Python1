'''
7. 함수
7.3 실습
- 받아들인 값(기호)에 따라 사칙연산을 하는 소스
    : print()문의 경우 소스의 내용에 따라서 결과가 다르게 나올 수 있기 때문에
    : 가급적 함수 안에 넣지 않는 것이 좋다. 
    : 즉, 함수 안에는 변동이 없는 등이 내용으로 구성하는 것이 좋다.(상수 형태)
    : 그러나 조건식에 따라 함수 안에 출력문을 포함하는 것이 코딩에 유리한 경우도 있다.
    
1) 내 코드
num1, num2 = int(input("숫자1 입력 : ")), int(input("숫자2 입력 : "))
a = input("연산기호 입력 : ")

def cal(a, num1, num2):
    if a == '+':
        return num1 + num2 
    elif a == '-':
        return num1 - num2
    elif a == '*':
        return num1 * num2
    elif a == '/':
        return num1 / num2

result = cal(a, num1, num2)
#print("%d %s %d = %d" % (num1, a, num2, result))
print("{} {} {} = {}" .format(num1, a, num2, result))           # 자동으로 형을 판별해줘서 더 적합한듯
2) 강사님 코드
각각 연산에 대한 함수를 하나씩 만드는 코드
소스가 너무 길어 따로 필기하지 않음

- 
select = 0          # 소스에 전혀 영향을 주지 않는다.
select = int(input("1. 콜라 | 2. 사이다 | 3. 환타 : "))
if select == 1: print("콜라")
elif select == 2: print("사이다")
elif select == 3: print("환타")
else: print("다시선택")

-
def add_mul(select):         # *agrs 사용시 함수 밖의 변수명과 함수 안의 변수명이 같아야 정상적으로 동작 (사용하지 않아도 변수명 일치하면 동작하는듯)
    if select == "add": return num1 + num2
    elif select == "min": return num1 - num2
    elif select == "mul": return num1 * num2
    elif select == "div": return num1 / num2
    
num1, num2 = int(input("숫자1 입력 : ")), int(input("숫자2 입력 : "))
buho = input("부호 : ")
res = add_mul(buho)
print(res)

7.4 이중함수 (매우중요)
- 단순하게 함수를 순서대로 나열하는 것이 아니라 함수안에 또 다른 함수를 호출하는 것을 말한다.
def display():      #2
    num = int(input("1_기본급 | 2_일 한 일수 : "))
    if num == 1:
        result1 = alba()
    elif num == 2:
        day = int(input("몇 일 동안 일 했니? : "))
        result1 = alba(day)
    print("당신의 급여는 %d원입니다." % result1)
    
def alba(day = 30, time = 8, pay = 9160):       #3
    result2 = day * time * pay
    return result2

display()       #4

- 이중함수를 이용한 사칙연산
def dispay():
    num1, num2 = int(input("숫자1 입력 : ")), int(input("숫자2 입력 : "))
    a = input("기호 입력 : ")
    res = cal(a, num1, num2)
    print("{} {} {} = {}" .format(num1, a, num2, res))
    
def cal(a, num1, num2):
    if a == '+':
        return num1 + num2 
    elif a == '-':
        return num1 - num2
    elif a == '*':
        return num1 * num2
    elif a == '/':
        return num1 / num2
    
dispay()

7.5 기타
- 매개변수의 초기값 지정
def say_samadal(name, old, man = True):
    print("나의 이름은 %s입니다." % name)
    print("나의 나이은 %d입니다." % old)
    if man:
        print("Male")
    else:
        print("Female")
say_samadal("사마달", 20)

- 지역변수와 전역변수
a = 2           # 함수 밖에 선언된 변수(전역변수. 소스 전반에 걸쳐서 영향을 주는 변수)
def vartest(a):
    a = 4           # 함수 안에 선언된 변수. 함수 안에서만 영향을 주는 변수
    a = a + 1       # 전역변수보다 지역변수가 우선한다.
    return a
b = vartest(a)
print(b)

- 키워드 파라미터(**kwargs)
def print_kwargs(**kwargs):     # 변수명 갯수와 무관하게 입력받은 내용 모두 출력
    print(kwargs)
print_kwargs(name='samadal', age = 3)

- 함수의 결과값은 반드시 한 개만 존재
def add_and_mul(a, b):   
    ab = a + b
    ba = b * a
    print(type(ab))
    print(type(ba))
    return ab, ba

print(add_and_mul(3, 4))            # (7, 12) 튜플로 출력 // 실제로 쓰지 않음, 리턴값은 하나만 존재해야 함

- Lambda
    : 함수와 동일한 역할을 수행한다.
    : 매개변수를 이용한 표현식을 사용한다.
    : return문은 사용할 수 없다.
    : 표현식
        lambda 매개변수1, 매개변수2, .... : 계산식
'''
x, y  = 3, 4
def sum1(a, b):
    return a + b
print(sum1(x, y))

sum2 = lambda a, b: a + b
print(sum2(x,y))
#print(lambda a, b: a + b)

    

    