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
            modifications_dict[int(id)] = (name,int(user))
    return modifications_dict