graph = [["C1", "H1"], ["C1", "H2"], ["C1", "H3"], ["C1", "H4"]]

from collections import defaultdict, Counter


def graphCompounds(graph):

    adjacency_list = defaultdict(list)

    atom_freq = defaultdict(int)

    for a, b in graph:
        adjacency_list[a].append(b)

    for src, atoms in adjacency_list.items():
        split_a = list(src)
        for char in split_a:
            if char.isalpha():
                atom_freq[char] += 1

        for atom in atoms:
            split_b = list(atom)
            for char in split_b:
                if char.isalpha():
                    atom_freq[char] += 1
    print(atom_freq)

    molecular_formula = ""
    for key, value in atom_freq.items():
        if value == 1:
            molecular_formula += key
        else:
            molecular_formula += key + str(value)

    return molecular_formula


print(graphCompounds(graph))

# topological sorting - sorts position of atom by priority
#

glucose = [
    ["C1", "H1"],
    ["C1", "H2"],
    ["C1", "C2"],
    ["C1", "C3"],
    ["C2", "H1"],
    ["C1", "H2"],
    ["C1", "C2"],
    ["C1", "C3"],
]

priority_order = {"C": 1, "H": 2, "O": 3}

sorted_atoms = sorted(priority_order.items(), key=lambda x: x[1])
print(sorted_atoms)

# priority_order
# adjacency_list
# atom_freq
