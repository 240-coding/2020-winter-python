file = open("contact.txt", "w+")
contact_list = []

for line in file:  # 연락처 리스트 초기화
    contact_list.append(line.split)
contact_list.sort()


def printList():   # 전체 연락처 출력
    print("이름\t전화번호")
    for i in range(len(contact_list)):
        print(contact_list[i][0], contact_list[i][1])


def addContact(name, number):  # 연락처 추가
    contact_list.append([name, number])
    contact_list.sort()
    print("\n")
    printList()


def deleteContact(name):   # 연락처 삭제 - 중복 이름 모두 삭제가 안 됨
    for lst in contact_list:
        if name in lst[0]:
            remove_index = contact_list.index(lst)
            contact_list.pop(remove_index)
    print("\n")
    printList()


def modifyContact(name, number, new_name, new_number):   # 연락처 수정
    modify_index = contact_list.index([name, number])
    contact_list[modify_index] = [new_name, new_number]
    contact_list.sort()
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

    if num == 1:
        printList()

    elif num == 2:
        name = input("연락처에 추가할 이름을 입력하세요: ")
        number = input("연락처에 추가할 전화번호를 입력하세요: ")
        addContact(name, number)

    elif num == 3:
        name = input("연락처에서 삭제할 이름을 입력하세요: ")
        deleteContact(name)

    elif num == 4:
        name = input("연락처에서 수정하고자 하는 이름을 입력하세요: ")
        number = input("전화번호를 입력하세요: ")
        new_name = input("\n수정할 이름을 입력하세요: ")
        new_number = input("수정할 전화번호를 입력하세요: ")
        modifyContact(name, number, new_name, new_number)

    elif num == 5:
        break

for i in range(len(contact_list)):
    file.write(contact_list[i][0]+' '+contact_list[i][1])

file.close()
