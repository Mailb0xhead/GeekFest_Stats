Insert into hlstatsx.player_tiers (playerID, playerDisplayName) 
(select p.playerId, p.lastName FROM hlstatsx.hlstats_players p, hlstatsx.hlstats_playeruniqueids u
where p.playerId = u.playerId
and left(uniqueId,3) <> 'BOT'
and p.playerID not in (
select playerId from hlstatsx.player_tiers)
);

