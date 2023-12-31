def sql_new_lfgdungeons_dbc(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            id = data['id'],
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
            minlevel = data['minlevel'],
            maxlevel = data['maxlevel'],
            target_level = data['target_level'],
            target_level_min = data['target_level_min'],
            target_level_max = data['target_level_max'],
            mapid = data['mapid'],
            difficulty = data['difficulty'],
            flags = data['flags'],
            typeid = data['typeid'],
            faction = data['faction'],
            texturefilename = data['texturefilename'],
            expansionlevel = data['expansionlevel'],
            order_index = data['order_index'],
            group_id = data['group_id'],
            description_lang_enus = data['description_lang_enus'],
            description_lang_engb = data['description_lang_engb'],
            description_lang_kokr = data['description_lang_kokr'],
            description_lang_frfr = data['description_lang_frfr'],
            description_lang_dede = data['description_lang_dede'],
            description_lang_encn = data['description_lang_encn'],
            description_lang_zhcn = data['description_lang_zhcn'],
            description_lang_entw = data['description_lang_entw'],
            description_lang_zhtw = data['description_lang_zhtw'],
            description_lang_eses = data['description_lang_eses'],
            description_lang_esmx = data['description_lang_esmx'],
            description_lang_ruru = data['description_lang_ruru'],
            description_lang_ptpt = data['description_lang_ptpt'],
            description_lang_ptbr = data['description_lang_ptbr'],
            description_lang_itit = data['description_lang_itit'],
            description_lang_unk = data['description_lang_unk'],
            description_lang_mask = data['description_lang_mask'],
        )