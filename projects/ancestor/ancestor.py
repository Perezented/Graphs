
def earliest_ancestor(ancestors, starting_node, parent=None, child=None):
    # initial setup
    if parent is None:
        parent = dict()
    if child is None:
        child = dict()
    # set up of dictionary
    if len(parent) == 0:
        for n in ancestors:
            # if n[1] is already an item in the child dictionary
            if n[1] in child:
                # look for smallest number value
                if child[n[1]] > n[0]:
                    child[n[1]] = n[0]
                else:
                    continue
            # adding items to parent and child
            parent[n[0]] = n[1]
            child[n[1]] = n[0]

    # has no parents, return -1
    if starting_node not in child:
        return - 1
    # if starting node has parent(s)
    if starting_node in child:
        # if the specified starting node does not have a parent
        if child[starting_node] not in child:
            return child[starting_node]
        # if the item does have a parent, run it thru again
        else:
            return earliest_ancestor(ancestors, child[starting_node], parent, child)


-
