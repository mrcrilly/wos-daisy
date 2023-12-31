def sql_new_creature_template(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            entry = data['entry'],
            difficulty_entry_1 = data['difficulty_entry_1'],
            difficulty_entry_2 = data['difficulty_entry_2'],
            difficulty_entry_3 = data['difficulty_entry_3'],
            killcredit1 = data['killcredit1'],
            killcredit2 = data['killcredit2'],
            modelid1 = data['modelid1'],
            modelid2 = data['modelid2'],
            modelid3 = data['modelid3'],
            modelid4 = data['modelid4'],
            name = data['name'],
            subname = data['subname'],
            iconname = data['iconname'],
            gossip_menu_id = data['gossip_menu_id'],
            minlevel = data['minlevel'],
            maxlevel = data['maxlevel'],
            exp = data['exp'],
            faction = data['faction'],
            npcflag = data['npcflag'],
            speed_walk = data['speed_walk'],
            speed_run = data['speed_run'],
            speed_swim = data['speed_swim'],
            speed_flight = data['speed_flight'],
            detection_range = data['detection_range'],
            scale = data['scale'],
            rank = data['rank'],
            dmgschool = data['dmgschool'],
            damagemodifier = data['damagemodifier'],
            baseattacktime = data['baseattacktime'],
            rangeattacktime = data['rangeattacktime'],
            basevariance = data['basevariance'],
            rangevariance = data['rangevariance'],
            unit_class = data['unit_class'],
            unit_flags = data['unit_flags'],
            unit_flags2 = data['unit_flags2'],
            dynamicflags = data['dynamicflags'],
            family = data['family'],
            trainer_type = data['trainer_type'],
            trainer_spell = data['trainer_spell'],
            trainer_class = data['trainer_class'],
            trainer_race = data['trainer_race'],
            type = data['type'],
            type_flags = data['type_flags'],
            lootid = data['lootid'],
            pickpocketloot = data['pickpocketloot'],
            skinloot = data['skinloot'],
            petspelldataid = data['petspelldataid'],
            vehicleid = data['vehicleid'],
            mingold = data['mingold'],
            maxgold = data['maxgold'],
            ainame = data['ainame'],
            movementtype = data['movementtype'],
            hoverheight = data['hoverheight'],
            healthmodifier = data['healthmodifier'],
            manamodifier = data['manamodifier'],
            armormodifier = data['armormodifier'],
            experiencemodifier = data['experiencemodifier'],
            racialleader = data['racialleader'],
            movementid = data['movementid'],
            regenhealth = data['regenhealth'],
            mechanic_immune_mask = data['mechanic_immune_mask'],
            spell_school_immune_mask = data['spell_school_immune_mask'],
            flags_extra = data['flags_extra'],
            scriptname = data['scriptname'],
            verifiedbuild = data['verifiedbuild'],
        )