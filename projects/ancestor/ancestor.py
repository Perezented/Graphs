
def earliest_ancestor(ancestors, starting_node, parent=None, child=None):
    if parent is None:
        parent = dict()
    if child is None:
        child = dict()
    if len(parent) == 0:
        for n in ancestors:
            # print(n[1])
            # if starting_node == n[1]:
            #     print(n)
            #     return n[0]
            if n[1] in child:
                # print(n[1])
                # print(n)
                # print(child[n[1]])
                if child[n[1]] > n[0]:
                    child[n[1]] = n[0]
                else:
                    continue
            parent[n[0]] = n[1]
            child[n[1]] = n[0]
    # print(child)
    # print(parent)
    if starting_node not in child:
        return - 1
    if starting_node in child:
        if child[starting_node] not in child:
            # print(child[starting_node])
            return child[starting_node]
        else:
            return earliest_ancestor(ancestors, child[starting_node], parent, child)
