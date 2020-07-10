import et_module as et
import choice_module as ch

#고객 정보 입력
def main():
    cust_list = []  # 고객정보 조회
    current = -1  # 현재 위치(포인터 역할)

    while True:

        choice = ch.print_choice()

        if choice == "I":
            print("고객 정보 입력합니다.")
            cust_list.append(et.modify_cust())
            current = len(cust_list)-1
            print(current)

        elif choice == "C":
            print("현재 고객 정보를 출력합니다.")

            if current >= 0:
                et.print_cust(cust_list, current)
            else:
                print("저장된 고객 정보가 없습니다.")

        elif choice == "P":
            print("이전 고객 정보를 출력합니다.")
            if current <= 0 or len(cust_list) == 0:
                print("현재 첫 번째 고객이므로, 이전 고객 정보가 존재하지 않습니다.")
            else:
                current -= 1
                et.print_cust(cust_list, current)

        elif choice == "N":
            print("다음 고객 정보를 출력합니다.")
            if current == len(cust_list)-1:
                print("현재 마지막 고객이므로, 다음 고객 정보가 존재하지 않습니다.")
            else:
                current += 1
                et.print_cust(cust_list, current)

        elif choice == "U":
            print("현재 고객 정보를 수정합니다.")

            cust_list[current] = et.modify_cust()

        elif choice == "D":
            print("현재 고객 정보를 삭제합니다.")
            current = et.delete_cust(cust_list, current)
            print(current)

        elif choice == "F":
            print("고객 정보 검색을 시작합니다.")
            current = et.find_cust(cust_list)
            if current != None:

                et.print_cust(cust_list, current)

            elif current == None:
                print("해당 고객이 존재하지 않습니다")
        elif choice == "Q":
            print("프로그램을 종료합니다.")
            break

        else:
            print("메뉴를 정확히 입력해 주세요.")


if __name__ == "__main__":
    main()
