import networkx as nx


def ecc(network):
    #net = network.to_undirected()
    e =  nx.eccentricity(network).items()
    #print(e)
    r = [x[1] for x in e]
    # mean eccentricity
    m = sum(r)/len(r)
    return round(m, 3)