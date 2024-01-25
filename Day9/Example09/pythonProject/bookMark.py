'''
파이썬 도서관리 프로그램

1. 도서 등록
2. 도서 목록
3. 도서 검색
4. 도서 삭제
5. 프로그램 종료

책 정보 => 도서번호, 책 이름, 책 저자, 출판사
'''

book_mark = []; # 모든 책 정보를 저장할 리스트

while True:
    print("========== ◆ 도서 관리 프로그램 ◆ ==========");
    print("1. 도서 등록");
    print("2. 도서 목록");
    print("3. 도서 검색");
    print("4. 도서 삭제");
    print("5. 도서 프로그램 종료");

    choice = int(input("메뉴 선택 >> "));
    if choice == 1:
        book_dict = {};

        book_seq = int(input("도서 번호 >> "));
        book_name = input("책 이름 >> ");
        book_author = input("책 저자 >> ");
        book_publisher = input("출판사 >> ");

        book_dict['seq'] = book_seq;
        book_dict['name'] = book_name;
        book_dict['author'] = book_author;
        book_dict['publisher'] = book_publisher;
        book_mark.append(book_dict);

    elif choice == 2:

        # 리스트에 저장된 모든 item을 출력해야 된다
        for item in book_mark:
            print("★★★★★★★★★★")
            print("도서 번호 : {}".format(item.get('seq')));
            print("도서 이름 : {}".format(item.get('name')));
            print("도서 저자 : {}".format(item.get('author')));
            print("출판사 : {}".format(item.get('publisher')));
            print("★★★★★★★★★★")
        pass;
    elif choice == 3:
        '''
        n을 입력하면 도서 제목으로 검색
        p를 입력하면 도서 출판사로 검색
        '''
        
        search_type = input("검색할 타입을 선택해 주세요 >>");

        if search_type == 'n':
            title = input("검색 하려는 책 제목을 입력해 주세요 >> ");
            for item in book_mark:
                sec = item.get('name'); # 책 제목들을 들고온다
                if sec == title: #만약 저장된 책 제목과 입력받은 값이 같다면 출력
                    print("★★★★★★★★★★")
                    print("도서 번호 : {}".format(item.get('seq')));
                    print("도서 이름 : {}".format(item.get('name')));
                    print("도서 저자 : {}".format(item.get('author')));
                    print("출판사 : {}".format(item.get('publisher')));
                    print("★★★★★★★★★★")
        elif search_type == 'p':
            publisher = input("검색 하려는 책 출판사를 입력해 주세요 >>");
            for item in book_mark:
                sec == item.get('publisher');
                if sec == publisher:
                    print("★★★★★★★★★★")
                    print("도서 번호 : {}".format(item.get('seq')));
                    print("도서 이름 : {}".format(item.get('name')));
                    print("도서 저자 : {}".format(item.get('author')));
                    print("출판사 : {}".format(item.get('publisher')));
                    print("★★★★★★★★★★")
            
    elif choice == 4:
        book_del = int(input("삭제 할 도서 번호를 입력해 주세요 >> "));
        for i in range(len(book_mark)):
            if book_mark[i]['seq'] == book_del:
                del book_mark[i];
    elif choice == 5:
        print("프로그램 종료 !! ~~~");
        break;

