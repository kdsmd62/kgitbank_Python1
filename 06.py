'''
2. 자료형
2.3 List
    - 유형별 구분
        리스트명 = [요소1, 요소2, 요소3, ...]
    - 실습    
    a = []
    b = [1, 2, 3]
    c = ['Samadal', 'sam', 'madal']
    d = [1, 2, 'Samadal', 'sam']
    e = [1, 2, ['Samadal', 'sam']]
    print(a, b, c, d, e)
    print(type(a))
    print("%s\n%s\n%s\n%s\n%s" % (a, b, c, d, e))
        
    a = [1, 2, 3]       # 1. 단일 인덱싱
    print(a)
    print(type(a[0]))       # 리스트 안에 숫자는 모두 정수이다.
    print(a[1] + a[2])
    print(a[2] - a[1])
    print(a[-3])
        
    b = [1, 2, 3, ['a', 'b', 'c']]
    print(b)
    print(b[0])
    print(b[1])
    print(b[2])
    print(b[3][0])
    print("%s" % (b[3][0]))

    c = [1, 2, ['a', 'b', ['kg', 'It', 'Bank']]]
    print(c)        # [1, 2, ['a', 'b', ['kg', 'It', 'Bank']]]
    print(c[0])     # 1
    print(c[2][1])      # b
    print(c[2][2][1])       # It
    print(c[-1][0])     # a

2.3.3 리스트 슬라이싱
    a = [1, 2, 3]
    print(a[:])     # 리스트의 출력은 모두 리스트
    print(a[1:])
    print(a[:2])

    b = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
    print(b[2:5])       # [3, ['a', 'b', 'c'], 4]
    print(b[3][:2])     # ['a', 'b']    # 인덱싱과 슬라이싱이 함께 적용 * 슬라이싱은 마지막 숫자 -1 자리값까지 출력

2.3.4 리스트 기타
    - 리스트 연산
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(a + b)        # 실제 연산되지 않고 목록을 더한다.
    print(a * 2)        # 두 번 반복되어 출력된다.
    print(a[2] + 4)
    - 리스트 수정
    a = [1, 2, 3]
    a[2] = 4
    print(a)        # [1, 2, 4]

    a[1] = ['a', 'b', 'c']
    print(a)        # [1, ['a', 'b', 'c'], 4]

    print(a[1:2])       # [['a', 'b', 'c']]     * 슬라이싱은 리스트의 일부분을 리스트 형태로 자른다
    print(a[1])         # ['a', 'b', 'c']       * 인덱싱은 리스트 안에 있는 '값'을 출력한다.
    a[1:2] =  ['d', 'e', 'f']
    print(a)        # # [1, 'd', 'e', 'f', 4]
    
    - 리스트 삭제
    a = [1, ['a', 'b', 'c'], 'b', 'c', 4]
    print(a[1:3])       # [['a', 'b', 'c'], 'b']
    a[1:3] = []
    print(a)        # [1,'c', 4]

    a = [1, ['a', 'b', 'c'], 'b', 'c', 4]
    print(a[1:3])       # [['a', 'b', 'c'], 'b']
    a[1:3] = []
    print(a)        # [1,'c', 4]

    b = [1, 2, ['a', 'b', ['Kg', 'It', 'Bank'], 4, ['c', 'd']]]
    print(b)        # [1, 2, ['a', 'b', ['Kg', 'It', 'Bank'], 4, ['c', 'd']]]
    print(b[2][2][1])       # 실행 전 확인
    b[2][2][1] = []
    print(b)        # # [1, 2, ['a', 'b', ['Kg', [], 'Bank'], 4, ['c', 'd']]]
    del b[2][2][1]      # 리스트 안의 값 삭제
    print(b)
    b[2][2][2:] = []
    print(b)

    a = [500, 200, 300, 400]
    sum = 0     # 조건문의 합을 구할 때는 반드시 초기값을 지정해야 한다.
    sum = a[0] + a[1] + a[2] + a[3]
    print(sum)
    
    - Cast 연산
    a, b = [1, 2, 3], '48'
    print(type(a), type(b))
    print(type(a[2]), type(b))
    print(a[2])
    print(int(b))
    print(type(int(b)))
    aa, aaa = str(a[1]), str(a[2])
    print(type(aa), type(aaa))
    
2.3.5 리스트 관련 함수
    a = [1, 2, 3]
    a.append(4)
    print(a)
    a.append([5, 6])      # list.append()는 하나의 인수만 가능하다. 그래서 list로 묶어줌
    print(a)
    # print(a.append([5,6]))        # 1. 추가. 변수명.append([인수1, 인수2, 인수3, ...])

    a.extend([5,6])
    print(a)                        # 2. 확장. 변수명.extend([인수1, 인수2, 인수3, ...])
    #print(a.extend([5,6]))      # 출력은 되지만 오류(None)

    b = [7, 8]
    a.extend(b)
    print(a)

    a = ['z', 'b', 't', 'c']
    b = [1, 4, 3, 2]
    a.reverse()     # 3. 뒤집기.    변수명.reverse()
    print(a)

    a.sort()        # 4. 정렬.  변수명.sort()
    print(a)
    print(a.sort())     # 출력은 되지만 오류(None)

    b.reverse()
    print(b)
    b.sort()
    print(b)

    c = b.sort()
    print(c)

    a = [1, 7, 13]
    b1 = a.index(1)         # 위치 확인. 변수명.index(위치를 확인하고자 하는 리스트 값)
    b2 = a.index(7)
    #b2 = a.index(3)            # 리스트 안에 '3'이 없기 때문에 오류
    b3 = a.index(13)
    print(b1, b2, b3)

    a = [1, 7, 13]
    b = [1, 2, 3, 1, 2, 3]
    a.insert(0, 4)          # 6. 삽입. 변수명.insert(값을 삽입할 위치, 삽입할 값)
    print(a)
    a.insert(3, 5)      
    print(a)            # 실행하기 전에 확인      * 대체가 아니라 '삽입'

    b.remove(3)         # 7. 삭제. 변수명.remove(삭제할 첫 번째로 나오는 값)
    print(b)
    b.remove(2)
    print(b)

    a = [3, 2, 1]
    b = [1, 2, 3, 4, 5]
    c = [1, 2, 2, 3, 3, 3]
    a.pop()         # 8. 꺼내기.    변수명.pop(꺼낼 숫자의 위치)
    print(a)        # 없으면 맨 뒤에서부터 꺼낸다.
    a.pop()
    print(a)

    b.pop(2)
    print(b)

    print(c.count(2))       # 9. 갯수 세기.     변수명.count(갯수를 셀 숫자 또는 문자)

2.4 Tuple(튜플)
2.4.1 튜플 자료형의 특징
    - 리스트와 거의 모두 동일하지만 값의 생성, 수정, 삭제가 불가능하다.
    - 문자열(%, .format(), f-Stirng, [List], (Tuple), {Dictionary})
2.4.2 튜플 자료형의 유형
    t1 = ()
    t2 = (, )
    t3 = (1, 2, 3)
    t3 = 1, 2, 3
    t5 = ('a', 'b, ('ab', 'ba'))
    t6 = (1, 2, 'a', 'b')
    print(t6)
    #t6[0] = 4          # 튜플 수정 불가
    #print(t6)

    #del t6[1]           # 튜플 삭제 불가
    #print(t6)
'''
