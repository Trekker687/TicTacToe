playingboard = {'7': '  ', '8': '  ', '9': '  ',
          '4': '  ', '5': '  ', '6': '  ',
          '1': '  ', '2': '  ', '3': '  '}

boardkeys = []
for key in playingboard:
    boardkeys.append(key)

def printboard(board):
    print(board['7'] +'|' +board['8'] + '|' + board['9'])
    print('-+-+-+-+-')
    print(board['4'] +'|' +board['5'] + '|' + board['6'])
    print('-+-+-+-+-')
    print(board['1'] +'|' +board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printboard(playingboard)
        print("It's your turn," +turn+ ".Move to which position?")
        move = input()
        if playingboard[move] == '  ':
            playingboard[move] = turn
            count += 1
        else:
            print("Position is already taken. Select a different position")
            continue
        if count >= 5:
            if  playingboard['7'] == playingboard['8'] == playingboard['9'] != '  ' :
                printboard(playingboard)
                print("Game Over.")
                print("****" +turn+ " won. ****")
            elif playingboard['4'] == playingboard['5'] == playingboard['6'] != '  ' :
                printboard(playingboard)
                print("Game Over.")
                print("****" +turn+ " won. ****") 
            elif playingboard['1'] == playingboard['2'] == playingboard['3'] != '  ' :
                printboard(playingboard)
                print("Game Over.")
                print("****" +turn+ " won. ****") 
            elif playingboard['1'] == playingboard['4'] == playingboard['7'] != '  ' :
                printboard(playingboard)
                print("Game Over.")
                print("****" +turn+ " won. ****") 
            elif playingboard['2'] == playingboard['5'] == playingboard['8'] != '  ' :
                printboard(playingboard)
                print("Game Over.")
                print("****" +turn+ " won. ****")    
            elif playingboard['3'] == playingboard['6'] == playingboard['9'] != '  ' :
                printboard(playingboard)
                print("Game Over.")
                print("****" +turn+ " won. ****")  
            elif playingboard['7'] == playingboard['5'] == playingboard['3'] != '  ' :
                printboard(playingboard)
                print("Game Over.")
                print("****" +turn+ " won. ****") 
            elif playingboard['1'] == playingboard['5'] == playingboard['9'] != '  ' :
                printboard(playingboard)
                print("Game Over.")
                print("****" +turn+ " won. ****") 

        if count == 9:
            printboard(playingboard)
            print("Game Over.")
            print("**** It's a Tie ****")
        

        if turn == 'X':
            turn = 'O'
        else:
            turn == 'X'

    restart = input("Do you want to play again? y/n ")
    if restart == 'y' or restart == 'Y':
        for key in boardkeys:
            playingboard[key] = ""
        game()


    
if __name__ == '__main__':
    game()

