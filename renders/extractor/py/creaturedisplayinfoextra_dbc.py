def sql_new_creaturedisplayinfoextra_dbc(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            id = data['id'],
            displayraceid = data['displayraceid'],
            displaysexid = data['displaysexid'],
            skinid = data['skinid'],
            faceid = data['faceid'],
            hairstyleid = data['hairstyleid'],
            haircolorid = data['haircolorid'],
            facialhairid = data['facialhairid'],
            npcitemdisplay1 = data['npcitemdisplay1'],
            npcitemdisplay2 = data['npcitemdisplay2'],
            npcitemdisplay3 = data['npcitemdisplay3'],
            npcitemdisplay4 = data['npcitemdisplay4'],
            npcitemdisplay5 = data['npcitemdisplay5'],
            npcitemdisplay6 = data['npcitemdisplay6'],
            npcitemdisplay7 = data['npcitemdisplay7'],
            npcitemdisplay8 = data['npcitemdisplay8'],
            npcitemdisplay9 = data['npcitemdisplay9'],
            npcitemdisplay10 = data['npcitemdisplay10'],
            npcitemdisplay11 = data['npcitemdisplay11'],
            flags = data['flags'],
            bakename = data['bakename'],
        )