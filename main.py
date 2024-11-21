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

def read_mode(filename:str) -> dict:
    """
Reads a file containing modification data and returns a dictionary
where the key is the modification id and the value is a tuple (name, user).
Return dictionary {key(id): (name,user)}
:param filename: The path to the file containing the modification data.
:param modifications_dict: A dictionary where the key is id and the value\
is a tuple (name: str, user: int).
    """
    with open(filename, encoding='utf-8') as f:
        modifications_dict = {}
        f.readline()
        for i in f:
            i = i.strip().split(';')
            if len(i) != 3:
                print('Неправильно написані дані,будь ласка, відкоригуйте файл!')
                break
            id, name, user = i
            modifications_dict[int(id)] = (name.strip(),int(user))
    return modifications_dict