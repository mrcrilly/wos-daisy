
-- START areapoi_dbc
SET
@id := {id},
@importance := {importance},
@icon_1 := {icon_1},
@icon_2 := {icon_2},
@icon_3 := {icon_3},
@icon_4 := {icon_4},
@icon_5 := {icon_5},
@icon_6 := {icon_6},
@icon_7 := {icon_7},
@icon_8 := {icon_8},
@icon_9 := {icon_9},
@factionid := {factionid},
@x := {x},
@y := {y},
@z := {z},
@continentid := {continentid},
@flags := {flags},
@areaid := {areaid},
@name_lang_enus := '{name_lang_enus}',
@name_lang_engb := '{name_lang_engb}',
@name_lang_kokr := '{name_lang_kokr}',
@name_lang_frfr := '{name_lang_frfr}',
@name_lang_dede := '{name_lang_dede}',
@name_lang_encn := '{name_lang_encn}',
@name_lang_zhcn := '{name_lang_zhcn}',
@name_lang_entw := '{name_lang_entw}',
@name_lang_zhtw := '{name_lang_zhtw}',
@name_lang_eses := '{name_lang_eses}',
@name_lang_esmx := '{name_lang_esmx}',
@name_lang_ruru := '{name_lang_ruru}',
@name_lang_ptpt := '{name_lang_ptpt}',
@name_lang_ptbr := '{name_lang_ptbr}',
@name_lang_itit := '{name_lang_itit}',
@name_lang_unk := '{name_lang_unk}',
@name_lang_mask := {name_lang_mask},
@description_lang_enus := '{description_lang_enus}',
@description_lang_engb := '{description_lang_engb}',
@description_lang_kokr := '{description_lang_kokr}',
@description_lang_frfr := '{description_lang_frfr}',
@description_lang_dede := '{description_lang_dede}',
@description_lang_encn := '{description_lang_encn}',
@description_lang_zhcn := '{description_lang_zhcn}',
@description_lang_entw := '{description_lang_entw}',
@description_lang_zhtw := '{description_lang_zhtw}',
@description_lang_eses := '{description_lang_eses}',
@description_lang_esmx := '{description_lang_esmx}',
@description_lang_ruru := '{description_lang_ruru}',
@description_lang_ptpt := '{description_lang_ptpt}',
@description_lang_ptbr := '{description_lang_ptbr}',
@description_lang_itit := '{description_lang_itit}',
@description_lang_unk := '{description_lang_unk}',
@description_lang_mask := {description_lang_mask},
@worldstateid := {worldstateid},
@worldmaplink := {worldmaplink};

DELETE FROM areapoi_dbc WHERE
    id=@id
;

INSERT INTO areapoi_dbc (
    id,
    importance,
    icon_1,
    icon_2,
    icon_3,
    icon_4,
    icon_5,
    icon_6,
    icon_7,
    icon_8,
    icon_9,
    factionid,
    x,
    y,
    z,
    continentid,
    flags,
    areaid,
    name_lang_enus,
    name_lang_engb,
    name_lang_kokr,
    name_lang_frfr,
    name_lang_dede,
    name_lang_encn,
    name_lang_zhcn,
    name_lang_entw,
    name_lang_zhtw,
    name_lang_eses,
    name_lang_esmx,
    name_lang_ruru,
    name_lang_ptpt,
    name_lang_ptbr,
    name_lang_itit,
    name_lang_unk,
    name_lang_mask,
    description_lang_enus,
    description_lang_engb,
    description_lang_kokr,
    description_lang_frfr,
    description_lang_dede,
    description_lang_encn,
    description_lang_zhcn,
    description_lang_entw,
    description_lang_zhtw,
    description_lang_eses,
    description_lang_esmx,
    description_lang_ruru,
    description_lang_ptpt,
    description_lang_ptbr,
    description_lang_itit,
    description_lang_unk,
    description_lang_mask,
    worldstateid,
    worldmaplink
)
VALUES (
    @id,
    @importance,
    @icon_1,
    @icon_2,
    @icon_3,
    @icon_4,
    @icon_5,
    @icon_6,
    @icon_7,
    @icon_8,
    @icon_9,
    @factionid,
    @x,
    @y,
    @z,
    @continentid,
    @flags,
    @areaid,
    @name_lang_enus,
    @name_lang_engb,
    @name_lang_kokr,
    @name_lang_frfr,
    @name_lang_dede,
    @name_lang_encn,
    @name_lang_zhcn,
    @name_lang_entw,
    @name_lang_zhtw,
    @name_lang_eses,
    @name_lang_esmx,
    @name_lang_ruru,
    @name_lang_ptpt,
    @name_lang_ptbr,
    @name_lang_itit,
    @name_lang_unk,
    @name_lang_mask,
    @description_lang_enus,
    @description_lang_engb,
    @description_lang_kokr,
    @description_lang_frfr,
    @description_lang_dede,
    @description_lang_encn,
    @description_lang_zhcn,
    @description_lang_entw,
    @description_lang_zhtw,
    @description_lang_eses,
    @description_lang_esmx,
    @description_lang_ruru,
    @description_lang_ptpt,
    @description_lang_ptbr,
    @description_lang_itit,
    @description_lang_unk,
    @description_lang_mask,
    @worldstateid,
    @worldmaplink
);
-- EOF areapoi_dbc