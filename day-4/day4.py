"""
   Name    : day4.py
   Author  : Ian Gomez
   Date    : December 10, 2021
   Description :
   Github  : imgomez0127@github
"""
import numpy as np
import collections

def get_boards():
    with open('input.txt', 'r') as f:
        seq_num = [int(c) for c in f.readline().strip().split(',')]
        boards = []
        mat = []
        for line in f:
            if line.strip() == '':
                boards.append(mat)
                mat = []
            mat.append([int(c) for c in filter(lambda x: len(x) > 0, line.strip().split(' '))])
        boards.append(mat)
        boards = [list(filter(lambda x: len(x) > 0, board)) for board in boards[1:]]
        return seq_num, [np.array(board) for board in boards]

def bingo(seq_num, boards):
    bool_boards = [np.zeros(board.shape).astype(bool) for board in boards]
    win = [False for _ in range(len(bool_boards))]
    for num in seq_num:
        for i, board in enumerate(boards):
            bool_boards[i] = np.logical_or(bool_boards[i], board == num)
            row_win = np.any(np.sum(bool_boards[i], axis=0) == bool_boards[i].shape[0])
            col_win = np.any(np.sum(bool_boards[i], axis=1) == bool_boards[i].shape[1])
            if row_win or col_win:
                win[i] = True
        if sum(win):
            break
    return num * max([np.sum(board[np.logical_not(bool_board)])
                      for i, (board, bool_board) in enumerate(zip(boards, bool_boards)) if win[i]])

def bingo2(seq_num, boards):
    bool_boards = [np.zeros(board.shape).astype(bool) for board in boards]
    win = [False for _ in range(len(boards))]
    win_counts = collections.Counter(range(len(boards)))
    for num in seq_num:
        for i, board in enumerate(boards):
            bool_boards[i] = np.logical_or(bool_boards[i], board == num)
            row_win = np.any(np.sum(bool_boards[i], axis=0) == bool_boards[i].shape[0])
            col_win = np.any(np.sum(bool_boards[i], axis=1) == bool_boards[i].shape[1])
            if row_win or col_win:
                win[i] = True
                win_counts[i] += 1
        if sum(win) == len(win):
            break
    board_num, count = min(win_counts.items(), key=lambda x: x[1])
    return num * np.sum(boards[board_num][np.logical_not(bool_boards[board_num])])


def main():
    seq_num, boards = get_boards()
    print(bingo(seq_num, boards))
    print(bingo2(seq_num, boards))

if __name__ == '__main__':
    main()
