
-- START quest_template
SET
@id := {id},
@questtype := {questtype},
@questlevel := {questlevel},
@minlevel := {minlevel},
@questsortid := {questsortid},
@questinfoid := {questinfoid},
@suggestedgroupnum := {suggestedgroupnum},
@requiredfactionid1 := {requiredfactionid1},
@requiredfactionid2 := {requiredfactionid2},
@requiredfactionvalue1 := {requiredfactionvalue1},
@requiredfactionvalue2 := {requiredfactionvalue2},
@rewardnextquest := {rewardnextquest},
@rewardxpdifficulty := {rewardxpdifficulty},
@rewardmoney := {rewardmoney},
@rewardmoneydifficulty := {rewardmoneydifficulty},
@rewardbonusmoney := {rewardbonusmoney},
@rewarddisplayspell := {rewarddisplayspell},
@rewardspell := {rewardspell},
@rewardhonor := {rewardhonor},
@rewardkillhonor := {rewardkillhonor},
@startitem := {startitem},
@flags := {flags},
@requiredplayerkills := {requiredplayerkills},
@rewarditem1 := {rewarditem1},
@rewardamount1 := {rewardamount1},
@rewarditem2 := {rewarditem2},
@rewardamount2 := {rewardamount2},
@rewarditem3 := {rewarditem3},
@rewardamount3 := {rewardamount3},
@rewarditem4 := {rewarditem4},
@rewardamount4 := {rewardamount4},
@itemdrop1 := {itemdrop1},
@itemdropquantity1 := {itemdropquantity1},
@itemdrop2 := {itemdrop2},
@itemdropquantity2 := {itemdropquantity2},
@itemdrop3 := {itemdrop3},
@itemdropquantity3 := {itemdropquantity3},
@itemdrop4 := {itemdrop4},
@itemdropquantity4 := {itemdropquantity4},
@rewardchoiceitemid1 := {rewardchoiceitemid1},
@rewardchoiceitemquantity1 := {rewardchoiceitemquantity1},
@rewardchoiceitemid2 := {rewardchoiceitemid2},
@rewardchoiceitemquantity2 := {rewardchoiceitemquantity2},
@rewardchoiceitemid3 := {rewardchoiceitemid3},
@rewardchoiceitemquantity3 := {rewardchoiceitemquantity3},
@rewardchoiceitemid4 := {rewardchoiceitemid4},
@rewardchoiceitemquantity4 := {rewardchoiceitemquantity4},
@rewardchoiceitemid5 := {rewardchoiceitemid5},
@rewardchoiceitemquantity5 := {rewardchoiceitemquantity5},
@rewardchoiceitemid6 := {rewardchoiceitemid6},
@rewardchoiceitemquantity6 := {rewardchoiceitemquantity6},
@poicontinent := {poicontinent},
@poix := {poix},
@poiy := {poiy},
@poipriority := {poipriority},
@rewardtitle := {rewardtitle},
@rewardtalents := {rewardtalents},
@rewardarenapoints := {rewardarenapoints},
@rewardfactionid1 := {rewardfactionid1},
@rewardfactionvalue1 := {rewardfactionvalue1},
@rewardfactionoverride1 := {rewardfactionoverride1},
@rewardfactionid2 := {rewardfactionid2},
@rewardfactionvalue2 := {rewardfactionvalue2},
@rewardfactionoverride2 := {rewardfactionoverride2},
@rewardfactionid3 := {rewardfactionid3},
@rewardfactionvalue3 := {rewardfactionvalue3},
@rewardfactionoverride3 := {rewardfactionoverride3},
@rewardfactionid4 := {rewardfactionid4},
@rewardfactionvalue4 := {rewardfactionvalue4},
@rewardfactionoverride4 := {rewardfactionoverride4},
@rewardfactionid5 := {rewardfactionid5},
@rewardfactionvalue5 := {rewardfactionvalue5},
@rewardfactionoverride5 := {rewardfactionoverride5},
@timeallowed := {timeallowed},
@allowableraces := {allowableraces},
@logtitle := '{logtitle}',
@logdescription := '{logdescription}',
@questdescription := '{questdescription}',
@areadescription := '{areadescription}',
@questcompletionlog := '{questcompletionlog}',
@requirednpcorgo1 := {requirednpcorgo1},
@requirednpcorgo2 := {requirednpcorgo2},
@requirednpcorgo3 := {requirednpcorgo3},
@requirednpcorgo4 := {requirednpcorgo4},
@requirednpcorgocount1 := {requirednpcorgocount1},
@requirednpcorgocount2 := {requirednpcorgocount2},
@requirednpcorgocount3 := {requirednpcorgocount3},
@requirednpcorgocount4 := {requirednpcorgocount4},
@requireditemid1 := {requireditemid1},
@requireditemid2 := {requireditemid2},
@requireditemid3 := {requireditemid3},
@requireditemid4 := {requireditemid4},
@requireditemid5 := {requireditemid5},
@requireditemid6 := {requireditemid6},
@requireditemcount1 := {requireditemcount1},
@requireditemcount2 := {requireditemcount2},
@requireditemcount3 := {requireditemcount3},
@requireditemcount4 := {requireditemcount4},
@requireditemcount5 := {requireditemcount5},
@requireditemcount6 := {requireditemcount6},
@unknown0 := {unknown0},
@objectivetext1 := '{objectivetext1}',
@objectivetext2 := '{objectivetext2}',
@objectivetext3 := '{objectivetext3}',
@objectivetext4 := '{objectivetext4}',
@verifiedbuild := {verifiedbuild};

DELETE FROM quest_template WHERE
    id=@id
;

