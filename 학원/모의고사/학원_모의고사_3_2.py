def solution(phone_book):

    result = True

    for i in range(1,len(sorted(phone_book, key=lambda x: len(x)))):

        phone_book = sorted(phone_book, key=lambda x: len(x))

        for p in phone_book[i:]:

            if phone_book[i-1:i][0] in p:

                result = False

            else:

                continue

    return result

phone_book = ["12","123","1235","567","88"]

phone_book_2 = ['123','456','789']

phone_book_3 = ['119','97674223','1195524421']

print(solution(phone_book))
