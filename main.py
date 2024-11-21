"""
2SAT project
"""
import argparse

def read_from_terminal() -> tuple[str, str, list[int]]:
    """
    Reads input data from the command line and returns it as a tuple.

    Parameters:
    - --m (str): 
    - --r (str): 
    - --c (str): 

    Returns:
    - tuple[str, str, list[int]]
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--m', type=str, required=True)
    parser.add_argument('--r', type=str, required=True)
    parser.add_argument('--c', type=str, required=True)
    args = parser.parse_args()
    id_users = [int(x) for x in args.c.split(',')]
    return (args.m, args.r, id_users)

def read_mods(filename:str) -> dict:
    """
Reads a file containing modification data and returns a dictionary
where the key is the modification mod_id and the value is a tuple (name, user_visibility).
Return dictionary {key(mod_id): (name,user_visibility)}
:param filename: The path to the file containing the modification data.
:return modifications_dict: A dictionary where the key is mod_id and the value\
is a tuple (name: str, user_visibility: int).
    """
    with open(filename, encoding='utf-8') as f:
        modifications_dict = {}
        f.readline()
        for i in f:
            i = i.strip().split(';')
            if len(i) != 3:
                print('Неправильно написані дані, будь ласка, відкоригуйте файл!')
                break
            mod_id, name, user_visibility = i
            modifications_dict[int(mod_id)] = (name.strip(),int(user_visibility))
    return modifications_dict

def read_constraints(filename: str) -> dict[int: list[int]]:
    constraints = {}
    with open(filename, mode='r', encoding='utf-8') as f:
        f.readline()
        for line in f:
            line = line.strip().split(';')
            mod_id = int(line[0])
            conflicts = line[1].strip().split(',')
            requirements = line[2].strip().split(',')
            constraints[mod_id] = ([-int(num) for num in conflicts \
            if conflicts != ['']] + [int(num) for num in requirements if line[2] != ''])
    return constraints

def build_graph(constraints: dict[int: list[int]], user_choice: list[int]) -> dict:
    """
    Stadnik Oleksandr
    """
    # NOT FINISHED!
    # make dicts with x[1], x[2] .. x[n] to be able to give x's bool values.
    # if x[n] is assigned value more than once, 2sat fails.
    # return табличку з деталями, які треба встановити
    graph = {}

    for mod_id, requirements in constraints.items():
        if mod_id in user_choice or mod_id in graph:
        # the second condition is to catch the required submods and assign constraints
            graph[mod_id] = requirements
            for submod_id in requirements:
                if submod_id > 0:  # Positive submod means it's required, so add to graph
                    if submod_id not in graph:
                        graph[submod_id] = []  # Create an entry for the required submod
        else:  # If mod_id is not in user_choice, handle negations (not selected)
            graph[-mod_id] = [-submod_id if submod_id > 0 else submod_id for submod_id in requirements]
            for submod_id in requirements:
                if submod_id > 0:
                    if -submod_id not in graph:
                        graph[-submod_id] = []
    return graph

def main():
    constraints = read_constraints('')
    modifications = read_mods('')
