#make_a_map.py
#A program to create graph data structures in Python
#NOTE: IDLE defualt indention for Python (4 spaces)

def debug(names, edges):
    '''debugs the map for user errors'''
    pass

yn = input("Make a map? (y/n)")
#pj = input("In Python3 or Java? (p/j)")

if yn.lower() == "y":
    nodes = int(input("How many nodes?"))
    names = []
    edges_list = []
    for node in range(nodes):
        names.append(input("Name of node " + str(node) + ":"))
        edges_list.append(input("Space seperated list of edges: "))

    #run debugging for missing nodes
    #debug(names, edges_list)

    m_name = input("Name of map?")
    print("\n\n\n")
    print(m_name+" = {")
    for index,name in enumerate(names):
        out = "    "+name+" : "+edges_list[index]
        if index+1!=len(names):
            out+=","
        print(out)
    print("}")
    
else:
    print("No map was made...")
        
