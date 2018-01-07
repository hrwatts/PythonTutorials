#risk.py
#Christian Watts

import sys
import risk_functions as rf

test = "Hello World!"
print(test,sys.getsizeof(test), "bytes")

board, continents, trade_vals, territories, cards = rf.gen_board()

for key in territories:
    territories[key][1]=1020

print("trade vals", trade_vals, len(trade_vals))

state = (territories, cards, 0)

st_string = rf.get_state(state)

print("State String Size:",sys.getsizeof(st_string) ,"\n", st_string)

state_2 = rf.parse_state(st_string)

st_string_2 = rf.get_state(state_2)

print("State String 2:",sys.getsizeof(st_string_2) ,"\n",st_string_2)

st_string = str(st_string)
st_string_2 = str(st_string_2)

for index,letter in enumerate(st_string):
    print(letter, st_string_2[index], st_string_2[index]==letter)
