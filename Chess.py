k = int(input('Введите номер вертикали (k): '))
l = int(input('Введите номер горизонтали (l): '))
m = int(input('Введите номер вертикали (m): '))
n = int(input('Введите номер горизонтали (n): '))

print('\t')  # Построение шахматной доски с нулями в качестве клеток, 1 и 2 - пешки
for i in range(1, 9):
    for j in range(1, 9):
        if k == j and l == 9 - i:
            print(1, end=' ')
        elif m == j and n == 9 - i:
            print(2, end=' ')
        else:
            print(0, end=' ')
    print('\t')


def color(k, l, m, n):
    if (k + l + m + n) % 2 == 0:
        return "Поля одного цвета"
    else:
        return "Поля разных цветов"


def queen(k, l, m, n):
    if k == m or l == n or k + l == m + n or k - m == l - n:
        return "Ферзь угрожает пешке"
    else:
        return "Ферзь не угрожает пешке"


def horse(k, l, m, n):
    if (m == k + 2 and n == l + 1) or (m == k - 2 and n == l + 1) or (m == k - 1 and n == l + 2) or (m == k + 1 \
                                                                                                     and n == l + 2) or (
            m == k - 2 and n == l - 1) or (m == k + 2 and n == l - 1) or (m == k - 1 and n == l - 2) \
            or (m == k + 1 and n == l - 2):
        return "Конь угрожает пешке"
    else:
        return "Конь не угрожает пешке"


def rook(k, l, m, n):
    if k == m or l == n:
        return "Ладья может попасть на поле одним ходом"
    else:
        a = "Ладья может попасть на поле за два хода, перейдя сначала на поле "
        b = str(m)  # Смещаем на поле по горизонтали с координатой как у второй пешки
        c = str(l)
        d = str(k)
        e = str(n)  # Смещаем на поле по вертикали с координатой как у второй пешки
        f = a + '(' + b + ',' + c + ')' + ' или ' + '(' + d + ',' + e + ')'
        return f


def queen_2(k, l, m, n):
    if k == m or l == n or k + l == m + n or k - m == l - n:
        return "Ферзь может попасть на поле одним ходом"
    else:
        a = "Ферзь может попасть на поле за два хода, перейдя сначала на поле "
        b = str(m)
        c = str(l)
        d = str(k)
        e = str(n)
        f = a + '(' + b + ',' + c + ')' + ' или ' + '(' + d + ',' + e + ')'
        return f


def bishop(k, l, m, n):
    if k + l == m + n or k - m == l - n:
        return "Слон может попасть на поле одним ходом"
    elif (k + l + m + n) % 2 != 0:  # Проверяем, стоят ли пешки на полях одного цвета
        return "Слон не угрожает пешке"
    else:  # Если пешки на полях одного цвета, то двигаем в разные стороны пока не найдем подходящий вариант
        i = 0
        while k + l != m + n and k - m != l - n:
            k -= 1
            l -= 1
            i += 1
            if k < 1 or l < 1 or k > 8 or l > 8:
                k = k + i
                l = l + i
                i = 0
                while k + l != m + n and k - m != l - n:
                    k += 1
                    l -= 1
                    i += 1
                    if k < 1 or l < 1 or k > 8 or l > 8:
                        k = k - i
                        l = l + i
                        i = 0
                        while k + l != m + n and k - m != l - n:
                            k -= 1
                            l += 1
                            i += 1
                            if k < 1 or l < 1 or k > 8 or l > 8:
                                k = k + i
                                l = l - i
                                while k + l != m + n and k - m != l - n:
                                    k += 1
                                    l += 1
    a = "Слон может попасть на поле за два хода, перейдя сначала на поле "
    b = str(k)
    c = str(l)
    f = a + '(' + b + ',' + c + ')'
    return f


print("а)", color(k, l, m, n))
print("б)", queen(k, l, m, n))
print("в)", horse(k, l, m, n))
print("г)", rook(k, l, m, n))
print("д)", queen_2(k, l, m, n))
print("е)", bishop(k, l, m, n))
