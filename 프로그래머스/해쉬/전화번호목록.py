def solution(phone_book):
    phone_book.sort(key=len)
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[i]) == len(phone_book[j]):
                continue
            elif phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return True
