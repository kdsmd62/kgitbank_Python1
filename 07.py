'''
2. 자료형
2.4 Tuple(튜플)
2.4.3 기타
    a = (1, 2, 'a', 'b')
    b = (3, 4, 'c', 'd')
    print(a[0])         # 인덱싱
    print(b[3])

    print(a[:2])            # 슬라이싱
    print(b[1:])

    print(a + b)            # 연산
    print(b * 4)

    # (1, 2, 3)이라는 튜플에 4라는 값을 추가해서 (1, 2, 3, 4)가 출력되려면?
    a = (1, 2, 3)           # 추가
    b = (4,)               # 뒤에 ,을 넣어주는게 point *콤마 없이 값이 하나면 튜플 자체가 int(정수형) 으로 인식되어 연산이 불가능한듯(튜플만 튜플에 연결 가능)
    print(type(a), type(b))
    a += b                  # a = a + b
    print(a)
2.4.4 튜플 관련 함수
    tp = 100, 200, "함수", 200, '갯수'          # 변수명.index(변수의 값)
    print("tp안의 200의 위치 : ", tp.index(200), "번째 인덱스")
    pt = tp.index(100)
    print(type(tp), type(pt))
    print("tp안의 100의 위치 : %d번째 인덱스" % pt)
    print("tp안의 200의 갯수 :", tp.count(200), "개")       # 변수명.count(변수의 값)
2.5 Dictionary(딕셔너리)
2.5.1 유형
    - 묶음이 '{}'로 되어 있다.
    - { 'key1' : 'Value1', 'key2' : 'Value2', ...}
    - 연산시 입력한 순서대로 출력하지 않고 Key를 통한 값을 호출한다.
2.5.2 생성, 추가, 삭제 
    dic1 = {'name':'Samadal', 'phone':'010-1234-5678', 'birth':'0113'}      #1. 생성
    print(dic1)
    print(type(dic1))
    print(dic1['name'])         # Key는 변수로 사용된다.

    dic2 = {'1' : 'madal'}
    print(dic1['name'], dic2['1'])

    dic3 = {'a':[1, 2, 3]}
    print(dic1['name'], dic2['1'], dic3['a'])

    #print(dic1['Samadal'])      # KeyError(키 대신에 값을 호출인자로 사용할 수 없다)
    
    a = {1:'a'}         # 2. 추가
    print(a[1])
    a[20] = 'b'
    print(a)

    b = {}          # 3. 생성
    b['name'] = 'Samadal'
    print(b)
    b['madal'] = 'samadal'
    print(b)

    c = {2:'samadal'}
    
    #print(a + c)    : 딕셔너리는 다른 연상 방식과 달리 병합이 안된다.

    c[3] = [7, 8, 9]        # 딕셔너리는 Value는 리스트도 가능하다.
    print(c)

    del c[2]        # 키를 삭제하면 키와 함께 값도 삭제된다.
    print(c)
    del c['samadal']        # 삭제할 때는 키를 이용하고 값을 사용할 수 없다.
    print(c)
2.5.3 딕셔너리 관련 함수
    dic1 = {'name':'Samadal', 'phone':'010-1234-5678', 'birth':'0113'}   
    print(dic1.keys())              # 1. keys() : Key 목록을 출력
    #print(dic1['name'].keys)        # str(문자열) 속성에는 keys 속성이 없다.
    print(dic1.values())             # 2. values : value 목록을 출력
    a = list(dic1.keys())
    print(a)
    print(list(dic1.values()))

    print(dic1.items())             # 3. key와 value 목록을 한 개의 리스트로 출력

    print(dic1.clear())             # 4. key와 value 모두 삭제
    print(dic1)

    dic1 = {'name':'Samadal', 'phone':'010-1234-5678', 'birth':'0113'}   
    a = dic1.get('name')            # 5. key를 이용한 value 호출
    print(a)
    print(dic1.get('name'))

    b = dic1['name']
    print(b)

    print(dic1)
    print(dic1.get('madal', 'samadal'))     # Key에 'madal'이라는 키명이 없기 때문에 그냥 출력
    print(dic1.get('phone', 'birth'))       # get(키명, 키명)이기 때문에 앞에 것만 출력
                                            # get('없는 key명', '기본값')일 경우 기본값이 출력
                                            # get('있는 key명', '기본값')일 경우 있는 key명이 출력

    print('name' in dic1)                   # 6. Bool대수(참과 거짓을 판단)
    print('madal' in dic1)
2.5.4 실습
    - 학생의 인적사항 등록 후 검색하는 프로그램을 작성
    - 조건 : 학번, 이름, 주민번호, 등급(A, B, C, D, F)
           : 포함 내용(인적사항 등록, 학생 등록, 학생 수정, 전체학생보기, 학생 삭제, 종료)
           
    #std = {'sn': 201412713, 'name' : '홍길동', 'pn' : 1234561234567, 'grade':'A'}
    student = []        # 학생리스트
    std1 = {}       # 인적사항 등록1
    std1['sn'], std1['name'], std1['pn'], std1['grade'] = 202200001, 'Samadal', '123456-1234568', 'B'

    std2 = {}       # 인적사항 등록2
    std2['sn'], std2['name'], std2['pn'], std2['grade'] = 202200002, 'Jay', '123456-1234569', 'C'

    student.append(list(std1.values()))     # 학생1 등록
    student.append(list(std2.values()))     # 학생2 등록

    print(student)

    print(std1.get('name'))         # 학생1 의 이름 검색

    std1['name'] = 'Madal'     # 학생 수정
    student[0] = list(std1.values())

    print(student)      # 전체학생보기

    del student[0]      # 학생삭제

    print(student)

    namelist1 = {'number': 1234567, 'name' : '사마달', 'id' : '123456-1456789', 'grade':'B'}

    print("\n새로운 프로그램 시작\n")

    namelist2 = {}          # 1. 인적사항 등록
    namelist2['num'] = '1234568'
    namelist2['name'] = '마달이'
    namelist2['id'] = '123457-1456790'
    namelist2['grade'] = 'A'
    print(namelist2)

    print(namelist2.get('name'))            # 2. 학생 검색

    namelist2['grade'] = 'C'            # 3. 학생 수정
    print(namelist2)

    print(namelist2.items())            # 4. 전체 학생 보기

    del namelist2['name'], namelist2['num'], namelist2['id'], namelist2['grade']               # 5. 학생 삭제
    print(namelist2)

    print("프로그램을 종료합니다.")     # 6. 종료

3. 변수(Variable)
3.1 고정변수
    - ':'을 이용한 변수 생성
    a = [1, 2, 3]
    b = a[:]
    print(a, b)
    - copy를 이용한 변수 생성
    a = [1, 2, 3]
    from copy import copy           # copy를 Module 안에 있는 copy() 함수를 호출
    b = copy(a)
    print(copy(b))
    
3.2 가변 변수 : '변수명 = input()' (매우 중요)
var = input("값을 입력하세요 : ")
print("{}을 입력 받았다.".format(var))
print(type(var))            # input()함수로 입력된 모든 값은 항상 '문자열' 이다
print("%s을 입력 받았다." % var)
print(f'{var}을 입력 받았다')           # f'{변수명}'

var1 = input("문자열 입력 : ")          # input()함수로 입력된 모든 값은 항상 '문자열' 이다
var2 = input("정수 입력 : ")
print("이름은 %s 입니다" % var1)
print("나이는 {}살 입니다".format(var2))
print(type(var1), type(var2))

    - 두 개의 정수값을 받아서 사칙연산을 한다.
'''
var1 = input("정수1 입력 : ")
var2 = input("정수2 입력 : ")
print("%d + %d = %d" % (int(var1), int(var2), int(var1 +var2)))         #35
print("%d + %d = %d" % (int(var1), int(var2), int(var1) + int(var2)))   #8












                                        
                                    
                                        
