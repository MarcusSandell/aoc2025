
with open("day08/input.txt") as f:
    lines = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]

class Node:
    def __init__(self, data):
        self.data = data
        self.x = data[0]
        self.y = data[1]
        self.z = data[2]
        self.connections = []
    
    def __str__(self):
        return f"{self.x},{self.y},{self.z}"

    def __repr__(self):
        return self.__str__()

    def connect(self, node: "Node"):
        self.connections.append(node)
        node.connections.append(self)

    def get_tree(self, seen=None):
        if seen is None:
            seen = set()

        tree = [self]
        seen.add(self)

        for n in self.connections:
            if n not in seen:
                tree.extend(n.get_tree(seen))

        return tree

nodes = [Node(data=line) for line in lines]

def get_closest_nodes(nodes: list[Node]):
    d = {}
    for i, n1 in enumerate(nodes):
        for n2 in nodes[i + 1:]:

            dist = (n2.x - n1.x)**2 + (n2.y - n1.y)**2 + (n2.z - n1.z)**2
            d[dist] = (n1,n2)

    return d

def get_trees(nodes: list[Node], tree = None, seen = None):
    trees = []
    seen = set()
    for node in nodes:
        if node in seen:
            continue
        tree = node.get_tree(seen=seen)
        trees.append(tree)
    return trees

def part1():
    d = get_closest_nodes(nodes)
    distances = sorted(d.keys())
    for dist in distances[:1000]:
        n1, n2 = d[dist]
        n1.connect(n2)

    trees = get_trees(nodes)
    trees.sort(key=lambda x: len(x))

    return(len(trees[-1]) * len(trees[-2]) * len(trees[-3]))

def part2():

    d = get_closest_nodes(nodes)
    distances = sorted(d.keys())
    nbr_trees = 2
    for dist in distances:
        n1, n2 = d[dist]
        n1.connect(n2)

        nbr_trees = len(get_trees(nodes))
        if nbr_trees == 1:
            return n1.x * n2.x
        #print(f"{nbr_trees}")

print(part1())
print(part2())
