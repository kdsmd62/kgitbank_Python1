'''
7. 함수
7.5 기타
- lambda
- 일반함수 사용
def num(*args):
    sum = 0
    for i in args:
        sum += i
    avg = sum / len(args)
    return avg
print(num(3, 4, 5, 6, 7))
- lambda로 변환
a, b, c, d, e = 3, 4, 5, 6, 7
samadal = lambda a, b, c, d, e : (a + b + c + d + e) / 4
print(samadal(a, b, c, d, e))

7.6 입력과 출력(외부에 저장된 파일 읽기)
    - 파일생성
        : 특징
            ; 자바에서의... => 객체 = 메서드()
            ; 파일이 있으면 내용을 삭제하고 없으면 지정 경로에 생성
            ; 문법
                파일객체(Object) = oepn("경로명\파일명", "열기모드(r(읽기), w(쓰기), a(추가))"
                파일객체.close()
 
a = open("samadal.txt", "w")            # 이렇게는 사용 안 한다.
a.close()

a = open("D:\pyt\samadal.txt", "w")            # 경로는 영어여야함, 폴더만들때 '_'사용해서 만들면 오류덜남(?)
a.close()

    - 쓰기 모드로 파일 열고 입력
a = open("D:\pyt\hi.doc", "w")
for i in range(1, 11):
    text = "%d번째 줄입니다\n" % i
    a.write(text)
a.close()

a = open("D:\pyt\samadal.txt", "w")
for i in range(1, 11):
    text = "%d번째 줄입니다\n" % i
    a.write(text)
a.close()

     - 읽기모드로 파일 한줄씩 읽기
a = open("D:\pyt\samadal.txt", "r")
while True:                     # while문 사용해서 전체내용 출력
    line = a.readline()         # 1. readline()함수 : 한 줄만 출력
    print(line, end='')   
    if not line: break          # if 'len(line) == 0: break' 도 가능
a.close()

a = open("D:\pyt\samadal.txt", "r")
lines = a.readlines()           # 2. readlines()함수 : 모든 줄 출력(리스트 형식으로 출력)
for line in lines:             
    print(lines)
a.close()

a = open("D:\pyt\samadal.txt", "r")
data = a.read()         #3. read()함수 : 모든 줄 출력(문서 내용 그대로 출력)
print(data)
a.close()

a = open("D:\pyt\samadal.txt", "a")         # 4. write()함수 : 파일에 새로운 내용을 추가하기
for i in range(11, 21):                     # open() 함수에서 a(add) 추가하기 모드로 열었기 때문에
    data = "%d번째 줄입니다\n" % i
    a.write(data)           
a.close()

a = open("D:\pyt\samadal.txt", "w")         # 기존 파일의 내용이 모두 삭제되고 신규 내용만 저장된다.
a.write("MADAL")
a.close() 

a = open("D:\pyt\samadal.txt", "w")         # 5. with ~ as문 : close()함수 없이 자동으로 열고 닫는다.
a.write("MADAL")
a.close() 

# 10줄 다시 생성
a = open("D:\pyt\samadal.txt", "w")         
for i in range(1, 11):
    data = "%d번째 줄입니다\n" % i
    a.write(data)
a.close()          

with open("D:\pyt\samadal.txt", "w") as i:
    i.write('samadal') 
    
with open("D:\pyt\samadal.txt", "w") as a:          # a라는 대표명으로 문서를 열어라!
    for i in range(1, 11):
        text = "%d번째 줄입니다\n" % i
        a.write(text)
        
# 6. sys 모듈로 매개변수 주기
import sys          # 파이썬 시스템의 내장 모듈(Module)
args = sys.argv[1:]     # 실행순서
for i in args:
    print(i)
    
7.7 실습
    - 구구단을 3가지 방법(함수 미사용, 단일 함수 사용, 이중 함수 사용)으로 구현
    
# 함수 미사용 (내코드 = 강사님코드)
for i in range(1,10):
    for j in range(2,10):
        res = i * j
        print("{} x {} = {}".format(j, i, res), end='\t')
    print("")

# 단일 함수 사용 (내 코드)

def mul(*args):         # args 쓰고 싶어서 만든 함수ㅎ
    for i in range(1, 10):
        for j in args:
            res = i * j
            print("{} x {} = {}".format(j, i, res), end='\t')
        print("")
        
mul(1, 2, 3, 4, 5, 6)           # 원하는 단수만 출력할 수 있게 함

# 이중함수 사용 (내 코드)

def mul(a, b):
    for i in range(1,10):
        res = a * i
        if b == 1:
            print("{} x {} = {}".format(a, i, res))
        elif b == 2:
            print("{} x {} = {}".format(a, i, res), end="\t")

def display():
    num = int(input("출력 단 수 : "))
    arr = int(input("출력 형태 : 1_세로 | 2_가로 : "))
    mul(num, arr)
    
display() 

* 강사님 코드

def gugu1():                # 구구단을 구성하는 함수
    for i in range(1,10):
        for j in range(2,10):
            print(j,'x',i,'=',gugu2(i,j),end="\t")          # 값을 곱하는 과정은 gugu2() 함수를 이용
        print('')
        
def gugu2(a, b):            # 값을 곱해주는 함수
    mul = a * b
    return mul

gugu1()

# 강사님 코드2

def gugu1():                # 구구단을 구성하는 함수
    for i in range(1,10):
        for j in range(2,10):
            #print("{} x {} = {}".format(j, i, i*j), end="\t")
            print(gugu2(i, j),end="\t")          # 값을 곱하는 과정은 gugu2() 함수를 이용
        print('')
        
def gugu2(i, j):            # 값을 곱해주는 함수
    str = "{} x {} = {}".format(j, i, i*j)
    #str = "%d x %d = %d" % (j, i, i*j)
    return str

gugu1()

'''
def gugu1():                # 구구단을 구성하는 함수
    for i in range(1,10):
        for j in range(2,10):
            #print("{} x {} = {}".format(j, i, i*j), end="\t")
            print(gugu2(i, j),end="\t")          # 값을 곱하는 과정은 gugu2() 함수를 이용
        print('')
        
def gugu2(i, j):            # 값을 곱해주는 함수
    str = "{} x {} = {}".format(j, i, i*j)
    #str = "%d x %d = %d" % (j, i, i*j)
    return str

gugu1()




