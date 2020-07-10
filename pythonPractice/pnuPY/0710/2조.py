

def print_choice():
    choice = input('''
    다음 중 작업하실 메뉴를 입력하세요.
    I - 고객 정보 입력
    C - 현재 고객 정보 출력
    P - 이전 고객 정보 출력
    N - 다음 고객 정보 출력
    U - 고객 정보 수정
    D - 고객 정보 삭제
    F - 고객 정보 검색
    Q - 프로그램 종료
    ''').upper()
    print(choice)
    return choice


def modify_cust():
    customer = {"name": "", "gender": "",
                "email": "", "birthyear": 0}   # 초기값 설정
    while True:
        name = input("이름을 입력하세요 : ")
        l_name = len(name)
        if l_name >= 2 and l_name <= 6:
            break
        else:
            print("2~6자 사이의 이름을 입력해주세요.")
    while True:
        gender = input("성별(M/F)을 입력하세요 : ").upper()
        if gender in ("M", "F"):
            break
    while True:
        email = input("이메일 주소를 입력하세요 : ")
        e = email.find("@")
        if e >= 0:
            break
        else:
            print("올바른 입력형식을 입력해주세요")

    while True:
        birthyear = int(input("출생년도를 입력하세요 : "))
        if birthyear >= 1900 and birthyear <= 2020:
            break
        else:
            print("1900~2020년 사이의 숫자를 입력해주세요")

    customer["name"] = name
    customer["gender"] = gender
    customer["email"] = email
    customer["birthyear"] = birthyear

    return customer


def print_cust(cust_list, current):
    print("이름 : ", cust_list[current]["name"])
    print("성별 : ", cust_list[current]["gender"])
    print("이메일 : ", cust_list[current]["email"])
    print("출생년도 : ", cust_list[current]["birthyear"])


def delete_cust(cust_list, current):
    del cust_list[current]
    if current == len(cust_list):    # 마지막 위치일 때만 current 조정
        current -= 1
    return current


def find_cust(cust_list):
    f_name = input("찾으실 고객이름을 입력해주세요 : ")
    for i in range(len(cust_list)):
        if f_name == cust_list[i]["name"]:

            return i


def main():
    cust_list = []  # 고객정보 조회
    current = -1  # 현재 위치(포인터 역할)

    while True:

        choice = print_choice()

        if choice == "I":
            print("고객 정보 입력합니다.")
            cust_list.append(modify_cust())
            current = len(cust_list)-1
            print(current)

        elif choice == "C":
            print("현재 고객 정보를 출력합니다.")

            if current >= 0:
                print_cust(cust_list, current)
            else:
                print("저장된 고객 정보가 없습니다.")

        elif choice == "P":
            print("이전 고객 정보를 출력합니다.")
            if current <= 0 or len(cust_list) == 0:
                print("현재 첫 번째 고객이므로, 이전 고객 정보가 존재하지 않습니다.")
            else:
                current -= 1
                print_cust(cust_list, current)

        elif choice == "N":
            print("다음 고객 정보를 출력합니다.")
            if current == len(cust_list)-1:
                print("현재 마지막 고객이므로, 다음 고객 정보가 존재하지 않습니다.")
            else:
                current += 1
                print_cust(cust_list, current)

        elif choice == "U":
            print("현재 고객 정보를 수정합니다.")

            cust_list[current] = modify_cust()

        elif choice == "D":
            print("현재 고객 정보를 삭제합니다.")
            current = delete_cust(cust_list, current)
            print(current)

        elif choice == "F":
            print("고객 정보 검색을 시작합니다.")
            current = find_cust(cust_list)
            if current != None:

                print_cust(cust_list, current)

            elif current == None:
                print("해당 고객이 존재하지 않습니다")
        elif choice == "Q":
            print("프로그램을 종료합니다.")
            break

        else:
            print("메뉴를 정확히 입력해 주세요.")


if __name__ == "__main__":
    main()
