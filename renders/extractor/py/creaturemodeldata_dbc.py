def sql_new_creaturemodeldata_dbc(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            id = data['id'],
            flags = data['flags'],
            modelname = data['modelname'],
            sizeclass = data['sizeclass'],
            modelscale = data['modelscale'],
            bloodid = data['bloodid'],
            footprinttextureid = data['footprinttextureid'],
            footprinttexturelength = data['footprinttexturelength'],
            footprinttexturewidth = data['footprinttexturewidth'],
            footprintparticlescale = data['footprintparticlescale'],
            foleymaterialid = data['foleymaterialid'],
            footstepshakesize = data['footstepshakesize'],
            deaththudshakesize = data['deaththudshakesize'],
            soundid = data['soundid'],
            collisionwidth = data['collisionwidth'],
            collisionheight = data['collisionheight'],
            mountheight = data['mountheight'],
            geoboxminx = data['geoboxminx'],
            geoboxminy = data['geoboxminy'],
            geoboxminz = data['geoboxminz'],
            geoboxmaxx = data['geoboxmaxx'],
            geoboxmaxy = data['geoboxmaxy'],
            geoboxmaxz = data['geoboxmaxz'],
            worldeffectscale = data['worldeffectscale'],
            attachedeffectscale = data['attachedeffectscale'],
            missilecollisionradius = data['missilecollisionradius'],
            missilecollisionpush = data['missilecollisionpush'],
            missilecollisionraise = data['missilecollisionraise'],
        )