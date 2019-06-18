try:
    from graphics import *
except ImportError as a:
    import os
    os.system('C:\Python27\Scripts\pip install --user http://bit.ly/csc161graphics')
    from graphics import *

import random
import time

"""
TO DO List
" "
$.$
---
"""


def instruction_page():
    ins_win = GraphWin('instruction page', 500, 500)
    title = Text(Point(250, 30), 'instruction page')
    title.setSize(25)
    title.setFill(color_rgb(255, 51, 51))
    l1 = Line(Point(130, 45), Point(370, 45))
    l1.setFill(color_rgb(255, 51, 51))
    l1.draw(ins_win)
    title.draw(ins_win)
    t1 = Text(Point(250, 80), '1. Turn over any two cards.')
    t1.draw(ins_win)

    t2 = Text(Point(250, 130), '2. If the two cards match, keep them.')
    t2.draw(ins_win)

    t3 = Text(Point(250, 180), '3. If they do not match, turn them back over.')
    t3.draw(ins_win)

    t4 = Text(Point(250, 230), '4. Remember what was on each card and where it was.')
    t4.draw(ins_win)

    t5 = Text(Point(250, 280), '5. Watch and remember during the other player turn.')
    t5.draw(ins_win)

    t6 = Text(Point(250, 330), '6. The game is over when all the cards have been matched.')
    t6.draw(ins_win)

    t7 = Text(Point(250, 380), '7. The player with the most matches wins.')
    t7.draw(ins_win)

    t = Text(Point(250, 450), 'click to move on')
    t.setFill(color_rgb(51, 51, 255))
    t.draw(ins_win)

    ins_win.getMouse()
    ins_win.close()


def create_secret_board(win, board, text):
    """
    game window + circles board (empty) + text board (empty)
    create the circles and texts boards (+ draw)
    """
    if len(board) == 8:
        # if board is 8*8 the distance between circles in shorter
        for i in range(len(board)):
            # first create the circles board
            y = 100
            for j in board:
                j.append(Circle(Point((i + 1) * 80, y), 20))
                j[i].setFill("black")
                j[i].draw(win)
                y += 70

        # create text board on each circle
        for i in range(len(board)):
            y = 100
            for j in text:
                j.append(Text(Point((i + 1) * 80, y), 0))
                j[i].draw(win)
                y += 70
    else:
        # first create the circles board
        for i in range(len(board)):
            y = 100
            for j in board:
                j.append(Circle(Point((i + 1) * 100, y), 20))
                j[i].setFill("black")
                j[i].draw(win)
                y += 100
        # create text board on each circle
        for i in range(len(board)):
            y = 100
            for j in text:
                j.append(Text(Point((i + 1) * 100, y), 0))
                j[i].draw(win)
                y += 100


def random_board(board):
    # empty board , fill the board (the answer board)
    for num in range(1, (len(board) * len(board)) / 2 + 1):
        # run on numbers that suppose to be in board and find a place for them.
        i = random.randint(0, len(board) - 1)
        j = random.randint(0, len(board) - 1)
        while board[i][j] != 0:
            # search other place in board if this place has already fill.
            i = random.randint(0, len(board) - 1)
            j = random.randint(0, len(board) - 1)
        board[i][j] = num
    for num in range(1, (len(board) * len(board)) / 2 + 1):
        # run on numbers that suppose to be in board and find a place for them. (for second time - Pairs)
        i = random.randint(0, len(board) - 1)
        j = random.randint(0, len(board) - 1)
        while board[i][j] != 0:
            # search other place in board if this place has already fill.
            i = random.randint(0, len(board) - 1)
            j = random.randint(0, len(board) - 1)
        board[i][j] = num


def board_print(board):
    # list of lists , print every list alone
    for i in board:
        print i
    print


def point_in_circle(p, c):
    """
    point and circle, true if point in circle else false.
    if x value of point is between x values of the circle and so y value, return true if not return false.
    """
    return c.getP1().getX() < p.getX() < c.getP2().getX() and c.getP1().getY() < p.getY() < c.getP2().getY()


