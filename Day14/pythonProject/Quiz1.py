'''
책 제목과 책 저자의 정보를 담고있는 book 클래스를 생성하세요
1. 책 제목과 책 저자 정보를 출력하는 print_info() 메소드를 구현
2. 다음과 같은 방법으로 book1, book2 인스턴스를 생성
'''

class Book():
    def book_info(self, title, author):
        self.title = title;
        self.author = author;

    def print_info(self):
        print("책 제목 : {}".format(self.title));
        print("책 저자 : {}".format(self.author));

book1 = Book();
book2 = Book();

print("<Book1>");
book1.book_info("파이썬 배우기", "KoreaIT");
book1.print_info();


print("<Book2>");
book2.book_info("처음부터 배우는 시스템", "KIM");
book2.print_info();