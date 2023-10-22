def sql_new_spellshapeshiftform_dbc(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            id = data['id'],
            bonusactionbar = data['bonusactionbar'],
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
            flags = data['flags'],
            creaturetype = data['creaturetype'],
            attackiconid = data['attackiconid'],
            combatroundtime = data['combatroundtime'],
            creaturedisplayid_1 = data['creaturedisplayid_1'],
            creaturedisplayid_2 = data['creaturedisplayid_2'],
            creaturedisplayid_3 = data['creaturedisplayid_3'],
            creaturedisplayid_4 = data['creaturedisplayid_4'],
            presetspellid_1 = data['presetspellid_1'],
            presetspellid_2 = data['presetspellid_2'],
            presetspellid_3 = data['presetspellid_3'],
            presetspellid_4 = data['presetspellid_4'],
            presetspellid_5 = data['presetspellid_5'],
            presetspellid_6 = data['presetspellid_6'],
            presetspellid_7 = data['presetspellid_7'],
            presetspellid_8 = data['presetspellid_8'],
        )