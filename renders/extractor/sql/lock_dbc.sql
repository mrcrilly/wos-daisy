
-- START lock_dbc
SET
@id := {id},
@type_1 := {type_1},
@type_2 := {type_2},
@type_3 := {type_3},
@type_4 := {type_4},
@type_5 := {type_5},
@type_6 := {type_6},
@type_7 := {type_7},
@type_8 := {type_8},
@index_1 := {index_1},
@index_2 := {index_2},
@index_3 := {index_3},
@index_4 := {index_4},
@index_5 := {index_5},
@index_6 := {index_6},
@index_7 := {index_7},
@index_8 := {index_8},
@skill_1 := {skill_1},
@skill_2 := {skill_2},
@skill_3 := {skill_3},
@skill_4 := {skill_4},
@skill_5 := {skill_5},
@skill_6 := {skill_6},
@skill_7 := {skill_7},
@skill_8 := {skill_8},
@action_1 := {action_1},
@action_2 := {action_2},
@action_3 := {action_3},
@action_4 := {action_4},
@action_5 := {action_5},
@action_6 := {action_6},
@action_7 := {action_7},
@action_8 := {action_8};

DELETE FROM lock_dbc WHERE
    id=@id
;

INSERT INTO lock_dbc (
    id,
    type_1,
    type_2,
    type_3,
    type_4,
    type_5,
    type_6,
    type_7,
    type_8,
    index_1,
    index_2,
    index_3,
    index_4,
    index_5,
    index_6,
    index_7,
    index_8,
    skill_1,
    skill_2,
    skill_3,
    skill_4,
    skill_5,
    skill_6,
    skill_7,
    skill_8,
    action_1,
    action_2,
    action_3,
    action_4,
    action_5,
    action_6,
    action_7,
    action_8
)
VALUES (
    @id,
    @type_1,
    @type_2,
    @type_3,
    @type_4,
    @type_5,
    @type_6,
    @type_7,
    @type_8,
    @index_1,
    @index_2,
    @index_3,
    @index_4,
    @index_5,
    @index_6,
    @index_7,
    @index_8,
    @skill_1,
    @skill_2,
    @skill_3,
    @skill_4,
    @skill_5,
    @skill_6,
    @skill_7,
    @skill_8,
    @action_1,
    @action_2,
    @action_3,
    @action_4,
    @action_5,
    @action_6,
    @action_7,
    @action_8
);
-- EOF lock_dbc