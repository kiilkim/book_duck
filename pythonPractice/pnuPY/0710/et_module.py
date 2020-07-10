#고객정보 변경 외 

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