INSERT INTO quest_template (
    id,
    questtype,
    questlevel,
    minlevel,
    questsortid,
    questinfoid,
    suggestedgroupnum,
    requiredfactionid1,
    requiredfactionid2,
    requiredfactionvalue1,
    requiredfactionvalue2,
    rewardnextquest,
    rewardxpdifficulty,
    rewardmoney,
    rewardmoneydifficulty,
    rewardbonusmoney,
    rewarddisplayspell,
    rewardspell,
    rewardhonor,
    rewardkillhonor,
    startitem,
    flags,
    requiredplayerkills,
    rewarditem1,
    rewardamount1,
    rewarditem2,
    rewardamount2,
    rewarditem3,
    rewardamount3,
    rewarditem4,
    rewardamount4,
    itemdrop1,
    itemdropquantity1,
    itemdrop2,
    itemdropquantity2,
    itemdrop3,
    itemdropquantity3,
    itemdrop4,
    itemdropquantity4,
    rewardchoiceitemid1,
    rewardchoiceitemquantity1,
    rewardchoiceitemid2,
    rewardchoiceitemquantity2,
    rewardchoiceitemid3,
    rewardchoiceitemquantity3,
    rewardchoiceitemid4,
    rewardchoiceitemquantity4,
    rewardchoiceitemid5,
    rewardchoiceitemquantity5,
    rewardchoiceitemid6,
    rewardchoiceitemquantity6,
    poicontinent,
    poix,
    poiy,
    poipriority,
    rewardtitle,
    rewardtalents,
    rewardarenapoints,
    rewardfactionid1,
    rewardfactionvalue1,
    rewardfactionoverride1,
    rewardfactionid2,
    rewardfactionvalue2,
    rewardfactionoverride2,
    rewardfactionid3,
    rewardfactionvalue3,
    rewardfactionoverride3,
    rewardfactionid4,
    rewardfactionvalue4,
    rewardfactionoverride4,
    rewardfactionid5,
    rewardfactionvalue5,
    rewardfactionoverride5,
    timeallowed,
    allowableraces,
    logtitle,
    logdescription,
    questdescription,
    areadescription,
    questcompletionlog,
    requirednpcorgo1,
    requirednpcorgo2,
    requirednpcorgo3,
    requirednpcorgo4,
    requirednpcorgocount1,
    requirednpcorgocount2,
    requirednpcorgocount3,
    requirednpcorgocount4,
    requireditemid1,
    requireditemid2,
    requireditemid3,
    requireditemid4,
    requireditemid5,
    requireditemid6,
    requireditemcount1,
    requireditemcount2,
    requireditemcount3,
    requireditemcount4,
    requireditemcount5,
    requireditemcount6,
    unknown0,
    objectivetext1,
    objectivetext2,
    objectivetext3,
    objectivetext4,
    verifiedbuild
)
VALUES (
    @id,
    @questtype,
    @questlevel,
    @minlevel,
    @questsortid,
    @questinfoid,
    @suggestedgroupnum,
    @requiredfactionid1,
    @requiredfactionid2,
    @requiredfactionvalue1,
    @requiredfactionvalue2,
    @rewardnextquest,
    @rewardxpdifficulty,
    @rewardmoney,
    @rewardmoneydifficulty,
    @rewardbonusmoney,
    @rewarddisplayspell,
    @rewardspell,
    @rewardhonor,
    @rewardkillhonor,
    @startitem,
    @flags,
    @requiredplayerkills,
    @rewarditem1,
    @rewardamount1,
    @rewarditem2,
    @rewardamount2,
    @rewarditem3,
    @rewardamount3,
    @rewarditem4,
    @rewardamount4,
    @itemdrop1,
    @itemdropquantity1,
    @itemdrop2,
    @itemdropquantity2,
    @itemdrop3,
    @itemdropquantity3,
    @itemdrop4,
    @itemdropquantity4,
    @rewardchoiceitemid1,
    @rewardchoiceitemquantity1,
    @rewardchoiceitemid2,
    @rewardchoiceitemquantity2,
    @rewardchoiceitemid3,
    @rewardchoiceitemquantity3,
    @rewardchoiceitemid4,
    @rewardchoiceitemquantity4,
    @rewardchoiceitemid5,
    @rewardchoiceitemquantity5,
    @rewardchoiceitemid6,
    @rewardchoiceitemquantity6,
    @poicontinent,
    @poix,
    @poiy,
    @poipriority,
    @rewardtitle,
    @rewardtalents,
    @rewardarenapoints,
    @rewardfactionid1,
    @rewardfactionvalue1,
    @rewardfactionoverride1,
    @rewardfactionid2,
    @rewardfactionvalue2,
    @rewardfactionoverride2,
    @rewardfactionid3,
    @rewardfactionvalue3,
    @rewardfactionoverride3,
    @rewardfactionid4,
    @rewardfactionvalue4,
    @rewardfactionoverride4,
    @rewardfactionid5,
    @rewardfactionvalue5,
    @rewardfactionoverride5,
    @timeallowed,
    @allowableraces,
    @logtitle,
    @logdescription,
    @questdescription,
    @areadescription,
    @questcompletionlog,
    @requirednpcorgo1,
    @requirednpcorgo2,
    @requirednpcorgo3,
    @requirednpcorgo4,
    @requirednpcorgocount1,
    @requirednpcorgocount2,
    @requirednpcorgocount3,
    @requirednpcorgocount4,
    @requireditemid1,
    @requireditemid2,
    @requireditemid3,
    @requireditemid4,
    @requireditemid5,
    @requireditemid6,
    @requireditemcount1,
    @requireditemcount2,
    @requireditemcount3,
    @requireditemcount4,
    @requireditemcount5,
    @requireditemcount6,
    @unknown0,
    @objectivetext1,
    @objectivetext2,
    @objectivetext3,
    @objectivetext4,
    @verifiedbuild
);
-- EOF quest_template