def sql_new_gameobject_template(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            entry = data['entry'],
            type = data['type'],
            displayid = data['displayid'],
            name = data['name'],
            iconname = data['iconname'],
            castbarcaption = data['castbarcaption'],
            unk1 = data['unk1'],
            size = data['size'],
            data0 = data['data0'],
            data1 = data['data1'],
            data2 = data['data2'],
            data3 = data['data3'],
            data4 = data['data4'],
            data5 = data['data5'],
            data6 = data['data6'],
            data7 = data['data7'],
            data8 = data['data8'],
            data9 = data['data9'],
            data10 = data['data10'],
            data11 = data['data11'],
            data12 = data['data12'],
            data13 = data['data13'],
            data14 = data['data14'],
            data15 = data['data15'],
            data16 = data['data16'],
            data17 = data['data17'],
            data18 = data['data18'],
            data19 = data['data19'],
            data20 = data['data20'],
            data21 = data['data21'],
            data22 = data['data22'],
            data23 = data['data23'],
            ainame = data['ainame'],
            scriptname = data['scriptname'],
            verifiedbuild = data['verifiedbuild'],
        )