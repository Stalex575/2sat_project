import pandas as pd

def read_exel_mods(filename: str, sheet_name: str) -> dict:
    """
    Reads a specific sheet from an Excel file containing modification data 
    and returns a dictionary where the key is the modification mod_id 
    and the value is a tuple (name, user_visibility).
    
    :param filename: The path to the Excel file containing the modification data.
    :param sheet_name: The name of the sheet to read from the Excel file.
    :return: A dictionary {key(mod_id): (name: str, user_visibility: int)}.

    >>> import pandas as pd
    >>> data = {'id': [1, 2], 'mods': ['Mod A', 'Mod B'], 'user_visibility': [1, 0]}
    >>> df = pd.DataFrame(data)
    >>> df.to_excel('test_mods.xlsx', sheet_name='Modifications', index=False)
    >>> read_exel_mods('test_mods.xlsx', 'Modifications')
    {1: ('Mod A', 1), 2: ('Mod B', 0)}
    """
    data = pd.read_excel(filename, sheet_name=sheet_name)
    required_columns = {'id', 'mods', 'user_visibility'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"Сторінка '{sheet_name}' повинна містити колонки: {required_columns}")
    modifications_dict = {
        row['id']: (row['mods'], row['user_visibility'])
        for _, row in data.iterrows()
    }
    return modifications_dict




def read_constraints(filename: str, sheet_name: str) -> dict:
    """
    Reads a specific sheet from an Excel file containing constraint data 
    and returns a dictionary where the key is the constraint id 
    and the value is a tuple (type, value).
    
    :param filename: The path to the Excel file containing the constraint data.
    :param sheet_name: The name of the sheet to read from the Excel file.
    :return: A dictionary {key(id): (type: str, value: any)}.

    >>> import pandas as pd
    >>> data = {'id': [1, 2, 3], 'conflicting id': ['Max', 'Min', 'Fixed'], 'must id': [100, 10, 50]}
    >>> df = pd.DataFrame(data)
    >>> df.to_excel('test_constraints.xlsx', sheet_name='Constraints', index=False)
    >>> read_constraints('test_constraints.xlsx', 'Constraints')
    {1: ('Max', 100), 2: ('Min', 10), 3: ('Fixed', 50)}
    """
    
    data = pd.read_excel(filename, sheet_name=sheet_name)
    required_columns = {'id', 'conflicting id', 'must id'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"Сторінка '{sheet_name}' повинна містити колонки: {required_columns}")
    constraints_dict = {
        row['id']: (row['conflicting id'], row['must id'])
        for _, row in data.iterrows()
    }
    
    return constraints_dict

if __name__== '__main__':
    import doctest
    print(doctest.testmod())
