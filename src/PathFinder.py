from read_input import *


#total cost for nodes visited
treeDict = read_input2()[0]
def Astar(start, goal):
    heuristicDict = createHeuristicDict(goal)
    cost = {start : 0}
    """
    Input : dictionary (data structures for graph with adjacency matrix representation) 
    Output : Array of nodes with A* values , Array of ordered place sequence based on shortest path using A* pathfinder algortihm
    """
    # OPEN SET
    opened = []
    # CLOSE SET
    closed = []
    # CURRENT PLACE
    current = start
    # ADD CURRENT TO OPEN 
    opened.append([current, heuristicDict[current]])
    while True:
        # CHECK FOR MINIMUM HEURISTIC in OPEN SET
        if len(opened) == 0 :
            return [], [], []
        current = min(opened, key = lambda x : x[1])
        # CHECKED_NODE
        checked_node = current[0]
        # APPEND IT TO CLOSED SET
        closed.append(current)
        # AFTER APPENDING TO CLOSE, DELETE FROM OPENED
        opened.remove(current)
        # CHECK IF GOAL IS INCLUDED IN CLOSED SET
        if(closed[-1][0] == goal):
            break
        # IF THE PREVIOUS CONDITIONAL GUARD IS NOT FULFILLED, move to the next children's node
        for children in treeDict[checked_node].items():
            # CHECK IF CHILDREN NODES ALREADY IN CLOSED SET
            if children[0] in [closed_nodes[0] for closed_nodes in closed]:
                 continue
            # UPDATE THE CHILDREN PATH WITH RECENT VALUE, guaranteed minimum because of lambda minimum function in line 24
            cost.update({children[0] : cost[checked_node] + children[1]})
            # CAST F VALUE (HEURISTIC + CURRENT PATH COST) OF CURRENT NODES
            current_fval = cost[checked_node] + heuristicDict[children[0]] + children[1]
            # ADD TO OPENED AFTER COUNTING THE F VALUES
            # USED TEMP SO THE ACTION WON'T CORRUPT THE treeDict
            temp = [children[0], current_fval]
            opened.append(temp)
    ''' ordering the sequence based on A* values
    e.g of A* closed set = [['ITB', 65], ['DagoA', 70], ['DagoB', 70], ['DagoC', 70], ['Goal', 75]] '''
    # DEFINING THE LAST_NODE OR GOAL_NODE
    last_node = goal
    ordered_sequence = []
    ordered_sequence.append(goal)
    # TRACK FROM lastindex-1 to the first index 
    for i in range(len(closed) - 2, -1, -1):
        # DEFINE CHECKED NODE AS STRING 
        check_node = closed[i][0]
        # CHECK IF THE GOAL IS THE CHILD OF THE CHECKED NODE
        if last_node in [children[0] for children in treeDict[check_node].items()]:
            if (cost[check_node] + treeDict[check_node][last_node] == cost[last_node]):
                ordered_sequence.append(check_node)
                last_node = check_node
    # Reverse ordering from ordered_sequence
    ordered_sequence.reverse()
    return closed, ordered_sequence, cost

def createHeuristicDict(goal):
    heuristicDict2 = dict()
    for nodes in treeDict:
        heuristicDict2[nodes] = euclideanDistance(nodes, goal)
    return heuristicDict2
