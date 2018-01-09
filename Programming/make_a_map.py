#make_a_map.py
#A program to create graph data structures in Python
#NOTE: IDLE defualt indention for Python (4 spaces)
def debug(names, edges):
    '''debugs the map for user errors'''

    print("Testing one directional validity...")
    
    invalid = False
    invalid_edges = []

    for edge_list in edges:
        for edge in edge_list:
            if edge not in names:
                invalid_edges.append(edge)
                invalid=True

    if invalid:
        print("One Directional Test: FAILED")
        out = "Nodes listed in edges that weren't in nodes: "
        for edge in invalid_edges:
            out+=edge+", "
        print(out)
        return False
    else:
        return True
            
    print("Testing is done, test success!")
    return True
        

yn = input("Make a map? (y/n) ")
#pj = input("In Python3 or Java? (p/j)")

if yn.lower() == "y":
    
    nodes = int(input("How many nodes? "))
    names = []
    edges_list = []
    for node in range(nodes):
        names.append(input("Name of node " + str(node) + ": "))
        edges_list.append(input("Space seperated list of edges: "))

    #run debugging for missing nodes
    debug(names, edges_list)

    m_name = input("Name of map? ")
    quotes = input("Are nodes Strings? (y/n) ")
    print("\n\nCode for this map in Python3\n")
    
    print(m_name+" = {")
    
    for index,name in enumerate(names):

        if quotes.lower() == "y":
            out = "    \""+name+"\" : \""+edges_list[index]+"\""
        else:
            out = "    "+name+" : "+edges_list[index]+""
            
        if index+1!=len(names):
            out+=","
        print(out)
    print("}")
    
else:
    print("No map was made...")
