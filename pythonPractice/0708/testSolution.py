cust_list = []
current = -1

while True:
    choice = input("""
    다음 중 작업 하실 메뉴를 입력하세요.
    I - 고객 정보 입력
    C - 현재 고객 정보 출력
    P - 이전 고객 정보 출력
    N - 다음 고객 정보 출력
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    """).upper()
    if choice == "I":
        print("고객 정보 입력")
        customer = {"name": "", "gender": "", "email": "", "birthyear": 0}
        name = input("이름을 입력하세요.")
        
        while True:
            gender = input("성별을(M/F) 입력하세요").upper()
            # if gender == "M" or gender == "F":
            if gender in ("M", "F", "O"):
                break
        email = input("이메일 주소를 입력하세요")
        birthyear = int(input("출생년도를 입력하세요"))

        customer["name"] = name
        customer["gender"] = gender
        customer["email"] = email
        customer["birthyear"] = birthyear
        # print(customer)
        cust_list.append(customer)
        current = len(cust_list)-1
        # print(cust_list[current])
    elif choice == "C":
        print("현재 고객 정보 출력")
        if current >= 0:
            print(cust_list[current])
        else:
            print("입력된 정보가 없읍니다.")
    elif choice == "P":
        print("이전 고객 정보 출력")
        if current <=0 or len(cust_list) == 0:
            print("첫 번째 고객 입니다.")
        else:
            current -= 1
            # current = current -1
            print(cust_list[current])
    elif choice == "N":
        print("다음 고객 정보 출력")
        if current >= len(cust_list)-1:
            print("마지막 고객 입니다")
        else:
            current = current + 1
            print(cust_list[current])
    elif choice == "U":
        print("고객 정보 입력")
        customer = {"name": "", "gender": "", "email": "", "birthyear": 0}
        name = input("이름을 입력하세요.")
        gender = input("성별을(M/F) 입력하세요").upper()
        email = input("이메일 주소를 입력하세요")
        birthyear = int(input("출생년도를 입력하세요"))

        customer["name"] = name
        customer["gender"] = gender
        customer["email"] = email
        customer["birthyear"] = birthyear
        cust_list[current] = customer
    elif choice == "D":
        print("현재 고객 정보를 삭제합니다.")
        del cust_list[current]
        current = current - 1
    elif choice == "Q":
        print("프로그램을 종료합니다.")
        break
    else:
        print("메뉴를 정확히 입력 해 주세요.")
