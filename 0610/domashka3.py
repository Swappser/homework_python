def phone():
    dic_q = dict()
    name = ''
    nomer = ''
    print("Введите имя: ")
    while name != 'q' and nomer != 'q':
        name = input()
        if (name == 'q'):
            break
        print("Введите номер формата (+X-XXX-XXX-XX-XX): ")
        nomer = input()
        if nomer == 'q':
            break
        if nomer[0]=='+' and nomer[1].isdigit and nomer[2]=="-" and nomer[3:6].isdigit and nomer[6]=='-' and nomer[7:10].isdigit and nomer[10]=='-' and nomer[11:13].isdigit and nomer[13]=='-' and nomer[14:] and len(nomer)==16:
            dic_q[name] = nomer
        else:
            print('Error')
        print("Если вам необходимо пополнить список , то повторно введите Имя")
        print("Если хотите получить список контактов , введите : 'q' ")
    print(dic_q)

phone()