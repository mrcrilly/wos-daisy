
-- START scalingstatvalues_dbc
SET
@id := {id},
@charlevel := {charlevel},
@shoulderbudget := {shoulderbudget},
@trinketbudget := {trinketbudget},
@weaponbudget1h := {weaponbudget1h},
@rangedbudget := {rangedbudget},
@clothshoulderarmor := {clothshoulderarmor},
@leathershoulderarmor := {leathershoulderarmor},
@mailshoulderarmor := {mailshoulderarmor},
@plateshoulderarmor := {plateshoulderarmor},
@weapondps1h := {weapondps1h},
@weapondps2h := {weapondps2h},
@spellcasterdps1h := {spellcasterdps1h},
@spellcasterdps2h := {spellcasterdps2h},
@rangeddps := {rangeddps},
@wanddps := {wanddps},
@spellpower := {spellpower},
@primarybudget := {primarybudget},
@tertiarybudget := {tertiarybudget},
@clothcloakarmor := {clothcloakarmor},
@clothchestarmor := {clothchestarmor},
@leatherchestarmor := {leatherchestarmor},
@mailchestarmor := {mailchestarmor},
@platechestarmor := {platechestarmor};

DELETE FROM scalingstatvalues_dbc WHERE
    id=@id
;

INSERT INTO scalingstatvalues_dbc (
    id,
    charlevel,
    shoulderbudget,
    trinketbudget,
    weaponbudget1h,
    rangedbudget,
    clothshoulderarmor,
    leathershoulderarmor,
    mailshoulderarmor,
    plateshoulderarmor,
    weapondps1h,
    weapondps2h,
    spellcasterdps1h,
    spellcasterdps2h,
    rangeddps,
    wanddps,
    spellpower,
    primarybudget,
    tertiarybudget,
    clothcloakarmor,
    clothchestarmor,
    leatherchestarmor,
    mailchestarmor,
    platechestarmor
)
VALUES (
    @id,
    @charlevel,
    @shoulderbudget,
    @trinketbudget,
    @weaponbudget1h,
    @rangedbudget,
    @clothshoulderarmor,
    @leathershoulderarmor,
    @mailshoulderarmor,
    @plateshoulderarmor,
    @weapondps1h,
    @weapondps2h,
    @spellcasterdps1h,
    @spellcasterdps2h,
    @rangeddps,
    @wanddps,
    @spellpower,
    @primarybudget,
    @tertiarybudget,
    @clothcloakarmor,
    @clothchestarmor,
    @leatherchestarmor,
    @mailchestarmor,
    @platechestarmor
);
-- EOF scalingstatvalues_dbc