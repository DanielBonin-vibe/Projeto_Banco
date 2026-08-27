def senha():
    password = 'B@nin180506'
    count = 0

    while True:
        tentativa = input('Informe a senha do sistema: ')

        if tentativa == password:
            print('Acesso autorizado!')
            return True
            
        else:
            count += 1
            print('Senha incorreta!')

            if count == 3:
                print('Limite atingido')
                return False

