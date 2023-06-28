'''
6. 제어문 - while
6.3 실습
    - 커피 한 잔의 값은 300원이고 오늘 판매할 수량은 10잔이 준비되어 있다.
    - 커피 한 잔을 뽑을 때마다 판매할 수량은 1잔씩 차감되고 입력된 금액은 차감된 금액을 제하고 거스름돈을 돌려주는 소스
    
    1) 내가 만든 코드
    price, coffee = 300, 10
    while True:
        money = int(input("금액을 입력하십시오 : "))
        if money >= price:
            coffee -= 1
            rest_money = money - price
            print("거스름돈 : %d원\n남은커피 수량 : %d잔\n" % (rest_money, coffee))
        else: print("금액이 부족합니다.\n")
        if coffee == 0:
            print("영업종료")
            break
            
    2) 강사님 코드
    coffee = 10
    while True:
        money = int(input("돈을 넣어주세요 : "))
        if money == 300:            # 한 잔만 주문
            print("한 잔만 가능한 돈이므로 커피를 줍니다.")
            coffee -= 1
            print("남은 커피 수량은 %d잔입니다\n" % coffee)
        elif money > 300:           # 주문하고 거스름돈 돌려 받고
            print("거스름돈 %d원을 주고 커피도 줍니다." % (money - 300))
            coffee -= 1
            print("남은 커피 수량은 %d잔닙니다\n" % coffee)
        else:           # 주문할 돈이 부족할 때
            print("입력받은 돈은 %d원이므로 돈을 다시 돌려주고 커피를 안 줍니다." % money)
            print("남은 커피수량은 %d잔입니다\n" % coffee)
        if not coffee:
            print("준비된 10잔의 커피는 모두 소진되었습니다.\n판매를 중지합니다.")
            break
            
    - 현재 원달러 환율은 1,146.4원이고 엔화 환율은 1,021.29원이다.
    - 500달러를 환전하면 몇 엔이 되겠는가?          * 내가 짠 코드와 알고리즘 동일, 변수값만 수정함
    
    wpd = 1146.4
    wpy = 1021.29
    money = 500 * wpd
    result = money / wpy
    print("500달러는 %.2f엔 입니다." % result)
    
    - x극장 영화표는 11,000원이고 y극장 영화표는 9,500원일 때
    - 각 극장 수익이 x극장(5,390,000,000), y극장(7,521,245,000)이라고 한다.
    - 각 극장의 관람객수는 얼마이고 두 극장의 총 관람객 수는 얼마인가?
    - 그리고 각 극장의 점유율은 얼마인가?           * 내가 짠 코드와 알고리즘 동일, 콤마만 가독성을 위해 내가 추가함
    
    x_price, y_price = 11000, 9500                      # 영화표 가격
    x_profit, y_profit = 5390000000, 7521245000         # 극장 수익
    x_spec = int(x_profit / x_price)                    # 관람객수
    y_spec = int(y_profit / y_price)
    print("1. X극장의 관람객 수 : {:,d}명 | Y극장의 관람객 수 :{:,d}명" .format(x_spec, y_spec))
    total_spec = x_spec + y_spec
    print("2. 총 관람객 수 : {:,d}명".format(total_spec))
    x_pi = x_spec / total_spec * 100            # X극장의 점유율
    y_pi = y_spec / total_spec * 100            # Y극장의 점유율
    print("3. X극장의 점유율 : %.2f(%%) | Y극장의 점유율 : %.2f(%%)" % (x_pi, y_pi))
    
    - xx은행의 연 이자율이 2.5%라고 했을 때 2500만원이 입금되어 있는 통장의 3개월 뒤
    - 통장 잔액과 이를 달러 및 엔화로 환전할 때의 금액은 얼마인가?
    
    d, e, year, bankbook = 1146.4, 1021.29, 0.025, 25000000
    month = year / 12 * 3

    interest = bankbook * month         # 3개월치에 해당하는 이자
    money = bankbook + interest         # 원금과 이자를 합한 최종금액
    print("원금(%d) | 이자(%d) | 원금+이자(%d)" % (bankbook, interest, money))

    wtd = money / d
    wte = money / e
    print("달러 환전 : %.1f | 엔화 환전 : %.2f" % (wtd, wte))
    
    - 담배 한 갑의 가격은 4,500원이고 하루 한 갑 반씩 담배를 피우는 사람의 경우
    - 5000만원 가량의 차량을 구입하기 위해서는 몇 년동안 금연을 해야하는가?
    1) 나
    per, tabacco, car = 1.5, 4500, 50000000
    ppd = tabacco * per         # 하루 소비 비용
    day = car / ppd             # 금연기간(단위 : 하루)
    year = day / 365            # 금연기간(단위 : 년)
    print("금연기간 : %.2f년" % year)
    2) 강사님
    cigar = 4500
    daycigar = cigar + cigar/2
    print("1. 하루에 지출되는 금액 : %d원" % daycigar)
    car = 50000000 / daycigar
    print("2. 차량 구매를 위한 일 수 : %d일" % car)
    year = car / 365
    print("3. 차량 구매를 금연 기간 : %.1f년" % year)

7. 함수
7.1 개요
    - 어떤 내용이 소스 내에서 지속적으로 반복될 경우 소스의 길이가 늘어나게 된다.
    - 이와 같이 반복되는 소스의 내용을 임의의 형태로 묶어두고 필요할 때 불러서 사용하면 된다.
    - 즉, 소스의 형태를 간결하게 할 수 있는 기능이 함수이다.
7.2 구조
    - 형식1.
        def 함수명(매개변수):
            <수행할 문장1>
            <수행할 문장1>
            ...
    형식2.
        def 함수명(매개변수):
            <수행할 문장>
    형식3. 입력값이 몇 개인지 모를때
        def 함수명(*매개변수):
            <수행할 문장>
7.3 실습
            
'''
# 함수식(사칙연산)
x, y = 4, 2
# number(a, b)          # 매개변수는 항상 '함수 선언부' 보다 하위에 위치해야 한다.
def number(a, b):       # 함수 선언부(매개변수며은 같지 않아도 되지만 갯수는 반드시 일치시켜야 한다.)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    
number(x, y)            # 함수 호출









    
