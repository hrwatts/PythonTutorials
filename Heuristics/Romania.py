#A* Search Romania
city_names=[
    "Zerind",
    "Oradea",
    "Arad",
    "Timisoara",
    "Sibiu",
    "Lugoj",
    "Mehadia",
    "Drobeta",
    "Rimnicu Vilcea",
    "Fagaras",
    "Craiova",
    "Pitesti",
    "Bucharest",
    "Giurgiu",
    "Neamt",
    "Iasi",
    "Vaslui",
    "Urziceni",
    "Hirsova",
    "Eforie"
    ]
chars = [chr(num) for num in range(97,123)]
pos = chars[:20]
pbl = dict(zip(pos, city_names)) #position by letter
pbn = dict(zip(city_names, pos)) #position by name

#p = {char:(actions, action_costs, heuristic)}
p = {
    "a":(["b", "c"],[71,75], 374),
    "b":(["a", "e"],[71, 151], 380),
    "c":(["a", "e", "d"],[75, 140, 118], 366),
    "d":(["c", "f"],[118,111], 329),
    "e":(["b", "c", "i", "j"],[151,140,80,99], 253),
    "f":(["g", "d"],[70,111], 244),
    "g":(["h", "f"],[75,70], 241),
    "h":(["k", "g"],[120,75], 242),
    "i":(["e", "l", "k"],[80,97,146], 193),
    "j":(["e", "m"],[99,211], 176),
    "k":(["h", "i", "l"],[120,146,138], 160),
    "l":(["m", "k", "i"],[101,138,97], 100),
    "m":(["r", "j", "l", "n"],[85,211,101,90], 0),
    "n":(["m"],[90], 77),
    "o":(["p"],[87], 234),
    "p":(["o", "q"],[87,92], 226),
    "q":(["r", "p"],[142,92], 199),
    "r":(["q", "m", "s"],[142,85,98], 80),
    "s":(["r", "t"],[98,86], 151),
    "t":(["s"],[86], 161)
    }

#A* search expands the path with the lowest f() value
#f(path)=g(path)+h(path)
#g(path)=action cost
#h(path)=heuristic value

initial_state = pbn[input("To: Bucharest, From: ")]


goal = pbn["Bucharest"]

#current state
s = initial_state

#running solution
solution = []
vals = []

while s!=goal:
    solution.append(pbl[s])
    #get possible actions for state s
    actions = p[s][0]
    #get cost for each action
    action_costs = p[s][1]
    #remove repeats
    for act in actions:
        if pbl[act] in solution:
            action_costs.remove(action_costs[actions.index(act)])
            actions.remove(act)
    #values for f(path)
    fs=[]
    #record the values and record them just like solution
    vals_tuples = []
    for index,act in enumerate(actions):
        heuristic = p[act][2]
        #f=g(path)+h(path)
        f = action_costs[index] + heuristic
        fs.append(f)
        vals_tuples.append((f, action_costs[index], heuristic))
    #take the one with the lowest f value
    s = actions[fs.index(min(fs))]
    vals.append(vals_tuples[fs.index(min(fs))])
    

print("Your solution is: ")
for index, val in enumerate(vals):
    print(solution[index] + " " + str(val))
print(pbl[goal])
