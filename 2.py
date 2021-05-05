def question2(num):
    return num - num // 3 - num // 5 + 2*(num // 15)

if __name__ == '__main__':
    assert question2(15) == 9, '2 wrong'