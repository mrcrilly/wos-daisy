def sql_new_talent_dbc(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            id = data['id'],
            tabid = data['tabid'],
            tierid = data['tierid'],
            columnindex = data['columnindex'],
            spellrank_1 = data['spellrank_1'],
            spellrank_2 = data['spellrank_2'],
            spellrank_3 = data['spellrank_3'],
            spellrank_4 = data['spellrank_4'],
            spellrank_5 = data['spellrank_5'],
            spellrank_6 = data['spellrank_6'],
            spellrank_7 = data['spellrank_7'],
            spellrank_8 = data['spellrank_8'],
            spellrank_9 = data['spellrank_9'],
            prereqtalent_1 = data['prereqtalent_1'],
            prereqtalent_2 = data['prereqtalent_2'],
            prereqtalent_3 = data['prereqtalent_3'],
            prereqrank_1 = data['prereqrank_1'],
            prereqrank_2 = data['prereqrank_2'],
            prereqrank_3 = data['prereqrank_3'],
            flags = data['flags'],
            requiredspellid = data['requiredspellid'],
            categorymask_1 = data['categorymask_1'],
            categorymask_2 = data['categorymask_2'],
        )