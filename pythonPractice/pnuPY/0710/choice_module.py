import main_module as m
# 입력하고 출력을 나눠보면 된다.



#메뉴 선택 칸
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



if __name__ == "__main__":
    m.main()

