
list = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]

def list_print():
    for i in range(0,3):
            for j in range(0,3):
                print("",list[i][j],end =" ")
            print()


def game():

    list_print()

    while True:

        print(' << player_1 >>')
        r = int(input('Enter row(0-2): '))
        c = int(input('Enter column(0-2): '))
        list[r][c] = 'X'

        list_print()

        print(' << player_2 >>')
        r = int(input('Enter row(0-2): '))
        c = int(input('Enter column(0-2): '))
        list[r][c] = 'O'
        
        list_print()

        if list[0] == ['O','O','O'] or list[1] == ['O','O','O'] or list[2] == ['O','O','O']:
            print('player_2 won!')
            break 
        elif list[0] == ['X','X','X'] or list[1] == ['X','X','X'] or list[2] == ['X','X','X']:
            print('player_1 won!')
            break 
        elif (list[0][0] == list[0][1] == list[0][2]) or (list[0][0] == list[1][1] == list[2][2]) :
            if list[0][0] == 'X':
                print('player_1 won!')
                break
            elif list[0][0] == 'O':
                print('player_2 won!')
                break 
        elif (list[0][2] == list[1][2] == list[2][2]) or (list[0][2] == list[1][1] == list[2][0]):
            if list[0][2] == 'X':
                print('player_1 won!')
                break
            elif list[0][2] == 'O':
                print('player_2 won!')
                break
        elif list[0][1] == list[1][1] == list[2][1]:
            if list[0][1] == 'X':
                print('player_1 won!')
                break
            elif list[0][1] == 'O':
                print('player_2 won!')
                break 
        else:
            check = True                        #no empty space 
            for i in range(0,3):
                for j in range(0,3):
                    if list[i][j] == '-':
                        check = False           #still have empty space
                        break
            if check:
                print('no one won :(')
                break

game()
