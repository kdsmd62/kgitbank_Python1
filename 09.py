'''
4. 제어문 - if
4.3 단일 if문(if ~ else)
    - 실습(한 개의 문자열에 2개의 값이 들어있다. 이를 분리하고 분리된 각 값들에서 
            문자와 숫자를 또 한 번 분리한다.)
            kg = "나이:30, 키:180"
            
        kg = "나이:30, 키:180"
        itbank = kg.split(", ")
        print(kg)
        print(itbank)

        age = itbank[0].split(":")[1]
        height = itbank[1].split(":")[1]
        print(age, height)

        if int(age) <= 30 and int(height) >= 180:
            print(type(age), type(height))          # cast연산을 그때 그때 형변환을 해주는 것으로 선언한 내용에서 변동은 없다(?)
            print("정상적으로 분리되었습니다.")
        else:
            print("다시 한번 확인해주십시오.")
4.4 다중 if문
- 문법
    if <조건문>:
        <수행할 문장1>
        <수행할 문장2>
        ...
    elif <조건문>:
        <수행할 문장3>
        <수행할 문장4>
        ...
    elif <조건문>:
        <수행할 문장5>
        <수행할 문장6>
        ...
    else <조건문>:
        <수행할 문장7>
        <수행할 문장8>
        ...    
- 실습(3개의 정수값을 입력받은 후 비교해서 가장 큰 값과 가장 작은 값을 출력)

    a, b ,c = int(input("첫 번째 값 입력 : ")),int(input("두 번째 값 입력 : ")),int(input("세 번째 값 입력 : "))


    if a > b and a > c : max = a            # 1. elif 사용
    elif b > a and b > c : max = b
    elif c > a and c > b : max = c

    if a < b and a < c : min = a
    elif b < a and b < c : min = b
    elif c < a and c < b : min = c


    max = a                 # 2. 내가 만든 코드
    if b > max: max = b
    if c > max: max = c
        
    min = a
    if b < min: min = b
    if c < min: min = c
        
    print("가장 큰 값 : %d\n가장 작은 값 : %d" % (max, min))
    
- 실습(임의의 정수 값(날짜)을 입력 받고 이에 해당하는 요일을 출력하는 소스) 
    : 1(월요일) ~ 7(일요일)
    : 만약 올바르지 않은 일력값일 경우 재입력을 권하는 문구 출력
    
    day = int(input("날짜 입력 : "))

    if 1 <= day <= 31:
        if day % 7 == 1: print("월요일")
        elif day % 7 == 2: print("화요일")
        elif day % 7 == 3: print("수요일")
        elif day % 7 == 4: print("목요일")
        elif day % 7 == 5: print("금요일")
        elif day % 7 == 6: print("토요일")
        elif day % 7 == 7: print("일요일")
    else:
        print("제대로 된 값을 입력하시오.")
        
- 실습(임의의 정수값(1 ~ 24)을 입력 받아서 시간을 출력하는 소스)
    : 정오(12시), 자정(24시), 오전(1시 ~ 11시), 오후(13시 ~ 23시)
    : 만약 올바르지 않은 일력값일 경우 재입력을 권하는 문구 출력
    
    time = int(input("시간을 입력하시오 : "))

    if 1 <= time <= 24:
        if 1 <= time <= 11: print("오전")
        elif time == 12: print("정오")
        elif 13 <= time <= 23: print("오후")
        elif time == 24: print("자정")
    else: 
        print("제대로 된 값을 입력하시오.")
        
- 실습(임의의 값(이름, 키, 몸무게)을 입력 받은 후 비만도를 구하는 소스)
    : 비만도 결과 출력(100을 기준으로 코딩)
        100 미만이면, "저체중. 곧 가겠네요"
        100 이상이면 110 미만, "정상"
        110 이상 120 미만이면, "과체중. 먹는 것을 줄이세요"
        120 이상 130 미만이면, "비만. 곧 따라가겠네요."
        130 이상이면, "고도비반. 옆자리에 앉았겠군요."
    : 표준 체중 계산        표준 체중 = (현재 키 - 100) * 0.9
    : 비만도 계산           비만도(%) = 현재 체중 / 표준채중 * 100
    
    name = input("이름 : ")
    height = int(input("키 : "))
    weight = int(input("몸무게 : "))

    std_weight = (height - 100) * 0.9
    bmi = weight / std_weight * 100

    if bmi < 100: tmp = "저체중"            # if문 각각에 print()문 넣은 것도 해보기*
    elif 100 <= bmi < 110: tmp = "정상"
    elif 110 <= bmi < 120: tmp = "과체중"
    elif 120 <= bmi < 130: tmp = "비만"
    elif 130 <= bmi: tmp = "고도비만"
    print("{}님의 비만도({:.1f})와 상태({})의 결과입니다." .format(name, bmi, tmp))

'''







    

