contact_list = []

def contact() :
    print('''메뉴\t설명
1\t전체 목록 출력
2\t연락처 추가
3\t연락처 삭제''')

    menu = int(input('연락처 관리 프로그램 메뉴를 선택하세요 : '))

    if menu == 1 :
        for i in range(len(contact_list)) :
            print('이름', contact_list[i][0], '연락처', contact_list[i][1])

    elif menu == 2 :
        name = input('추가할 이름을 입력하세요 : ')
        call = input('추가할 전화번호를 입력하세요 : ')
        contact_list.append([name, call])

    elif menu == 3 :
        name = input('삭제할 이름을 입력하세요 : ')
        call = input('삭제할 전화번호를 입력하세요 : ')
        contact_list.remove([name, call])

    else :
        print('잘못 입력하셨습니다.')

while True :
    contact()
