
-- START areatable_dbc
SET
@id := {id},
@continentid := {continentid},
@parentareaid := {parentareaid},
@areabit := {areabit},
@flags := {flags},
@soundproviderpref := {soundproviderpref},
@soundproviderprefunderwater := {soundproviderprefunderwater},
@ambienceid := {ambienceid},
@zonemusic := {zonemusic},
@introsound := {introsound},
@explorationlevel := {explorationlevel},
@areaname_lang_enus := '{areaname_lang_enus}',
@areaname_lang_engb := '{areaname_lang_engb}',
@areaname_lang_kokr := '{areaname_lang_kokr}',
@areaname_lang_frfr := '{areaname_lang_frfr}',
@areaname_lang_dede := '{areaname_lang_dede}',
@areaname_lang_encn := '{areaname_lang_encn}',
@areaname_lang_zhcn := '{areaname_lang_zhcn}',
@areaname_lang_entw := '{areaname_lang_entw}',
@areaname_lang_zhtw := '{areaname_lang_zhtw}',
@areaname_lang_eses := '{areaname_lang_eses}',
@areaname_lang_esmx := '{areaname_lang_esmx}',
@areaname_lang_ruru := '{areaname_lang_ruru}',
@areaname_lang_ptpt := '{areaname_lang_ptpt}',
@areaname_lang_ptbr := '{areaname_lang_ptbr}',
@areaname_lang_itit := '{areaname_lang_itit}',
@areaname_lang_unk := '{areaname_lang_unk}',
@areaname_lang_mask := {areaname_lang_mask},
@factiongroupmask := {factiongroupmask},
@liquidtypeid_1 := {liquidtypeid_1},
@liquidtypeid_2 := {liquidtypeid_2},
@liquidtypeid_3 := {liquidtypeid_3},
@liquidtypeid_4 := {liquidtypeid_4},
@minelevation := {minelevation},
@ambient_multiplier := {ambient_multiplier},
@lightid := {lightid};

DELETE FROM areatable_dbc WHERE
    id=@id
;

INSERT INTO areatable_dbc (
    id,
    continentid,
    parentareaid,
    areabit,
    flags,
    soundproviderpref,
    soundproviderprefunderwater,
    ambienceid,
    zonemusic,
    introsound,
    explorationlevel,
    areaname_lang_enus,
    areaname_lang_engb,
    areaname_lang_kokr,
    areaname_lang_frfr,
    areaname_lang_dede,
    areaname_lang_encn,
    areaname_lang_zhcn,
    areaname_lang_entw,
    areaname_lang_zhtw,
    areaname_lang_eses,
    areaname_lang_esmx,
    areaname_lang_ruru,
    areaname_lang_ptpt,
    areaname_lang_ptbr,
    areaname_lang_itit,
    areaname_lang_unk,
    areaname_lang_mask,
    factiongroupmask,
    liquidtypeid_1,
    liquidtypeid_2,
    liquidtypeid_3,
    liquidtypeid_4,
    minelevation,
    ambient_multiplier,
    lightid
)
VALUES (
    @id,
    @continentid,
    @parentareaid,
    @areabit,
    @flags,
    @soundproviderpref,
    @soundproviderprefunderwater,
    @ambienceid,
    @zonemusic,
    @introsound,
    @explorationlevel,
    @areaname_lang_enus,
    @areaname_lang_engb,
    @areaname_lang_kokr,
    @areaname_lang_frfr,
    @areaname_lang_dede,
    @areaname_lang_encn,
    @areaname_lang_zhcn,
    @areaname_lang_entw,
    @areaname_lang_zhtw,
    @areaname_lang_eses,
    @areaname_lang_esmx,
    @areaname_lang_ruru,
    @areaname_lang_ptpt,
    @areaname_lang_ptbr,
    @areaname_lang_itit,
    @areaname_lang_unk,
    @areaname_lang_mask,
    @factiongroupmask,
    @liquidtypeid_1,
    @liquidtypeid_2,
    @liquidtypeid_3,
    @liquidtypeid_4,
    @minelevation,
    @ambient_multiplier,
    @lightid
);
-- EOF areatable_dbc