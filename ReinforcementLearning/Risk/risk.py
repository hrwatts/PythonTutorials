#risk.py
#Christian Watts

import risk_functions as rf

board, continents, territories, cards, node2name, name2node = rf.gen_board()

init_state = (territories, cards, 0)

st = rf.get_state(init_state)
import sys
sz = sys.getsizeof(st)
print(sz)
