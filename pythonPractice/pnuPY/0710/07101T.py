#성적관리

# kors = list()


# while True :
#     print("성적관리")
#     print("메인메뉴")
#     print("1.성적입력")
#     print("2.성적출력")
#     print("3.프로그램 종료")

#     menu = int(input())

#     if menu == 1:
#         print("성적입력")

#         for i in range(3):
#             while True:
#                 kor = int(input("국어 %d :" %(i+1)))

#                 if 0 > kor or 100 <kor:
#                     print("성적은 0 ~ 100 사이의 범위로 입력 가능합니다.")

#                 else:
#                     kors.insert(i,kor)
#                     break

#         print("="*50)

#     elif menu == 2:
#         print("성적출력")
#         total = 0
#         for i in range(3):
#             total = total+kors[i]
        
#         for i in range(3):
#             print("[국어 %d : %3d]" % (i+1, kors[i]), end= " ")

#         avg = total/3.0
#         print("\n총점 : %3d" % total)
#         print("평균: %6.2f" % avg)
#         print("="*50)


#     elif menu == 3:
#         print("프로그램 종료합니다.~~~~")
#         break

#     else:
#         print("메뉴를 잘못입력하셨습니다.")

# 스타트업이 망하는 이유는 행동 메뉴얼이 스크립트로 잘 짜여있지 않아서 그렇다.




# 관상어 종류별 정리 

# 관상어 정보 입력 , 검색, 조회 , 수정 ,삭제, 프로그램 종료
def print_choice():
    choice = input(""" 
    작업할 메뉴를 고르시오
    1 - 관상어 정보 입력
    2 - 관상어 검색
    3 - 관상어 정보 수정
    4 - 관상어 정보 삭제
    5 - 프로그램 종료
    """).upper()
    print(choice)
    return choice



#선택 어떻게 했더라? choice
 
def modify_fish():

    fish = {
        "name": " ", "celcius":0, "ph":0,"n":0
    }

    while True:

        name=input("이름을 입력하세요:")
    
    while True:

        celcius=input("온도를 입력하세요:")

    while True:

        ph = input("ph를 입력하세요.")

    fish["name"] = name
    fish["celcius"] = celcius
    fish["ph"] = ph
    fish["n"] = n

    return fish

def print_fish(cust_fish, current):
    print("이름 : ", cust_fish[current]["name"])
    print("celcius : ", cust_fish[current]["celcius"])
    print("ph : ", cust_fish[current]["ph"])
    print("n : ", cust_fish[current]["n"])

def delete_fish(fish_list, current):
    del fish_list[current]
    if current == len(fish_list):
        current -=1
    return current


#만약 input에 1번이 입력되었다면, 정보입력할 수 있는 칸과, 그것을 저장하여 리스트에 넣어야 함.

def main():
    fish_list = []
    current = -1

    while True:

        choice = print_choice()

        if choice == 1:
            print("물고기 정보 입력합니다.")
            fish_list.append(modify_fish())
            current = len(fish_list)-1
            print(current)

        elif choice == 2:
            print("관상어 검색합니다.")

            if current >= 0:
                print_fish(fish_list, current)
            else:
                print("물고기 정보가 없습니다.")
                
        
        elif choice == 3:
            print("물고기 정보를 수정합니다.")
            fish_list[current] = modify_fish()

        elif choice == 4:
            print("물고기 정보를 삭제합니다.")
            current = delete_fish(fish_list, current)
            print(current)

        elif choice == 5:
            print("프로그램을 종료합니다.")
            break


        else:
            print("메뉴를 정확히 입력해 주세요,")

if __name__ == "__main__":
    main()





























