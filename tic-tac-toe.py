from sys import exit
import re

def game_on():
    def print_board(row1,row2,row3):
        print("\n")
        print(''.join(row1[0] + " | " + row1[1] + " | " + row1[2]))
        print(''.join(row2[0] + " | " + row2[1] + " | " + row2[2]))
        print(''.join(row3[0] + " | " + row3[1] + " | " + row3[2]))
        return

    def instructions(irow1,irow2,irow3):
        print("##################### Two Player Tic Tac Toe #####################")
        print("\n")
        print("######################### Instructions ###########################")

        print("To play the game, select a square by number:")
       
        print(''.join(irow1[0] + " | " + irow1[1] + " | " + irow1[2]))
        print(''.join(irow2[0] + " | " + irow2[1] + " | " + irow2[2]))
        print(''.join(irow3[0] + " | " + irow3[1] + " | " + irow3[2]))
        return

    def win_check(trackerlist):
        win_condition1 = ["1","2","3"]
        win_condition2 = ["4","5","6"]
        win_condition3 = ["7","8","9"]

        win_condition4 = ["1","4","7"]
        win_condition5 = ["2","5","8"]
        win_condition6 = ["3","6","9"]

        win_condition7 = ["1","5","9"]
        win_condition8 = ["3","5","7"]
        trackerlist.sort()

        if(all(x in trackerlist for x in win_condition1)):
            print_board(row1,row2,row3)
            print("Winner!!")
            exit()
        elif(all(x in trackerlist for x in win_condition2)):
            print_board(row1,row2,row3)
            print("Winner!!")
            exit()
        elif(all(x in trackerlist for x in win_condition3)):
            print_board(row1,row2,row3)
            print("Winner!!")
            exit()
        elif(all(x in trackerlist for x in win_condition4)):
            print_board(row1,row2,row3)
            print("Winner!!")            
            exit()
        elif(all(x in trackerlist for x in win_condition5)):
            print_board(row1,row2,row3)
            print("Winner!!")
            exit()
        elif(all(x in trackerlist for x in win_condition6)):
            print_board(row1,row2,row3)
            print("Winner!!")
            exit()
        elif(all(x in trackerlist for x in win_condition7)):
            print_board(row1,row2,row3)
            print("Winner!!")
            exit()
        elif(all(x in trackerlist for x in win_condition8)):
            print_board(row1,row2,row3)
            print("Winner!!")
            exit()
        return

    ####### The Board #######
    row1 = ["_","_","_"]
    row2 = ["_","_","_"]
    row3 = ["_","_","_"]

    irow1 = ["1","2","3"]
    irow2 = ["4","5","6"]
    irow3 = ["7","8","9"]
    ####### The Board #######

    turn = 1
    ex_tracker = []
    oh_tracker = []
    # test_tracker = ["1","2","3"]


    ############# WIN CONDITIONS ################
    win_condition1 = ["1","2","3"]
    win_condition2 = ["4","5","6"]
    win_condition3 = ["7","8","9"]

    win_condition4 = ["1","4","7"]
    win_condition5 = ["2","5","8"]
    win_condition6 = ["3","6","9"]

    win_condition7 = ["1","5","9"]
    win_condition8 = ["3","5","7"]
    ############# WIN CONDITIONS ################
    instructions(irow1,irow2,irow3)
    while True:
        print_board(row1,row2,row3)
        if turn == 10:
            win_check(ex_tracker)
            win_check(oh_tracker)
            print("The game has ended in a draw!")
            exit()
        else:
            while True:
                move = input("Pick a square: ")
                if move in ex_tracker:
                    print("Please choose an empty square!")
                    print_board(row1,row2,row3)
                    continue
                if move in oh_tracker:
                    print("Please choose an empty square!")
                    print_board(row1,row2,row3)
                    continue
                if not re.match("[1-9]", move):
                    print("Please choose a number: ")
                    continue
                if move == "1":
                    if turn % 2 == 0:
                        row1[0] = "O"
                        oh_tracker.append(move)
                        win_check(oh_tracker)
                        turn = turn + 1
                    else:
                        row1[0] = "X"
                        ex_tracker.append(move)
                        win_check(ex_tracker)
                        turn = turn + 1
                elif move == "2":
                    if turn % 2 == 0:
                        row1[1] = "O"
                        oh_tracker.append(move)
                        win_check(oh_tracker)
                        turn = turn + 1
                    else:
                        row1[1] = "X"
                        ex_tracker.append(move)
                        win_check(ex_tracker)
                        turn = turn + 1
                elif move == "3":
                    if turn % 2 == 0:
                        row1[2] = "O"
                        oh_tracker.append(move)
                        win_check(oh_tracker)
                        turn = turn + 1
                    else:
                        row1[2] = "X"
                        ex_tracker.append(move)
                        win_check(ex_tracker)
                        turn = turn + 1
                elif move == "4":
                    if turn % 2 == 0:
                        row2[0] = "O"
                        oh_tracker.append(move)
                        win_check(oh_tracker)
                        turn = turn + 1
                    else:    
                        row2[0] = "X"    
                        ex_tracker.append(move)
                        win_check(ex_tracker)
                        turn = turn + 1
                elif move == "5":
                    if turn % 2 == 0:
                        row2[1] = "O"
                        oh_tracker.append(move)
                        win_check(oh_tracker)
                        turn = turn + 1
                    else:
                        row2[1] = "X"
                        ex_tracker.append(move)
                        win_check(ex_tracker)
                        turn = turn + 1
                elif move == "6":
                    if turn % 2 == 0:
                        row2[2] = "O"
                        oh_tracker.append(move)
                        win_check(oh_tracker)
                        turn = turn + 1
                    else:
                        row2[2] = "X"
                        ex_tracker.append(move)    
                        win_check(ex_tracker)
                        turn = turn + 1
                elif move == "7":
                    if turn % 2 == 0:
                        row3[0] = "O"
                        oh_tracker.append(move)
                        win_check(oh_tracker)
                        turn = turn + 1
                    else:
                        row3[0] = "X"
                        ex_tracker.append(move)
                        win_check(ex_tracker)
                        turn = turn + 1    
                elif move == "8":
                    if turn % 2 == 0:
                        row3[1] = "O"
                        oh_tracker.append(move)
                        win_check(oh_tracker)
                        turn = turn + 1
                    else:
                        row3[1] = "X"
                        ex_tracker.append(move)
                        win_check(ex_tracker)
                        turn = turn + 1
                elif move == "9":
                    if turn % 2 == 0:
                        row3[2] = "O"
                        oh_tracker.append(move)
                        win_check(oh_tracker)
                        turn = turn + 1
                    else:
                        row3[2] = "X"
                        ex_tracker.append(move)
                        win_check(ex_tracker)
                        turn = turn + 1
                else:
                    print("Choose a square (1 - 9): ")
                    continue
                break
    return
game_on()
