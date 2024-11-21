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

def read_constraints(filename: str):
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
    pass

def build_tarjans_sccs(graph: dict) -> list:
    def strong_connection(v: int) -> None:
        pass
    pass

def is_satisfiable(constraints: dict[int: list[int]], user_choice: list[int]) -> bool:
    pass

def main():
    constraints = read_constraints('')
    modifications = read_mods('')
