
-- START creaturefamily_dbc
SET
@id := {id},
@minscale := {minscale},
@minscalelevel := {minscalelevel},
@maxscale := {maxscale},
@maxscalelevel := {maxscalelevel},
@skillline_1 := {skillline_1},
@skillline_2 := {skillline_2},
@petfoodmask := {petfoodmask},
@pettalenttype := {pettalenttype},
@categoryenumid := {categoryenumid},
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
@iconfile := '{iconfile}';

DELETE FROM creaturefamily_dbc WHERE
    id=@id
;

INSERT INTO creaturefamily_dbc (
    id,
    minscale,
    minscalelevel,
    maxscale,
    maxscalelevel,
    skillline_1,
    skillline_2,
    petfoodmask,
    pettalenttype,
    categoryenumid,
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
    iconfile
)
VALUES (
    @id,
    @minscale,
    @minscalelevel,
    @maxscale,
    @maxscalelevel,
    @skillline_1,
    @skillline_2,
    @petfoodmask,
    @pettalenttype,
    @categoryenumid,
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
    @iconfile
);
-- EOF creaturefamily_dbc