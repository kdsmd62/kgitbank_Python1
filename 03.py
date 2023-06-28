'''
2. 자료형
2.2 문자열(형)
2.2.6 실습
    - 주어진 그림과 같이 구성하세요.
        print('=' * 19)
        print('\t /)/)')
        print('\t(  ..)')
        print('\t(  >♡')
        print('Have a Good Time.')
        print('=' * 20)

        a = '=' * 19
        b = '=' * 20
        print(a +'\n\t /)/)\n\t(  ..)\n\t(  >♡\n Have a Good Time.\n'+ b)

        print("=" * 20)
        print("\t/)/)")
        print("\t\b(   ..)")
        print("\t\b(   >♡")
        print(" Have a Good Time.")
        print("=" * 20)
        
        print("\t\t#### 회비 정보 ####")
        print("=" * 50)
        print(" 이름\t\t나이\t전화번호\t회비")
        print("=" * 50)
        print(' 홍길동\t\t' '\"15\"\t' '010-123-1234\t' '￦20,000')
        print(' 임꺽정\t\t'+'"20"\t'+'010-234-2345\t'+'￦30,000')
        print(' 김말이\t\t"28"\t010-345-3456\t￦50,000')
        print("-" * 50)
        print(" 총합계\t\t\t\t\t￦100,000")
        print("=" * 50)

2.2.7 문자열 인덱싱(Indexing)
    - 개요
        : 원하는 임의의 위치의 값을 출력
        : 책에서의 '목차'에 해당, 즉 '위치'를 표시
    - 인덱싱 요령
        : 앞에서 인덱싱(기호(-)가 없는 형태)할 때는 '0'부터 
        : 뒤에서 인덱싱(기호(-)가 있는 형태)할 때는 '1'부터
    - 실습
        a = "KgItBank, Samadal, Python"
        print(a)
        print(a[0])
        print(a[8])
        print(a[-1])
        print(a[-6])
        
        b = "Kg_It_Bank"
        print(b[3])
        c = b[3]        # 변수를 치환
        print(c)

        print('SAM', 'Samadal', sep=' = ')
        b = "Kg_It_Bank"
        d = b[0]
        print('d', b[0], sep=' = ')
        print('d', d, sep=' = ')
        print('b[0]', d, sep=' = ')
        print(10, 20, 30,sep="<")

        print(10, 20, 30,sep="% ")
        print('사마달', end="씨\n")     # end가 있을 경우에는 아랫줄이 모두 한 줄로 붙어서 출력
        print(10, 20, 30,sep="% ",end="%\n")
        print(10, 20, 30,end="%",sep="% ")
    
    - 출력 문구가 'C:\\Program Files\\Python310\\'과 같이 되게 하려면?
        print('C:','Program Files','Python310',sep='\\\\',end='\\\\')
        print('C:','Program Files','Python310',sep='\\''\\',end='\\''\\')
        print('\nC:\\\\Program Files\\\\Python310\\\\')
        print('C:\\\Program Files\\\Python310\\',end="\\")
        print('\nC:\\','Program Files\\','Python310\\',sep="\\",end="\\")
        print('\nC:','Program Files','Python310',sep='\\'*2,end='\\'*2)
        
2.2.8 문자열 슬라이싱(Slicing)
    -  개요
        : 원하는 임의의 값(범위)를 출력
    - 
    - 인덱싱과의 차이점
        : 인덱싱은 '지점'을 출력하고 슬라이싱은 '범위'를 출력
    - 실습
        a = 'Kg_It_Bank'
        b, c, d = a[2], a[3], a[4]
        print(b, c, d)

        e = a[0:4]      # 0 <= e < 4
        print(e)
        print(a[2:5])   # 2 <= a < 5
        print(a[3:])    # 3 <= a < 끝점+1       print(a[3:10])
        print(a[:3])    # 0 <= a < 3            print(a[0:3])
        print(a[3:-1])  # 3 <= a < -1
    - 문자열 치환
        a = "KgItBank20220107"
        name  = a[0:8]
        date = a[8:]
        print(name+date)
        print(name,'\n',date)   # 줄 바꿈 후 자동정렬이 안된다.
        print(name,'\n'+date)   # 줄 바꿈 후 자동정렬이 된다.
        print(name+'\n'+date)   # 줄 바꿈 후 자동정렬이 된다.
        print('name = ',name,'\ndate = ',date)
    - 'Pithon'을 3가지 요소(치환, 인덱싱, 슬라이싱)을 모두 사용해서 'Python'으로 출력되는 소스 코딩
        var = 'Pithon'           
        n1 = var[0]        # 인덱싱
        n2 = 'y'       # 인덱싱
        n3 = var[2:]       # 슬라이싱
        print(n1+n2+n3)
        print(n1,n2,n3)

        e = var[0]
        f = "thon"
        print(e,f,sep='y')

2.2.9 %문자열(매우중요)
    - 문자열 포맷 코드
        %d(정수), %s(문자열), %c(문자), %f(실수), %b(2진수), %o(8진수), %x(16진수)
    - 문법
        print("%유형1, %유형2, ..." % (값1, 값2, ...))
    - 실습
    # 2진수를 10진수로 표현
    print(0b1101010001110001)
    bin1 = 0b1101010001110001
    bin2 = 1101010001110001
    print("%d" % bin1)      # 정수형으로 변환된 후 출력
    print("%d" % bin2)      # 일반적인 숫자와 동일하게 출력
2.2.10 .format() 함수(매우중요)
    - 문법
        print("{0}{1}...".format(값1, 값2, ...))
    - 실습
        출력내용이 "사마달님의 나이는 200살입니다."인 것을 문자열로 표현
        a, name, age = "{}님의 나이는 %d살입니다", '사마달', 200
        print(a.format(name) % age)
        print("%s님의 나이는 {}살입니다".format(age) % name)
        print("{}님의 나이는 %s살입니다".format(name) % age)
        a, name, age = "{}님의 나이는 %d살입니다", '사마달', 200
print(a.format(name) % age)
print("%s님의 나이는 {}살입니다".format(age) % name)
print("{}님의 나이는 %s살입니다".format(name) % age)

b = "{0}님의 나이는 {1}살입니다"
c = "%s님의 나이는 %d살입니다"
d, e = '사마달', 200
print(b.format(d,e))
print(c % (d, e))

str = "대학교 : %s대학교\n학번 : %d\n이름 : %s"
str2 = "대학교 : {0}대학교\n학번 : {2}\n이름 : {1}"

univ, num, name = "한국", 201412713, "홍길동"
print(str % (univ,num, name))
print(str2.format(univ,name,num))
        - 변수의 값(사마달, 200)을 인덱싱 또는 슬라이싱으로 변경 후 같은 내용을 출력
'''
a = '사마달, 200'
print(a[:3], a[5:8])

b, c = a[:3], a[5:]
print('%s님의 나이는 %s살입니다' % (b,c))
print('{}님의 나이는 {}살입니다.'.format(b,c))


