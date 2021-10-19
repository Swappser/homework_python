def Year(d, m, y):

    '''
    d - день | m - месяц | y - год | d_now - день на данный момент | m_now - месяц на данный момент | y_now - год на данный момент |
    Все переменные должны быть целочисленными
    Функция возвращает значение True или False в зависимости от существования даты
    '''

    listVisokos = [1,3,5,7,8,10,12]
    listNeVisokos = [4,6,9,11]
    d_now = 18
    m_now = 10
    y_now = 2021
    if (y > 0 and m > 0 and d > 0 and m < 13 and d < 32) and (y <= y_now):
        if (y < y_now) or (y == y_now and m < m_now) or (y == y_now and m == m_now and d <= d_now):
            if d < 31 and m in listNeVisokos:
                return True
            elif d < 32 and m in listVisokos:
                return True
            elif m == 2:
                if (d == 29 and y % 4 == 0) or d < 29:
                    return True
    return False

print(Year(18, 56 ,4224))