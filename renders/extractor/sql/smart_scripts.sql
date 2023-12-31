
-- START smart_scripts
SET
@entryorguid := {entryorguid},
@source_type := {source_type},
@id := {id},
@link := {link},
@event_type := {event_type},
@event_phase_mask := {event_phase_mask},
@event_chance := {event_chance},
@event_flags := {event_flags},
@event_param1 := {event_param1},
@event_param2 := {event_param2},
@event_param3 := {event_param3},
@event_param4 := {event_param4},
@event_param5 := {event_param5},
@event_param6 := {event_param6},
@action_type := {action_type},
@action_param1 := {action_param1},
@action_param2 := {action_param2},
@action_param3 := {action_param3},
@action_param4 := {action_param4},
@action_param5 := {action_param5},
@action_param6 := {action_param6},
@target_type := {target_type},
@target_param1 := {target_param1},
@target_param2 := {target_param2},
@target_param3 := {target_param3},
@target_param4 := {target_param4},
@target_x := {target_x},
@target_y := {target_y},
@target_z := {target_z},
@target_o := {target_o},
@comment := '{comment}';

DELETE FROM smart_scripts WHERE
    entryorguid=@entryorguid AND
    source_type=@source_type AND
    id=@id AND
    link=@link
;

INSERT INTO smart_scripts (
    entryorguid,
    source_type,
    id,
    link,
    event_type,
    event_phase_mask,
    event_chance,
    event_flags,
    event_param1,
    event_param2,
    event_param3,
    event_param4,
    event_param5,
    event_param6,
    action_type,
    action_param1,
    action_param2,
    action_param3,
    action_param4,
    action_param5,
    action_param6,
    target_type,
    target_param1,
    target_param2,
    target_param3,
    target_param4,
    target_x,
    target_y,
    target_z,
    target_o,
    comment
)
VALUES (
    @entryorguid,
    @source_type,
    @id,
    @link,
    @event_type,
    @event_phase_mask,
    @event_chance,
    @event_flags,
    @event_param1,
    @event_param2,
    @event_param3,
    @event_param4,
    @event_param5,
    @event_param6,
    @action_type,
    @action_param1,
    @action_param2,
    @action_param3,
    @action_param4,
    @action_param5,
    @action_param6,
    @target_type,
    @target_param1,
    @target_param2,
    @target_param3,
    @target_param4,
    @target_x,
    @target_y,
    @target_z,
    @target_o,
    @comment
);
-- EOF smart_scripts