def turn(board, s_board, win, text, ans, remember):
    """
    get game board + circles board + window game + text board + answer box + computer's remember board,
    make the player turn by taking his mouse clicks check them and if the player select pair return true else return false.
    """

    # default values
    re_i = -1
    re_j = -1
    re_i1 = -1
    re_j1 = -1

    click = win.getMouse()
    # get point from mouse click and check if that point is in one of the circles and which one is that.
    for i in range(len(board)):
        for j in range(len(board)):
            if point_in_circle(click, s_board[i][j]) and board[i][j] != -1:
                # if click point is in this circle and this place is not exposed, make the selected circle to red and show his number.
                s_board[i][j].setFill('red')
                text[i][j].setText(board[i][j])
                re_i = i
                re_j = j

    while re_i == -1 or re_j == -1 or board[re_i][re_j] == -1:
        # if the mouse click point was not on any circle do it (the last comment) again. (wrong input)
        ans.setText('please click in a empty circle')
        click = win.getMouse()
        for i in range(len(board)):
            for j in range(len(board)):
                if point_in_circle(click, s_board[i][j]) and board[i][j] != -1:
                    s_board[i][j].setFill('red')
                    text[i][j].setText(board[i][j])
                    re_i = i
                    re_j = j

    click = win.getMouse()
    # get point from mouse click and check if that point is in one of the circles and which one is that.
    for i1 in range(len(board)):
        for j1 in range(len(board)):
            if point_in_circle(click, s_board[i1][j1]) and board[i1][j1] != -1:
                # if click point is in this circle and this place is not exposed, make the selected circle to red and show his number.
                s_board[i1][j1].setFill('red')
                text[i1][j1].setText(board[i1][j1])
                re_i1 = i1
                re_j1 = j1

    while re_i1 == -1 or re_j1 == -1 or (re_j == re_j1 and re_i == re_i1) or board[re_i1][re_j1] == -1:
        # if the mouse click point was not on any circle do it (the last comment) again. + if it the same circle (wrong input)
        ans.setText('please click in a empty circle')
        click = win.getMouse()
        for i1 in range(len(board)):
            for j1 in range(len(board)):
                if point_in_circle(click, s_board[i1][j1]) and board[i1][j1] != -1:
                    s_board[i1][j1].setFill('red')
                    text[i1][j1].setText(board[i1][j1])
                    re_i1 = i1
                    re_j1 = j1

    if board[re_i][re_j] == board[re_i1][re_j1]:
        # if the numbers of both circles are the same (correct pair), change those places it other boards (game board and remember board)
        board[re_i][re_j] = -1
        board[re_i1][re_j1] = -1
        remember[re_i][re_j] = -1
        remember[re_i1][re_j1] = -1
        ans.setText('nice move!')
        return True
    else:
        # if numbers are different, computer's remember board remember numbers in those places + return circles black again and also the text. + answer
        remember[re_i][re_j] = board[re_i][re_j]
        remember[re_i1][re_j1] = board[re_i1][re_j1]
        time.sleep(1)
        ans.setText('try again :( ')
        s_board[re_i][re_j].setFill('black')
        s_board[re_i1][re_j1].setFill('black')
        text[re_i][re_j].setText(0)
        text[re_i1][re_j1].setText(0)
    return False


def find_2(board):
    # board, num that shows twice else -1
    for i in range(len(board)):
        for j in range(len(board[i])):
            num = board[i][j]
            if num != -1 and num != 0:
                # if num is not find his pair yet but already expose
                for t in range(len(board)):
                    for f in range(len(board[i])):
                        if not (not (i != t and j == f and num == board[t][f]) and
                                not (i == t and j != f and num == board[t][f]) and
                                not (i != t and j != f and num == board[t][f])):
                                # if one of boolean (all the possible options) is true it return num else if all false not entered
                            return num
    return -1


def find_indexes(board, num):
    # board and num that show twice in board, return indexes from two shows

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == num:
                # first place (tuple number 1)
                p1 = (i, j)
                for t in range(len(board)):
                    for f in range(len(board[i])):
                        if not (not (i != t and j == f and num == board[t][f]) and
                                not (i == t and j != f and num == board[t][f]) and
                                not (i != t and j != f and num == board[t][f])):
                                # # if one of boolean (all the possible options) is true it return num else if all false not entered

                            # second place (tuple number 2)
                            p2 = (t, f)
                            return p1, p2


def find_partner(board, num):
    # board and num, True if num in board else False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == num:
                return True
    return False


def find_one_index(board, num):
    # board and num in board, index of num in board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == num:
                return i, j


