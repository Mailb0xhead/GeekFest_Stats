SELECT u.playerId, u.uniqueId, p.lastName, p.kills, p.deaths, (p.kills/p.deaths) as ktd 
FROM hlstatsx.hlstats_playeruniqueids u, hlstatsx.hlstats_players p
where u.playerID = p.playerID
order by ktd desc;

insert into hlstatsx.player_tiers (playerId, playerDisplayName) 
select playerId, lastName from hlstatsx.hlstats_players ;