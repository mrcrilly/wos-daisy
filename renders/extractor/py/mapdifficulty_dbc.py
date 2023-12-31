def sql_new_mapdifficulty_dbc(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            id = data['id'],
            mapid = data['mapid'],
            difficulty = data['difficulty'],
            message_lang_enus = data['message_lang_enus'],
            message_lang_engb = data['message_lang_engb'],
            message_lang_kokr = data['message_lang_kokr'],
            message_lang_frfr = data['message_lang_frfr'],
            message_lang_dede = data['message_lang_dede'],
            message_lang_encn = data['message_lang_encn'],
            message_lang_zhcn = data['message_lang_zhcn'],
            message_lang_entw = data['message_lang_entw'],
            message_lang_zhtw = data['message_lang_zhtw'],
            message_lang_eses = data['message_lang_eses'],
            message_lang_esmx = data['message_lang_esmx'],
            message_lang_ruru = data['message_lang_ruru'],
            message_lang_ptpt = data['message_lang_ptpt'],
            message_lang_ptbr = data['message_lang_ptbr'],
            message_lang_itit = data['message_lang_itit'],
            message_lang_unk = data['message_lang_unk'],
            message_lang_mask = data['message_lang_mask'],
            raidduration = data['raidduration'],
            maxplayers = data['maxplayers'],
            difficultystring = data['difficultystring'],
        )