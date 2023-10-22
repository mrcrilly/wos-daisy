def sql_new_battlemasterlist_dbc(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            id = data['id'],
            mapid_1 = data['mapid_1'],
            mapid_2 = data['mapid_2'],
            mapid_3 = data['mapid_3'],
            mapid_4 = data['mapid_4'],
            mapid_5 = data['mapid_5'],
            mapid_6 = data['mapid_6'],
            mapid_7 = data['mapid_7'],
            mapid_8 = data['mapid_8'],
            instancetype = data['instancetype'],
            groupsallowed = data['groupsallowed'],
            name_lang_enus = data['name_lang_enus'],
            name_lang_engb = data['name_lang_engb'],
            name_lang_kokr = data['name_lang_kokr'],
            name_lang_frfr = data['name_lang_frfr'],
            name_lang_dede = data['name_lang_dede'],
            name_lang_encn = data['name_lang_encn'],
            name_lang_zhcn = data['name_lang_zhcn'],
            name_lang_entw = data['name_lang_entw'],
            name_lang_zhtw = data['name_lang_zhtw'],
            name_lang_eses = data['name_lang_eses'],
            name_lang_esmx = data['name_lang_esmx'],
            name_lang_ruru = data['name_lang_ruru'],
            name_lang_ptpt = data['name_lang_ptpt'],
            name_lang_ptbr = data['name_lang_ptbr'],
            name_lang_itit = data['name_lang_itit'],
            name_lang_unk = data['name_lang_unk'],
            name_lang_mask = data['name_lang_mask'],
            maxgroupsize = data['maxgroupsize'],
            holidayworldstate = data['holidayworldstate'],
            minlevel = data['minlevel'],
            maxlevel = data['maxlevel'],
        )