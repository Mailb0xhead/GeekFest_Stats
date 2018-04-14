select map, killerId as playerId, playerDisplayName, (sum(tot.kills)/sum(tot.deaths)) as KTD, t.playerTier, t.playerGroup from (
SELECT map, killerId, 0 as deaths, count(*) as kills FROM hlstatsx.hlstats_events_frags
group by killerId, map
UNION
Select map, victimId, count(*) as deaths, 0 as kills FROM hlstatsx.hlstats_events_frags
group by victimId, map
) tot, hlstatsx.player_tiers t
where tot.killerId = t.playerId
and map = 'de_bank'
#and playerTier = 1
group by playerId, map, playerDisplayName

order by map, KTD desc;