file = open("contact.txt", "a+", encoding="UTF8")   # 연락처 파일 열기
file.seek(0)    # 파일 커서를 맨 앞으로 이동
contact_list = []

for line in file:  # 연락처 리스트에 저장
    contact_list.append(line.split())
contact_list.sort()

file.close()    # 파일 닫기


def printList():   # 전체 연락처 출력
    print("이름\t전화번호")
    for i in range(len(contact_list)):
        print(contact_list[i][0], contact_list[i][1])
    print("\n")


def addContact(name, number):  # 연락처 추가
    contact_list.append([name, number])
    contact_list.sort()  # 리스트 재정렬 후 출력
    print("\n")
    printList()


def deleteContact(name):   # 연락처 삭제
    flag = 1    # 중복되는 이름이 있는지 검사하기 위한 변수
    while flag:  # 중복되는 이름이 하나도 없으면 실행되지 않음
        flag = 0
        for lst in contact_list:    # 리스트의 요소들을 순차적으로 검사함
            if name in lst[0]:
                remove_index = contact_list.index(lst)
                contact_list.pop(remove_index)
                flag = 1    # 중복되는 이름 발견

    print("\n")
    printList()  # 연락처 목록 출력


def modifyContact(name, number, new_name, new_number):   # 연락처 수정
    modify_index = contact_list.index([name, number])   # 수정할 연락처가 있는 인덱스를 찾음
    contact_list[modify_index] = [new_name, new_number]  # 새 이름과 번호로 수정
    contact_list.sort()  # 연락처 재정렬 후 출력
    print("\n")
    printList()


while True:
    num = int(input("""연락처 관리 프로그램]
    1 : 전체 연락처 출력
    2 : 새로운 연락처 추가
    3 : 연락처 삭제
    4 : 연락처 수정
    5 : 종료
    메뉴를 선택하세요[1-5] : """))
    print("\n")

    if num == 1:    # 전체 연락처 출력
        printList()

    elif num == 2:  # 새로운 연락처 추가
        name = input("연락처에 추가할 이름을 입력하세요: ")
        number = input("연락처에 추가할 전화번호를 입력하세요: ")
        addContact(name, number)

    elif num == 3:  # 연락처 삭제
        name = input("연락처에서 삭제할 이름을 입력하세요: ")
        deleteContact(name)

    elif num == 4:  # 연락처 수정
        name = input("연락처에서 수정하고자 하는 이름을 입력하세요: ")
        number = input("전화번호를 입력하세요: ")
        new_name = input("\n수정할 이름을 입력하세요: ")
        new_number = input("수정할 전화번호를 입력하세요: ")
        modifyContact(name, number, new_name, new_number)

    elif num == 5:  # 종료
        break

# 연락처 파일을 새로 업데이트하기 위해 w 모드로 다시 읽음
file = open("contact.txt", "w", encoding="UTF8")

for i in range(len(contact_list)):  # 순서대로 연락처를 파일에 저장함
    file.write(contact_list[i][0]+' '+contact_list[i][1]+'\n')

file.close()    # 파일 닫기
