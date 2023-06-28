'''
2.2.10 .format() 함수(매우중요)
    - 문법
        print("{0}{1}...".format(값1, 값2, ...))
    - 실습
        출력내용이 "사마달님의 나이는 200살입니다."인 것을 문자열로 표현
        a, name, age = "{}님의 나이는 %d살입니다", '사마달', 200
        print(a.format(name) % age)
        print("%s님의 나이는 {}살입니다".format(age) % name)
        print("{}님의 나이는 %s살입니다".format(name) % age)        # 
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

        변수의 값(사마달, 200)을 인덱싱 또는 슬라이싱으로 변경 후 같은 내용을 출력       
        a = '사마달, 200'
        print(a[:3], a[5:8])

        b, c = a[:3], a[5:]
        print('%s님의 나이는 %s살입니다' % (b,c))
        print('{}님의 나이는 {}살입니다.'.format(b,c))
    - 실습(출력문에 이름 넣기)   
        year, month = 2022, 1
        print("%d(KgItBank) %d(Samanal)" % (year, month))
        print("{}(KgItBank) {}(Samanal)".format(year, month))
            
        #print("{}(KgItBank) {}(Samanal)".format(year=2022, month=1))
        print("{}(KgItBank) {}(Samanal)".format('year=2022', 'month=1'))

        #print("{year}(KgItBank) {month}(Samanal)".format(2022,1))
        print("{year}(KgItBank) {month}(Samanal)".format(year=2022,month=1))        # 변수 선언 없이 한줄만 써도 ㄱㅊ
    -실습(정렬)
        print("{}".format('0123456789'))

        print("{0:<10}".format('samadal'))      # 왼쪽 정렬
        print("{:<10}".format('samadal'))      # 왼쪽 정렬
        print("{0:>10}".format('samadal'))      # 오른쪽 정렬
        print("{0:^10}".format('samadal'))      # 가운데 정렬
        print("{0:=^10}".format('samadal'))      # 가운데 정렬 후 공백을 '='로 채우기

        print("%-10s" % 'samadal')
        print("%10s" % 'samadal')
    - 실수(소수점표현)
        print("{0:f}".format(3.41214234))       # 실수는 기본적으로 6자리까지 출력
        print("{0:0.4f}".format(3.41214234))    # 소수점 4자리까지 출력
        print("{0:0.4f}".format(3.41215234))    # 반올림된다는 것을 알 수 있음

     - 기타
        print("{:,}".format(2000000))       # 천 자리 구분
2.2.11 f-string(매우 중요)
    - 문법
    name, age = 'Samadal', 30
    print("{} %d".format(name) % age)
    print("{} {}".format(name, age))
    print(f"{name} {age}")
    - 실습
        홍길동씨의 과목별 점수는 다음과 같다고 할 때 평균 점수를 구하는 소스(소수2자리까지)
        국어/85.5 영어/79.3 수학/95.4
        
        kor, math, eng = 85.5, 79.3, 95.4
        sum = kor + math + eng
        avg = sum / 3
        print(type(avg))
        print("%0.2f" % avg)
        print("{0:.2f}".format(avg))
    - 실습
        놀이공원을 가기 위해 11개의 지하철 역을 지나왔다.
        출발역에서 37분이 걸렸다면 한 역을 지나는데 걸리는 시간은 얼마인가?(소수 이하 두 자리)
        print("%0.2f" % (37/11))
    - 호텔 한 층의 높이는 260cm이다.
      총 14개의 층을 쓰고 있으며 1층만 500.23cm라면 이 건물의 높이는 총 몇 m인가?(소수 이하 두 자리)
        a = 260
        total = 500.23 + (a * 13)
        print("%0.2f" % (total * 0.01))
2.2.12 내장 함수
    a = 'samadal'           # 1. 문자 갯수 세기
    print(a.count('a'))

    b = 'KgItBank Samadal'  # 2. 문자 위치 알려주기 
    print(b.find('B'))
    print(b[4])
    print(b.index('k'))

    print("," .join("samadal"))     #3. 문자(열) 삽입하기

    c, d = "SAMADAL", "samadal"     #4. 대소문자 바꾸기
    print(c.lower())
    print(d.upper())

    e, f, g = "     hi","hi     ","e     hi"        #5. 공백지우기
    print(e.lstrip())       # left
    print(f.rstrip())       # right
    print(g.lstrip())
    print(g.strip())        # 양쪽(both side)

    h = "Samadal Madalgyo"      # 6. 문자열 교체하기
    print(h.replace("Madalgyo", "Sam"))

    i = "KgItBank Samadal"      # 7. 문자열 나누기
    j = "a:b:c:d"
    print(i.split())
    print(j.split(":"))
2.2.13 변수의 유형
    var1 , var2, var3 = '1', 1, 1.0
    print("{}".format(type(var1)))
    print("{}".format(type(var2)))
    print("{}".format(type(var3)))

    var1 , var2, var3 = int(var1) , float(var2), str(var3)      # Cast 연산(강제 형 변환)
    print("{}".format(type(var1)))
    print("{}".format(type(var2)))
    print("{}".format(type(var3)))
    
    - 실습
        홍길동씨의 주민등록번호는 881120-1068234 이다.
        '-' 을 기준으로 좌측과 우측으로 분리, 출력

'''
a = '881120-1068234'
print(a.split('-'))
print("%s-%s" % (a[:6],a[7:]))
print("{}-{}".format(a[:6],a[-7:]))

id = '881120-1068234'
id1, id2 = id[:6], id[-7:]
print("%s-%s" % (id1, id2))
print("{}-{}".format(id1, id2))
print(id.split('-'))        # 리스트 형식으로 출력되기 때문에 원하는 형식과 거리가 있음ㅠ
print(id.split('-')[0]+"-"+id.split('-')[1]) 