'''
4. 제어문 - if
4.4
    - 실습(임의의 값을 입력 받은 후 윤년을 구하는 소스)
        : 4의 배수는 윤년이고 그 이외는 모두 평년
        : 4의 배수이면서 100의 배수인 경우는 평년 그 이외는 모두 윤년
        : 4와 100의 배수이면서 400의 배수인 경우는 윤년, 그 이외는 모두 평년
        
        year = int(input("년도 입력 : "))           #내가 만든 코드랑 거의 똑같아서 따로 필기안함

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0: tmp = "윤년"
                else: tmp = "평년"
            else: tmp = "윤년"
        else: tmp = "평년"

        print("%d년은 %s입니다." % (year, tmp))
        
    - 실습(사용자로부터 'Gbyte'를 입력받은 후 'byte, Kbyte, Mbyte'로 출력하는 소스)
        : 원하는 용량을 선택을 통해서 출력하도록 한다.
        
    cap = int(input("용량(Gbyte) : "))          # 강사님 코드랑 많이 다르긴한데 ,,, 지수표현만 주의할 것
    unit = input("원하는 용량을 선택하시오 : 1. byte | 2. Kbyte | 3. Mbyte\n")

    if unit == '1': 
        tmp1 = "{:,}".format(int(cap * 10e8))
        tmp2 = "byte"
    elif unit == '2' : 
        tmp1 = "{:,}".format(int(cap * 10e5))
        tmp2 = "Kbyte"
    elif unit == '3' : 
        tmp1 = "{:,}".format(int(cap * 10e2))
        tmp2 = "Mbyte"

    print("%d Gbyte = %s %s" % (cap, tmp1, tmp2))
    
5. 제어문 - for
5.1 단일 for문
    : 문법
        for 변수 in range(초기값, 끝값, 증감값):
            수행코드(종속문장)
            
        for 변수 in 리스트(문자열 또는 튜플)
            수행코드1
            수행코드2
            ...
            
    : 실습
    
    # 1. 초기값, 끝값, 증감값 유무에 따른 실습
    i = 1101                    # 적용이 안되는 변수
    #for i in range(1, 10):      # range(초기값, 끝값, x)
    #    print("i = %d" % i)
        
    #for i in range(10):      # range(x, 끝값, x)
    #    print("i = %d" % i)  # 초기값이 없는 경우 '0'부터 출력
        
    #for i in range(10, 2):      # range(초기값, 끝값, x)
    #   print("i = %d" % i)     # 조건에 맞지 않기 때문에 오류(출력x)

    #for i in range(0, 10, 2):      # range(초기값, 끝값, 증감값)
    #   print("i = %d" % i)     
    
    #for i in range(1, 11, 1):      # range(초기값, 끝값, 증감값)
    #   print("i = %d" % i)         # 끝값은 '끝값-1'이 될 때까지만 출력
    
    for i in range(1, 11, 1):      # range(초기값, 끝값, 증감값)
    if i % 2 == 1: print("i(OK) : {}".format(i))
    else: print("i(Fail) : %d" % i)   
    
    #2. List
    for a in 'one', 'two', 'three':         # 그냥 문자열
        print(a)
        
    for b in 1, 2, 3:                       # 그냥 숫자
        print(b)
        
    for c in range(1, 12):
        if c < 11: print("작은수 까지 출력(%d)" % c)
        else: print("크거나 같은 수 출력(%d)" % c)

    test_list = ['one', 'two', 'three']         # 리스트
    for a in test_list[:]:                      # 슬라이싱      
        print(a)
        
    # 3. 1부터 10까지의 합을 구하는 소스

    sum = 0         # 값이 누적되는 경우에는 반드시 누적되는 변수를 초기화 해야 한다.
    mod = ''

    for i in range(1, 11, 1):
        sum += i            # sum = sum + 1
        if i < 10:          # 내가 추가로 붙인 코드
            mod += str(i) + " + "
        else: mod += str(i)
        
    print("%s = %d\n" % (mod, sum))

    # 4. 1부터 51까지의 숫자를 출력하는데 7의 배수인 경우와 아닌 경우의 소스 코딩

    for i in range(1, 52, 1):
        if i % 7 == 0:          # '!=' 사용하면 어떻게 될 지도 생각
            print("%d는 7의 배수 : Ok" % i)
        else: print("%d는 7의 배수 : No" % i)
        
    list1 = []          # 내가 만든 코드
    list2 = []

    for i in range(1, 52, 1):
        if i % 7 == 0:
            list1.append(i)
        else: 
            list2.append(i)
    print("\n7의 배수 : {}\nnone 7의 배수 : {}\n".format(list1, list2))

    # 5. 누적에 따른 합산(값(3가지 요소)을 입력해서 합산을 하는 소스)
    j = sum = var_start = var_end = grow = 0 # 값이 같은 변수들은 이렇게 선언해도 된다.
    mod = ''
    var_start = int(input("시작값 입력 : "))
    var_end = int(input("마지막값 입력 : "))
    grow = int(input("증감값 입력 : "))

    for j in range(var_start, var_end + 1, grow):
        sum += j
        if j < var_end:          # 내가 추가로 붙인 코드
            mod += str(j) + " + "
        else: mod += str(j)

    print("%s = %d" % (mod, sum))
    
    # 6. 임의의 값을 입력받은 후 0부터 입력받은 값까지 단계별 출력과 합계를 구하는 소스
    a = [(1, 2), (3, 4), (5, 6)]            # 리스트 안에 튜플이 정의
    for (samadal, madal) in a:
        print("%d + %d = %d" % (samadal, madal, (samadal + madal)))

    # 7. 다음의 값이 주어졌을 때 합격, 불합격 여부를 출력하는 소스
        : 60점 미만인 학생을 '불합격'을, 이 이외에는 모두 '합격'을 출력
        : 주어진 값(95, 25, 67, 45, 80)
        
    list = [95, 25, 67, 45, 80]

    for grade in list:
        if grade < 60: print("점수 : %d | 결과 : 불합격" % grade)
        else: print("점수 : %d | 결과 : 합격" % grade)
        
    num = 0

    for i in list:
        num += 1
        if i >= 60:
            print("%d번 학생은 %d점이므로 합격입니다." % (num, i))
        else:
            print("%d번 학생은 %d점이므로 불합격입니다." % (num, i))

'''


