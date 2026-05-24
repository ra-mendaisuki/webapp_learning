from reversi_utils import EMPTY, WHITE, BLACK
import reversi_utils as utils

# リバーシのボードの初期データを作成する関数をテスト --- (※1)
def test_generate_board():
    b = utils.generate_board() # ボードを生成
    assert b[0][0] == EMPTY # 左上の盤は空であるべき
    assert b[0][7] == EMPTY
    assert b[3][4] == BLACK # 座標(4, 3)は黒であるべき
    assert b[4][3] == BLACK
    assert b[3][3] == WHITE # 座標(3, 3)は白であるべき
    assert b[4][4] == WHITE
    assert b[7][7] == EMPTY
    assert b[7][0] == EMPTY

def test_is_on_board():
    result = utils.is_on_board(1,1)
    assert result == True
    result = utils.is_on_board(1,8)
    assert result == False
    result = utils.is_on_board(8,1)
    assert result == False
    result = utils.is_on_board(8,8)
    assert result == False
    result = utils.is_on_board(1,7)
    assert result == True
    result = utils.is_on_board(7,1)
    assert result == True

def test_toggle():
    result = utils.toggle(utils.EMPTY)
    assert result == utils.EMPTY
    result = utils.toggle(utils.WHITE)
    assert result == utils.BLACK
    result = utils.toggle(utils.BLACK)
    assert result == utils.WHITE

# リバーシをルールに沿って反転できるかテスト --- (※2)
def test_reversi_rule():
    b = utils.generate_board()
    # 石を置けるかどうかのテスト --- (※3)
    assert not utils.can_flip(b, 2, 3, WHITE)
    # 最初に黒の石が置けるか試して、置けるなら置いて反転する --- (※4)
    assert utils.can_flip(b, 2, 3, BLACK)
    assert utils.flip(b, 2, 3, BLACK) == 1
    assert utils.count_stone(b, BLACK) == 4 # 数が正しいか確認
    assert utils.count_stone(b, WHITE) == 1
    print_board(b)
    # 次に白の石が置けるか試して、置けるなら置いて反転する --- (※5)
    assert utils.can_flip(b, 2, 2, WHITE)
    assert utils.flip(b, 2, 2, WHITE) == 1
    print_board(b)
    # 次に黒
    assert utils.can_flip(b, 3, 2, BLACK)
    assert utils.flip(b, 3, 2, BLACK) == 1
    print_board(b)
    # 次の白
    assert utils.can_flip(b, 2, 4, WHITE)
    assert utils.flip(b, 2, 4, WHITE) == 2
    print_board(b)
    # 次の黒
    assert utils.can_flip(b, 1, 5, BLACK)
    assert utils.flip(b, 1, 5, BLACK) == 1
    print_board(b)

# ボードを表示する関数 --- (※6)
def print_board(board: list[list[int]]):
    ST = [".", "X", "O"]
    print("  0 1 2 3 4 5 6 7")
    for y, row in enumerate(board):
        print(f"{y} " + (" ".join([ST[i] for i in row])))

if __name__ == "__main__":
    test_reversi_rule()