def comp_turn(board, s_board, text, ans, remember):
    """
    get game board + circles board + text board + answer box + computer's remember board,
    if there is already known pair in computer's remember board select them else make random select of unknown place and check
    if pair of num in that place is already in computer's remember board if he is select him that mean select a pair else
    guss one more time random place select of unknown place and check if in some luck the computer select pair.
    if at the end the computer select pair return true else return false
    """

    num = find_2(remember)
    # check if computer's remember board have 2 expose numbers if that true num equals this number else num equals -1

    if num != -1:
        # find pair in computer's remember board

        indexes = find_indexes(remember, num)
        # indexes is a tuple of 2 others tuple that remember the places in board of the pair num

        # first place of num
        i1 = indexes[0][0]
        j1 = indexes[0][1]

        # show the move in window by terning the circle color at this place to yellow and expose his text
        s_board[i1][j1].setFill('yellow')
        text[i1][j1].setText(board[i1][j1])
        time.sleep(1.6)

        # second place of num
        i2 = indexes[1][0]
        j2 = indexes[1][1]

        # show the move in window by terning the circle color at this place to yellow and expose his text + answer
        s_board[i2][j2].setFill('yellow')
        text[i2][j2].setText(board[i2][j2])
        ans.setText('There are no smarter than the computer')
        time.sleep(1.6)

        # change the value of this places to -1 ( that mean expose place) at game board and computer's remember board
        board[i1][j1] = -1
        board[i2][j2] = -1
        remember[i1][j1] = -1
        remember[i2][j2] = -1

        return True
    else:
        # if there is no pair in computer's remember board

        # select random place in board that is not know already to the computer's remember board
        i1 = random.randint(0, len(board) - 1)
        j1 = random.randint(0, len(board) - 1)
        while remember[i1][j1] != 0:
            # the check if num in that place is already know
            i1 = random.randint(0, len(board) - 1)
            j1 = random.randint(0, len(board) - 1)

        # show that move (the circle that select by the random) in window by turning circle color to yellow and expose is text
        s_board[i1][j1].setFill('yellow')
        text[i1][j1].setText(board[i1][j1])
        time.sleep(1.6)

        if find_partner(remember, board[i1][j1]):
            # if the other place of the select number is in computer's remember board

            index = find_one_index(remember, board[i1][j1])
            # index is a tuple that remember the place of the other show of num

            # place other show of num
            i2 = index[0]
            j2 = index[1]

            # show that move (the pair of num) in window by turning circle color to yellow and expose is text + answer
            s_board[i2][j2].setFill('yellow')
            text[i2][j2].setText(board[i2][j2])
            ans.setText('There are no smarter than the computer')
            time.sleep(1.6)

            # change the value of this places to -1 ( that mean expose place) at game board and computer's remember board
            board[i1][j1] = -1
            board[i2][j2] = -1
            remember[i1][j1] = -1
            remember[i2][j2] = -1

            return True
        else:
            # if other show of num is not in computer's remember board

            # select random place in board that is not know already to the computer's remember board and not same place like the first random select
            i2 = random.randint(0, len(board) - 1)
            j2 = random.randint(0, len(board) - 1)
            while i2 == i1 and j2 == j1 or remember[i2][j2] != 0:
                # the check if num in that place is already know and not same select luke first one
                i2 = random.randint(0, len(board) - 1)
                j2 = random.randint(0, len(board) - 1)

            # show that move (the second select) in window by turning circle color to yellow and expose is text
            s_board[i2][j2].setFill('yellow')
            text[i2][j2].setText(board[i2][j2])
            time.sleep(1.6)

            if board[i1][j1] == board[i2][j2]:
                # if by luck the computer guss pair,
                # change the value of this places to -1 ( that mean expose place) at game board and computer's remember board + answer
                board[i1][j1] = -1
                board[i2][j2] = -1
                remember[i1][j1] = -1
                remember[i2][j2] = -1
                ans.setText('crazy luck !!')
                return True
            else:
                # if the computer select different numbers, computer's remember board remember numbers in those places + return circles color to black again and also the text.
                remember[i1][j1] = board[i1][j1]
                remember[i2][j2] = board[i2][j2]
                s_board[i1][j1].setFill('black')
                s_board[i2][j2].setFill('black')
                ans.setText('i am gone do it next time')
                text[i1][j1].setText(0)
                text[i2][j2].setText(0)
                return False


def game_over(board):
    # list of lists, return True if all values in lists is -1 else return False
    for i in board:
        for j in i:
            if j != -1:
                return False
    return True


