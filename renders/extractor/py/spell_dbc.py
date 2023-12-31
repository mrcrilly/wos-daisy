def sql_new_spell_dbc(data, path):
    with open(path, 'r') as fd:
        return fd.read().format(
            id = data['id'],
            category = data['category'],
            dispeltype = data['dispeltype'],
            mechanic = data['mechanic'],
            attributes = data['attributes'],
            attributesex = data['attributesex'],
            attributesex2 = data['attributesex2'],
            attributesex3 = data['attributesex3'],
            attributesex4 = data['attributesex4'],
            attributesex5 = data['attributesex5'],
            attributesex6 = data['attributesex6'],
            attributesex7 = data['attributesex7'],
            shapeshiftmask = data['shapeshiftmask'],
            unk_320_2 = data['unk_320_2'],
            shapeshiftexclude = data['shapeshiftexclude'],
            unk_320_3 = data['unk_320_3'],
            targets = data['targets'],
            targetcreaturetype = data['targetcreaturetype'],
            requiresspellfocus = data['requiresspellfocus'],
            facingcasterflags = data['facingcasterflags'],
            casteraurastate = data['casteraurastate'],
            targetaurastate = data['targetaurastate'],
            excludecasteraurastate = data['excludecasteraurastate'],
            excludetargetaurastate = data['excludetargetaurastate'],
            casterauraspell = data['casterauraspell'],
            targetauraspell = data['targetauraspell'],
            excludecasterauraspell = data['excludecasterauraspell'],
            excludetargetauraspell = data['excludetargetauraspell'],
            castingtimeindex = data['castingtimeindex'],
            recoverytime = data['recoverytime'],
            categoryrecoverytime = data['categoryrecoverytime'],
            interruptflags = data['interruptflags'],
            aurainterruptflags = data['aurainterruptflags'],
            channelinterruptflags = data['channelinterruptflags'],
            proctypemask = data['proctypemask'],
            procchance = data['procchance'],
            proccharges = data['proccharges'],
            maxlevel = data['maxlevel'],
            baselevel = data['baselevel'],
            spelllevel = data['spelllevel'],
            durationindex = data['durationindex'],
            powertype = data['powertype'],
            manacost = data['manacost'],
            manacostperlevel = data['manacostperlevel'],
            manapersecond = data['manapersecond'],
            manapersecondperlevel = data['manapersecondperlevel'],
            rangeindex = data['rangeindex'],
            speed = data['speed'],
            modalnextspell = data['modalnextspell'],
            cumulativeaura = data['cumulativeaura'],
            totem_1 = data['totem_1'],
            totem_2 = data['totem_2'],
            reagent_1 = data['reagent_1'],
            reagent_2 = data['reagent_2'],
            reagent_3 = data['reagent_3'],
            reagent_4 = data['reagent_4'],
            reagent_5 = data['reagent_5'],
            reagent_6 = data['reagent_6'],
            reagent_7 = data['reagent_7'],
            reagent_8 = data['reagent_8'],
            reagentcount_1 = data['reagentcount_1'],
            reagentcount_2 = data['reagentcount_2'],
            reagentcount_3 = data['reagentcount_3'],
            reagentcount_4 = data['reagentcount_4'],
            reagentcount_5 = data['reagentcount_5'],
            reagentcount_6 = data['reagentcount_6'],
            reagentcount_7 = data['reagentcount_7'],
            reagentcount_8 = data['reagentcount_8'],
            equippeditemclass = data['equippeditemclass'],
            equippeditemsubclass = data['equippeditemsubclass'],
            equippediteminvtypes = data['equippediteminvtypes'],
            effect_1 = data['effect_1'],
            effect_2 = data['effect_2'],
            effect_3 = data['effect_3'],
            effectdiesides_1 = data['effectdiesides_1'],
            effectdiesides_2 = data['effectdiesides_2'],
            effectdiesides_3 = data['effectdiesides_3'],
            effectrealpointsperlevel_1 = data['effectrealpointsperlevel_1'],
            effectrealpointsperlevel_2 = data['effectrealpointsperlevel_2'],
            effectrealpointsperlevel_3 = data['effectrealpointsperlevel_3'],
            effectbasepoints_1 = data['effectbasepoints_1'],
            effectbasepoints_2 = data['effectbasepoints_2'],
            effectbasepoints_3 = data['effectbasepoints_3'],
            effectmechanic_1 = data['effectmechanic_1'],
            effectmechanic_2 = data['effectmechanic_2'],
            effectmechanic_3 = data['effectmechanic_3'],
            implicittargeta_1 = data['implicittargeta_1'],
            implicittargeta_2 = data['implicittargeta_2'],
            implicittargeta_3 = data['implicittargeta_3'],
            implicittargetb_1 = data['implicittargetb_1'],
            implicittargetb_2 = data['implicittargetb_2'],
            implicittargetb_3 = data['implicittargetb_3'],
            effectradiusindex_1 = data['effectradiusindex_1'],
            effectradiusindex_2 = data['effectradiusindex_2'],
            effectradiusindex_3 = data['effectradiusindex_3'],
            effectaura_1 = data['effectaura_1'],
            effectaura_2 = data['effectaura_2'],
            effectaura_3 = data['effectaura_3'],
            effectauraperiod_1 = data['effectauraperiod_1'],
            effectauraperiod_2 = data['effectauraperiod_2'],
            effectauraperiod_3 = data['effectauraperiod_3'],
            effectmultiplevalue_1 = data['effectmultiplevalue_1'],
            effectmultiplevalue_2 = data['effectmultiplevalue_2'],
            effectmultiplevalue_3 = data['effectmultiplevalue_3'],
            effectchaintargets_1 = data['effectchaintargets_1'],
            effectchaintargets_2 = data['effectchaintargets_2'],
            effectchaintargets_3 = data['effectchaintargets_3'],
            effectitemtype_1 = data['effectitemtype_1'],
            effectitemtype_2 = data['effectitemtype_2'],
            effectitemtype_3 = data['effectitemtype_3'],
            effectmiscvalue_1 = data['effectmiscvalue_1'],
            effectmiscvalue_2 = data['effectmiscvalue_2'],
            effectmiscvalue_3 = data['effectmiscvalue_3'],
            effectmiscvalueb_1 = data['effectmiscvalueb_1'],
            effectmiscvalueb_2 = data['effectmiscvalueb_2'],
            effectmiscvalueb_3 = data['effectmiscvalueb_3'],
            effecttriggerspell_1 = data['effecttriggerspell_1'],
            effecttriggerspell_2 = data['effecttriggerspell_2'],
            effecttriggerspell_3 = data['effecttriggerspell_3'],
            effectpointspercombo_1 = data['effectpointspercombo_1'],
            effectpointspercombo_2 = data['effectpointspercombo_2'],
            effectpointspercombo_3 = data['effectpointspercombo_3'],
            effectspellclassmaska_1 = data['effectspellclassmaska_1'],
            effectspellclassmaska_2 = data['effectspellclassmaska_2'],
            effectspellclassmaska_3 = data['effectspellclassmaska_3'],
            effectspellclassmaskb_1 = data['effectspellclassmaskb_1'],
            effectspellclassmaskb_2 = data['effectspellclassmaskb_2'],
            effectspellclassmaskb_3 = data['effectspellclassmaskb_3'],
            effectspellclassmaskc_1 = data['effectspellclassmaskc_1'],
            effectspellclassmaskc_2 = data['effectspellclassmaskc_2'],
            effectspellclassmaskc_3 = data['effectspellclassmaskc_3'],
            spellvisualid_1 = data['spellvisualid_1'],
            spellvisualid_2 = data['spellvisualid_2'],
            spelliconid = data['spelliconid'],
            activeiconid = data['activeiconid'],
            spellpriority = data['spellpriority'],
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
            namesubtext_lang_enus = data['namesubtext_lang_enus'],
            namesubtext_lang_engb = data['namesubtext_lang_engb'],
            namesubtext_lang_kokr = data['namesubtext_lang_kokr'],
            namesubtext_lang_frfr = data['namesubtext_lang_frfr'],
            namesubtext_lang_dede = data['namesubtext_lang_dede'],
            namesubtext_lang_encn = data['namesubtext_lang_encn'],
            namesubtext_lang_zhcn = data['namesubtext_lang_zhcn'],
            namesubtext_lang_entw = data['namesubtext_lang_entw'],
            namesubtext_lang_zhtw = data['namesubtext_lang_zhtw'],
            namesubtext_lang_eses = data['namesubtext_lang_eses'],
            namesubtext_lang_esmx = data['namesubtext_lang_esmx'],
            namesubtext_lang_ruru = data['namesubtext_lang_ruru'],
            namesubtext_lang_ptpt = data['namesubtext_lang_ptpt'],
            namesubtext_lang_ptbr = data['namesubtext_lang_ptbr'],
            namesubtext_lang_itit = data['namesubtext_lang_itit'],
            namesubtext_lang_unk = data['namesubtext_lang_unk'],
            namesubtext_lang_mask = data['namesubtext_lang_mask'],
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
            auradescription_lang_enus = data['auradescription_lang_enus'],
            auradescription_lang_engb = data['auradescription_lang_engb'],
            auradescription_lang_kokr = data['auradescription_lang_kokr'],
            auradescription_lang_frfr = data['auradescription_lang_frfr'],
            auradescription_lang_dede = data['auradescription_lang_dede'],
            auradescription_lang_encn = data['auradescription_lang_encn'],
            auradescription_lang_zhcn = data['auradescription_lang_zhcn'],
            auradescription_lang_entw = data['auradescription_lang_entw'],
            auradescription_lang_zhtw = data['auradescription_lang_zhtw'],
            auradescription_lang_eses = data['auradescription_lang_eses'],
            auradescription_lang_esmx = data['auradescription_lang_esmx'],
            auradescription_lang_ruru = data['auradescription_lang_ruru'],
            auradescription_lang_ptpt = data['auradescription_lang_ptpt'],
            auradescription_lang_ptbr = data['auradescription_lang_ptbr'],
            auradescription_lang_itit = data['auradescription_lang_itit'],
            auradescription_lang_unk = data['auradescription_lang_unk'],
            auradescription_lang_mask = data['auradescription_lang_mask'],
            manacostpct = data['manacostpct'],
            startrecoverycategory = data['startrecoverycategory'],
            startrecoverytime = data['startrecoverytime'],
            maxtargetlevel = data['maxtargetlevel'],
            spellclassset = data['spellclassset'],
            spellclassmask_1 = data['spellclassmask_1'],
            spellclassmask_2 = data['spellclassmask_2'],
            spellclassmask_3 = data['spellclassmask_3'],
            maxtargets = data['maxtargets'],
            defensetype = data['defensetype'],
            preventiontype = data['preventiontype'],
            stancebarorder = data['stancebarorder'],
            effectchainamplitude_1 = data['effectchainamplitude_1'],
            effectchainamplitude_2 = data['effectchainamplitude_2'],
            effectchainamplitude_3 = data['effectchainamplitude_3'],
            minfactionid = data['minfactionid'],
            minreputation = data['minreputation'],
            requiredauravision = data['requiredauravision'],
            requiredtotemcategoryid_1 = data['requiredtotemcategoryid_1'],
            requiredtotemcategoryid_2 = data['requiredtotemcategoryid_2'],
            requiredareasid = data['requiredareasid'],
            schoolmask = data['schoolmask'],
            runecostid = data['runecostid'],
            spellmissileid = data['spellmissileid'],
            powerdisplayid = data['powerdisplayid'],
            effectbonusmultiplier_1 = data['effectbonusmultiplier_1'],
            effectbonusmultiplier_2 = data['effectbonusmultiplier_2'],
            effectbonusmultiplier_3 = data['effectbonusmultiplier_3'],
            spelldescriptionvariableid = data['spelldescriptionvariableid'],
            spelldifficultyid = data['spelldifficultyid'],
        )