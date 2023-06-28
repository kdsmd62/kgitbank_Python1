''''
# 7. 
a = int(input("1번 학생의 점수 : "))
b = int(input("2번 학생의 점수 : "))
c = int(input("3번 학생의 점수 : "))
d = int(input("4번 학생의 점수 : "))
e = int(input("5번 학생의 점수 : "))

mark = [a, b, c, d, e]
cnt = 0

for i in mark:
    cnt = cnt + 1
    if i > 60:
        print("%d번 학생은 %d점이므로 합격입니다" % (cnt, i))
    else: print("%d번 학생은 %d점이므로 불합격입니다" % (cnt, i))
    
# 8. A학급에 총 10명의 학생이 있고 이 학생들의 중간고사 점수는 다음과 같다.
    : 이 학생들의 평균 점수를 구한다. 
    : 주어진 값(70, 60, 55, 75, 95, 90, 80, 80, 85, 100)
    
    mark = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100, 0]

    sum = 0
    for i in mark:
        sum += i
    avg = sum / 10
    print("합계(%d), 평균(%d점)" % (sum, avg))

    sum2 = 0
    for i in range(10):
        sum2 += mark[i]
    avg2 = sum2 / 10
    print("합계(%d), 평균(%d점)" % (sum2, avg2))

    sum3 = 0
    for i in range(mark[0], mark[9], 1):            # a[0] ~ a[9]
        sum3 += i
        print(sum3)
    avg3 = sum3 / 10
    print("합계(%d), 평균(%d점)" % (sum3, avg3))

# 9. 하단의 리스트 중에서 홀수에만 2를 곱하고 출력하는 소스
    : 주어진 값[1, 2, 3, 4, 5]
    
    a = [1, 2, 3, 4, 5]
    result = []

    for i in a:
        if i % 2 == 1:
            result.append(i * 2)
    print(result) 

5.2 다중 for문
    : 문법
        for 변수 in range(초기값1, 끝값1, 증감값1):
            수행코드(종속문장)
            for 변수 in 리스트(초기값2, 끝값2, 증감값2)
                수행코드1
                수행코드2
                ...
    : 실습(구구단)
    : 단 구분없이 세로로 모두 출력
    for i in range(2, 10, 1):
        #print("\n%d단 시작!" % i)
        for j in range(1, 10, 1):
            print ("%d * %d = %d" % (i, j, (i * j)))
        print("")
        
    : 가로로 출력
    for i in range(2, 10, 1):           # i, j 의 위치를 바꿔서 세로, 가로로 단이 출력되게 바꾸어 보기
        for j in range(1, 10, 1):
        print(j,' x ',i,' = ',i * j, end='\t')  # end 속성을 생략하면 기본값이 \n 이 들어감으로 다른값을 넣어 가로로 출력되게 한다
    print("")
    
    : 입력된 값의 단수 출력
    a = int(input("입력 : "))
    for i in range(a, a+1, 1):
        for j in range(1, 10):
            print("%d * %d = %d" % (i,j,i*j))  # end 속성을 생략하면 기본값이 \n 이 들어감으로 다른값을 넣어 가로로 출력되게 한다
        print("")
        
6. 제어문 - While
6.1 개요
    - 프로그램 실행 후 종속 문장 등의 실행을 계속 진행할 수 있도록 한다.
    - 조건문이 부정확할 경우 무한루프에 빠지기 쉽다. (무한 루프 종료 : ^ + C)
    - break문과 함께 사용한다.
6.2 문법
    while <조건문>:
        <수행할 문장1>
        <수행할 문장2>
        ...
6.3 실습
1)
while True:
    print("무한루프에서 빠져나오려면 터미널창에 포커스 후 ^+C 누르세요.")
2)
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었다." % treeHit)
    if treeHit == 10:
        print("끝.")
3)
number = 0
while number != 4:
    number = int(input("1_Add | 2_Del | 3_List | 4_Quit | 5_Name : "))
    if number == 4:
        break
4)
coffee, money = 5, 300      # 실제 적용되는 수가 아니기 때문에 아무거나 입력해도 된다.
while money:            # money 라는 변수가 값을 가지고 있다면. True를 입력해도 된다.
    print("커피 한 잔을 뽑습니다.")
    coffee -= 1         # 한 잔을 뽑았기 때문에
    print('남은 커피 수량은 %d잔입니다.\n' % coffee)
    if coffee == 0:
        print('오늘 준비한 수량은 모두 소진되었습니다.\n판매를 중지합니다.')
        break
4-1)
coffee, money = 5, 300     # 실제 적용되는 수가 아니기 때문에 아무거나 입력해도 된다.
while True:            # money 라는 변수가 값을 가지고 있다면. True를 입력해도 된다.
    print("커피 한 잔을 뽑습니다.")
    coffee -= 1         # 한 잔을 뽑았기 때문에
    money += 300
    print('남은 커피 수량은 %d잔이고 총 금액은 %d입니다.\n' % (coffee, money-300))
    if not coffee:
        print('오늘 준비한 수량은 모두 소진되었습니다.\n판매를 중지합니다.')
        break
5)
a = 0     
while a < 10:
    a += 1
    if a % 2 == 0:
        print("%d 진행. 짝수" % a)
6)
*
**
***
****
*****

a = 0
while a < 5:
    a += 1
    print("*" * a)          # print("=" * 50) 과 같은 방법으로 생각하면 된다.
    
7) 1부터 100까지의 자연수 중 3의 배수의 합을 구하는 소스
'''
num , sum = 1, 0
while num <= 100:
    if num % 3 == 0:
        sum += num
        print("%d + %d = %d" % (num, sum, sum+num))
    num += 1
    if num == 100: break

print("총 합은, %d이다" % sum)


    