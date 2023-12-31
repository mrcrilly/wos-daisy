def sql_new_vehicleseat_dbc(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            id = data['id'],
            flags = data['flags'],
            attachmentid = data['attachmentid'],
            attachmentoffsetx = data['attachmentoffsetx'],
            attachmentoffsety = data['attachmentoffsety'],
            attachmentoffsetz = data['attachmentoffsetz'],
            enterpredelay = data['enterpredelay'],
            enterspeed = data['enterspeed'],
            entergravity = data['entergravity'],
            enterminduration = data['enterminduration'],
            entermaxduration = data['entermaxduration'],
            enterminarcheight = data['enterminarcheight'],
            entermaxarcheight = data['entermaxarcheight'],
            enteranimstart = data['enteranimstart'],
            enteranimloop = data['enteranimloop'],
            rideanimstart = data['rideanimstart'],
            rideanimloop = data['rideanimloop'],
            rideupperanimstart = data['rideupperanimstart'],
            rideupperanimloop = data['rideupperanimloop'],
            exitpredelay = data['exitpredelay'],
            exitspeed = data['exitspeed'],
            exitgravity = data['exitgravity'],
            exitminduration = data['exitminduration'],
            exitmaxduration = data['exitmaxduration'],
            exitminarcheight = data['exitminarcheight'],
            exitmaxarcheight = data['exitmaxarcheight'],
            exitanimstart = data['exitanimstart'],
            exitanimloop = data['exitanimloop'],
            exitanimend = data['exitanimend'],
            passengeryaw = data['passengeryaw'],
            passengerpitch = data['passengerpitch'],
            passengerroll = data['passengerroll'],
            passengerattachmentid = data['passengerattachmentid'],
            vehicleenteranim = data['vehicleenteranim'],
            vehicleexitanim = data['vehicleexitanim'],
            vehiclerideanimloop = data['vehiclerideanimloop'],
            vehicleenteranimbone = data['vehicleenteranimbone'],
            vehicleexitanimbone = data['vehicleexitanimbone'],
            vehiclerideanimloopbone = data['vehiclerideanimloopbone'],
            vehicleenteranimdelay = data['vehicleenteranimdelay'],
            vehicleexitanimdelay = data['vehicleexitanimdelay'],
            vehicleabilitydisplay = data['vehicleabilitydisplay'],
            enteruisoundid = data['enteruisoundid'],
            exituisoundid = data['exituisoundid'],
            uiskin = data['uiskin'],
            flagsb = data['flagsb'],
            cameraenteringdelay = data['cameraenteringdelay'],
            cameraenteringduration = data['cameraenteringduration'],
            cameraexitingdelay = data['cameraexitingdelay'],
            cameraexitingduration = data['cameraexitingduration'],
            cameraoffsetx = data['cameraoffsetx'],
            cameraoffsety = data['cameraoffsety'],
            cameraoffsetz = data['cameraoffsetz'],
            cameraposchaserate = data['cameraposchaserate'],
            camerafacingchaserate = data['camerafacingchaserate'],
            cameraenteringzoom = data['cameraenteringzoom'],
            cameraseatzoommin = data['cameraseatzoommin'],
            cameraseatzoommax = data['cameraseatzoommax'],
        )