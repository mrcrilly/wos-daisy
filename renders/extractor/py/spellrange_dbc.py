def sql_new_spellrange_dbc(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            id = data['id'],
            rangemin_1 = data['rangemin_1'],
            rangemin_2 = data['rangemin_2'],
            rangemax_1 = data['rangemax_1'],
            rangemax_2 = data['rangemax_2'],
            flags = data['flags'],
            displayname_lang_enus = data['displayname_lang_enus'],
            displayname_lang_engb = data['displayname_lang_engb'],
            displayname_lang_kokr = data['displayname_lang_kokr'],
            displayname_lang_frfr = data['displayname_lang_frfr'],
            displayname_lang_dede = data['displayname_lang_dede'],
            displayname_lang_encn = data['displayname_lang_encn'],
            displayname_lang_zhcn = data['displayname_lang_zhcn'],
            displayname_lang_entw = data['displayname_lang_entw'],
            displayname_lang_zhtw = data['displayname_lang_zhtw'],
            displayname_lang_eses = data['displayname_lang_eses'],
            displayname_lang_esmx = data['displayname_lang_esmx'],
            displayname_lang_ruru = data['displayname_lang_ruru'],
            displayname_lang_ptpt = data['displayname_lang_ptpt'],
            displayname_lang_ptbr = data['displayname_lang_ptbr'],
            displayname_lang_itit = data['displayname_lang_itit'],
            displayname_lang_unk = data['displayname_lang_unk'],
            displayname_lang_mask = data['displayname_lang_mask'],
            displaynameshort_lang_enus = data['displaynameshort_lang_enus'],
            displaynameshort_lang_engb = data['displaynameshort_lang_engb'],
            displaynameshort_lang_kokr = data['displaynameshort_lang_kokr'],
            displaynameshort_lang_frfr = data['displaynameshort_lang_frfr'],
            displaynameshort_lang_dede = data['displaynameshort_lang_dede'],
            displaynameshort_lang_encn = data['displaynameshort_lang_encn'],
            displaynameshort_lang_zhcn = data['displaynameshort_lang_zhcn'],
            displaynameshort_lang_entw = data['displaynameshort_lang_entw'],
            displaynameshort_lang_zhtw = data['displaynameshort_lang_zhtw'],
            displaynameshort_lang_eses = data['displaynameshort_lang_eses'],
            displaynameshort_lang_esmx = data['displaynameshort_lang_esmx'],
            displaynameshort_lang_ruru = data['displaynameshort_lang_ruru'],
            displaynameshort_lang_ptpt = data['displaynameshort_lang_ptpt'],
            displaynameshort_lang_ptbr = data['displaynameshort_lang_ptbr'],
            displaynameshort_lang_itit = data['displaynameshort_lang_itit'],
            displaynameshort_lang_unk = data['displaynameshort_lang_unk'],
            displaynameshort_lang_mask = data['displaynameshort_lang_mask'],
        )