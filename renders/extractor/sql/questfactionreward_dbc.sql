
-- START questfactionreward_dbc
SET
@id := {id},
@difficulty_1 := {difficulty_1},
@difficulty_2 := {difficulty_2},
@difficulty_3 := {difficulty_3},
@difficulty_4 := {difficulty_4},
@difficulty_5 := {difficulty_5},
@difficulty_6 := {difficulty_6},
@difficulty_7 := {difficulty_7},
@difficulty_8 := {difficulty_8},
@difficulty_9 := {difficulty_9},
@difficulty_10 := {difficulty_10};

DELETE FROM questfactionreward_dbc WHERE
    id=@id
;

INSERT INTO questfactionreward_dbc (
    id,
    difficulty_1,
    difficulty_2,
    difficulty_3,
    difficulty_4,
    difficulty_5,
    difficulty_6,
    difficulty_7,
    difficulty_8,
    difficulty_9,
    difficulty_10
)
VALUES (
    @id,
    @difficulty_1,
    @difficulty_2,
    @difficulty_3,
    @difficulty_4,
    @difficulty_5,
    @difficulty_6,
    @difficulty_7,
    @difficulty_8,
    @difficulty_9,
    @difficulty_10
);
-- EOF questfactionreward_dbc