def size():
    # none, return selected size board

    # new window
    size_win = GraphWin("check", 300, 300)

    title = Text(Point(150, 20), 'Select Board size')
    title.setSize(18)
    title.setFill(color_rgb(204, 0, 0))
    title.draw(size_win)

    ans = Text(Point(150, 100), '')
    ans.draw(size_win)

    # 3 circles and texts -> 3 size options
    c1 = Circle(Point(100, 150), 20)
    c2 = Circle(Point(200, 150), 20)
    c3 = Circle(Point(150, 200), 20)
    c1.draw(size_win)
    c2.draw(size_win)
    c3.draw(size_win)
    t1 = Text(c1.getCenter(), '4*4')
    t2 = Text(c2.getCenter(), '6*6')
    t3 = Text(c3.getCenter(), '8*8')
    t1.draw(size_win)
    t2.draw(size_win)
    t3.draw(size_win)

    click = size_win.getMouse()
    # get mouse click point and then check if this point is in one of the circles
    if point_in_circle(click, c1):
        size_win.close()
        return 4
    if point_in_circle(click, c2):
        size_win.close()
        return 6
    if point_in_circle(click, c3):
        size_win.close()
        return 8

    while not point_in_circle(click, c1) and not point_in_circle(click, c2) and not point_in_circle(click, c3):
        # if the click is not in any of the circle do it again (wrong input)
        ans.setText('please select one of the circles')
        click = size_win.getMouse()
        if point_in_circle(click, c1):
            size_win.close()
            return 4
        if point_in_circle(click, c2):
            size_win.close()
            return 6
        if point_in_circle(click, c3):
            size_win.close()
            return 8


def make_title(win, x_board):
    # window and x_win, create the main title of the game and draw it to the window
    title = Text(Point(x_board / 2, 10), 'memory game')
    line_title = Line(Point(x_board / 2 - 50, 16), Point(x_board / 2 + 50, 16))
    title.setFill(color_rgb(209, 0, 0))
    line_title.setFill(color_rgb(209, 0, 0))
    title.draw(win)
    line_title.draw(win)


def end_win(run_time, my_record, computer_record):
    # running play time + player record + computer record, new window that show who win and how long have played the game

    # new window
    the_end = GraphWin('game over', 500, 500)

    # end text depend who win
    end_text = Text(Point(250, 200), 'game over')
    if my_record > computer_record:
        end_text.setText('game over - you are the winner')
    elif computer_record > my_record:
        end_text.setText('game over - you lost')
    else:
        end_text.setText('game over - it is a draw')
    end_text.setSize(15)
    end_text.setFill(color_rgb(0, 128, 255))

    # Time played the game text
    run_time_text = Text(Point(250, 250),
                         'play time is: ' + str(run_time / 60) + ' minutes ' + str(run_time % 60) + ' seconds')
    run_time_text.setSize(15)
    run_time_text.setFill(color_rgb(0, 128, 255))

    # text about close end window
    close = Text(Point(250, 450), 'another click to close')
    close.setSize(15)
    close.setFill(color_rgb(96, 96, 96))

    close.draw(the_end)
    end_text.draw(the_end)
    run_time_text.draw(the_end)

    # wait to mouse click to close the window (no matter where to click)
    the_end.getMouse()
    the_end.close()


def starter():
    # none, who is start the game (1 = the player | 2 = the computer |  random between 1 and 2)

    # new window
    wd = GraphWin("check", 300, 300)

    title = Text(Point(150, 20), 'select a starting player')
    title.setSize(18)
    title.setFill(color_rgb(204, 0, 0))
    title.draw(wd)

    ans = Text(Point(150, 100), '')
    ans.draw(wd)

    # 3 circles and texts -> 3 starter options
    c1 = Circle(Point(100, 150), 30)
    c2 = Circle(Point(200, 150), 30)
    c3 = Circle(Point(150, 200), 30)
    c1.draw(wd)
    c2.draw(wd)
    c3.draw(wd)
    t1 = Text(c1.getCenter(), 'me')
    t2 = Text(c2.getCenter(), 'comp')
    t3 = Text(c3.getCenter(), 'random')
    t1.draw(wd)
    t2.draw(wd)
    t3.draw(wd)

    click = wd.getMouse()
    # get mouse click point and then check if this point is in one of the circles
    if point_in_circle(click, c1):
        wd.close()
        return 1
    if point_in_circle(click, c2):
        wd.close()
        return 2
    if point_in_circle(click, c3):
        wd.close()
        return random.randint(1, 2)

    while not point_in_circle(click, c1) and not point_in_circle(click, c2) and not point_in_circle(click, c3):
        # if the click is not in any of the circle do it again (wrong input)
        ans.setText('please select one of the circles')
        click = wd.getMouse()
        if point_in_circle(click, c1):
            wd.close()
            return 1
        if point_in_circle(click, c2):
            wd.close()
            return 2
        if point_in_circle(click, c3):
            wd.close()
            return random.randint(1, 2)


