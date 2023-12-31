def sql_new_soundentries_dbc(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            id = data['id'],
            soundtype = data['soundtype'],
            name = data['name'],
            file_1 = data['file_1'],
            file_2 = data['file_2'],
            file_3 = data['file_3'],
            file_4 = data['file_4'],
            file_5 = data['file_5'],
            file_6 = data['file_6'],
            file_7 = data['file_7'],
            file_8 = data['file_8'],
            file_9 = data['file_9'],
            file_10 = data['file_10'],
            freq_1 = data['freq_1'],
            freq_2 = data['freq_2'],
            freq_3 = data['freq_3'],
            freq_4 = data['freq_4'],
            freq_5 = data['freq_5'],
            freq_6 = data['freq_6'],
            freq_7 = data['freq_7'],
            freq_8 = data['freq_8'],
            freq_9 = data['freq_9'],
            freq_10 = data['freq_10'],
            directorybase = data['directorybase'],
            volumefloat = data['volumefloat'],
            flags = data['flags'],
            mindistance = data['mindistance'],
            distancecutoff = data['distancecutoff'],
            eaxdef = data['eaxdef'],
            soundentriesadvancedid = data['soundentriesadvancedid'],
        )