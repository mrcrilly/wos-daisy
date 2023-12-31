
-- START player_factionchange_titles
SET
@alliance_id := {alliance_id},
@alliance_comment := '{alliance_comment}',
@horde_id := {horde_id},
@horde_comment := '{horde_comment}';

DELETE FROM player_factionchange_titles WHERE
    alliance_id=@alliance_id AND
    horde_id=@horde_id
;

INSERT INTO player_factionchange_titles (
    alliance_id,
    alliance_comment,
    horde_id,
    horde_comment
)
VALUES (
    @alliance_id,
    @alliance_comment,
    @horde_id,
    @horde_comment
);
-- EOF player_factionchange_titles