def play():
    # none, the main (all game)

    instruction_page()

    first = starter()

    size_board = size()

    # create game window and basic pattern of the board that use in the game (by the size that (according to the selected size)
    if size_board == 4:
        win = GraphWin('Memory Game!', 510, 500)
        x_board = 510
        y_board = 500

        secret_board = [[], [], [], []]
        game_board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        text = [[], [], [], []]
        re_board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    elif size_board == 6:
        win = GraphWin('Memory Game!', 710, 660)
        x_board = 710
        y_board = 660

        secret_board = [[], [], [], [], [], []]
        game_board = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        text = [[], [], [], [], [], []]
        re_board = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]]
    else:
        # size 8*8
        win = GraphWin('Memory Game!', 710, 660)
        x_board = 710
        y_board = 660

        secret_board = [[], [], [], [], [], [], [], []]
        game_board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]
        text = [[], [], [], [], [], [], [], []]
        re_board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]

    # create the record (player and computer) and show them on the window
    my_record = 0
    computer_record = 0
    my_record_text = Text(Point(80, 22), 'my record: ' + str(my_record))
    computer_record_text = Text(Point(80, 40), 'computer record: ' + str(computer_record))
    my_record_text.draw(win)
    computer_record_text.draw(win)

    make_title(win, x_board)

    # answers and information to the player
    ans = Text(Point(x_board / 2, y_board - 20), '')
    ans.draw(win)

    # show the turn status
    turn_status = Text(Point(x_board - 110, 20), 'turn status: ')
    turn_status.draw(win)
    r_player = Rectangle(Point(x_board - 210, 30), Point(x_board - 110, 50))
    r_comp = Rectangle(Point(x_board - 110, 30), Point(x_board - 10, 50))
    r_player.draw(win)
    r_comp.draw(win)
    player_turn = Text(r_player.getCenter(), 'your turn')
    computer_turn = Text(r_comp.getCenter(), 'computer turn')
    computer_turn.draw(win)
    player_turn.draw(win)

    create_secret_board(win, secret_board, text)
    random_board(game_board)
    # board_print(game_board)

    start = time.time()
    # start = save the start time for the playtime calculation

    if first == 1:
        # the player begins
        while not game_over(game_board):
            # while not all pairs have been exposed

            # change the color about who is turn and who is began
            r_player.setFill(color_rgb(102, 255, 102))
            r_comp.setFill(color_rgb(255, 51, 51))

            while not game_over(game_board) and turn(game_board, secret_board, win, text, ans, re_board):
                # while not all pairs have been exposed and player was right (find pair) last turn
                my_record += 1
                my_record_text.setText('my record: ' + str(my_record))

            # change the color about who is turn and who is began
            r_player.setFill(color_rgb(255, 51, 51))
            r_comp.setFill(color_rgb(102, 255, 102))

            while not game_over(game_board) and comp_turn(game_board, secret_board, text, ans, re_board):
                # while not all pairs have been exposed and computer was right (find pair) last turn
                computer_record += 1
                computer_record_text.setText('computer record: ' + str(computer_record))

    elif first == 2:
        # the computer begins
        time.sleep(0.4)

        while not game_over(game_board):
            # while not all pairs have been exposed

            # change the color about who is turn and who is began
            r_player.setFill(color_rgb(255, 51, 51))
            r_comp.setFill(color_rgb(102, 255, 102))

            while not game_over(game_board) and comp_turn(game_board, secret_board, text, ans, re_board):
                # while not all pairs have been exposed and computer was right (find pair) last turn
                computer_record += 1
                computer_record_text.setText('computer record: ' + str(computer_record))

            # change the color about who is turn and who is began
            r_player.setFill(color_rgb(102, 255, 102))
            r_comp.setFill(color_rgb(255, 51, 51))

            while not game_over(game_board) and turn(game_board, secret_board, win, text, ans, re_board):
                # while not all pairs have been exposed and player was right (find pair) last turn
                my_record += 1
                my_record_text.setText('my record: ' + str(my_record))

    end = time.time()
    # end = save the end time for the playtime calculation
    win.close()

    run_time = int(end - start)
    # playtime calculation

    end_win(run_time, my_record, computer_record)


play()
