select * from hlstatsx.hlstats_events_frags
where eventTime > '2018-01-24';
select distinct weapon from hlstatsx.hlstats_events_frags
where eventTime > '2018-01-24' order by weapon;

# most kills in a row (use loop to find streaks)
select * from hlstatsx.hlstats_events_frags where killerId = 7 or victimId = 7 order by eventTime;
SELECT c.playerId, c.playerDisplayName, description 
FROM hlstatsx.hlstats_events_playeractions a, hlstatsx.hlstats_actions b, player_tiers c 
where a.actionId = b.id
and a.playerId = c.playerId
and eventTime > '2018-01-24'
and b.code like 'kill_streak%'
group by c.playerId, c.playerDisplayName, b.description
order by code desc;

# Top Red Shirt (most deaths)
select count(*) as deaths, victimId, b.playerDisplayName 
from hlstatsx.hlstats_events_frags a, player_tiers b 
where eventTime > '2018-01-24' 
and a.victimId = b.playerId
group by victimId, playerDisplayName order by deaths desc;

# silent killer (silencer)
select killerId, b.playerDisplayName, count(*) as s_kills
from hlstatsx.hlstats_events_frags a, player_tiers b
where weapon in ('usp_silencer','m4a1_silencer') and a.killerId = b.playerId and a.eventTime > '2018-01-24'
group by killerId, b.playerDisplayName
order by s_kills desc;

# headhunter (most headshots)
select killerId, b.playerDisplayName, count(*) as hs 
from hlstatsx.hlstats_events_frags a, player_tiers b
where headshot = 1 and eventTime > '2018-01-24' and a.killerId = b.playerId
group by killerId
order by hs desc ; 

# Mailboxhead Award (most deaths by headshot)
select victimId, b.playerDisplayName, count(*) as deaths 
from hlstatsx.hlstats_events_frags a, player_tiers b
where headshot = 1 and eventTime > '2018-01-24' and a.victimId = b.playerId
group by victimId, playerDisplayName 
order by deaths desc; 

# grenade killer
select b.playerDisplayName, count(*) as deaths from hlstatsx.hlstats_events_frags a, player_tiers b
where weapon = 'hegrenade' and eventTime > '2018-01-17' group by killerId order by deaths desc; 

# knife killer
select killerId, count(*) as deaths from hlstatsx.hlstats_events_frags where weapon in ('knife_t','knife_default_ct') and eventTime > '2018-01-17' group by killerId order by deaths desc; 

# cowboy killer (dualies)
select killerId, count(*) as deaths from hlstatsx.hlstats_events_frags where weapon = 'elite' and eventTime > '2018-01-17' group by killerId order by deaths desc; 

# Terminator (shotgun)
select killerId, count(*) as deaths from hlstatsx.hlstats_events_frags where weapon in('nova','xm1014','mag7','sawedoff') and eventTime > '2018-01-17' group by killerId order by deaths desc; 

# Eagle eye (sniper)
select killerId, count(*) as deaths from hlstatsx.hlstats_events_frags where weapon = 'ssg08' and eventTime > '2018-01-17' group by killerId order by deaths desc; 

# pistol man (pistols)
select killerId, count(*) as deaths from hlstatsx.hlstats_events_frags where weapon in('p2000','usp','usp_silencer','glock','p250','fiveseven','elite','deagle','revolver') and eventTime > '2018-01-17' group by killerId order by deaths desc; 

# Hand Cannon (deagle)
select killerId, count(*) as deaths from hlstatsx.hlstats_events_frags where weapon = 'deagle' and eventTime > '2018-01-17' group by killerId order by deaths desc; 

# Heavy gunner 
select killerId, count(*) as deaths from hlstatsx.hlstats_events_frags where weapon in('m249','negev') and eventTime > '2018-01-17' group by killerId order by deaths desc; 

# Pyro 
select killerId, count(*) as deaths from hlstatsx.hlstats_events_frags where weapon ='inferno' and eventTime > '2018-01-17' group by killerId order by deaths desc; 


# arms dealer (most weapons used)
select count(*) as events, u.playerDisplayName as player
from (select distinct weapon, b.playerDisplayName
	  from hlstatsx.hlstats_events_frags a, hlstatsx.player_tiers b
      where a.victimId = b.playerId and a.eventTime > '2018-01-24'
	 ) u
group by u.playerDisplayName
order by events desc;

# target practice (killed by most different weapons)
select count(*) as events, victimId from (select distinct weapon, killerId from hlstatsx.hlstats_events_frags) u group by victimId;

# Wesley Crusher Award (most times killed by team from team)
SELECT count(*) as events, playerDisplayName as player
FROM hlstatsx.hlstats_events_teamkills a, player_tiers b
where a.victimId = b.playerId and eventTime > '2018-01-24'
group by playerDisplayName order by deaths desc;

# n00b (team killer)
SELECT count(*) as kills, killerId FROM hlstatsx.hlstats_events_teamkills group by killerId order by kills desc;

# sabateur (bomb plants)
SELECT c.playerDisplayName as player, count(*) as events
FROM hlstatsx.hlstats_events_playeractions a, hlstatsx.hlstats_actions b, player_tiers c 
where a.actionId = b.id and a.playerId = c.playerId
and b.code like 'Planted_The_Bomb%' and eventTime > '2018-01-24'
group by c.playerDisplayName
order by events desc;

# hero (rescues)
SELECT playerId, count(*) code
FROM hlstatsx.hlstats_events_playeractions a, hlstatsx.hlstats_actions b 
where a.actionId = b.id
and b.code like 'Rescued_A_Hostage%'
group by playerId
order by code desc;

# Savior (rescues)
SELECT playerId, count(*) code
FROM hlstatsx.hlstats_events_playeractions a, hlstatsx.hlstats_actions b 
where a.actionId = b.id
and b.code like 'Defused_The_Bomb%'
group by playerId
order by code desc;


# Hero Wannabe (attempted rescues)
SELECT playerId, count(*) code
FROM hlstatsx.hlstats_events_playeractions a, hlstatsx.hlstats_actions b 
where a.actionId = b.id
and b.code like 'Touched_A_Hostage%'
group by playerId
order by code desc;

select killerId, b.playerDisplayName as player, count(*) as events
            from hlstatsx.hlstats_events_frags a, player_tiers b
            where weapon = 'inferno' and a.killerId = b.playerId and a.eventTime > '2018-01-24'
            group by killerId, b.playerDisplayName
            order by events desc;

SELECT c.playerDisplayName as player, description as events, reward_player 
            FROM hlstatsx.hlstats_events_playeractions a, hlstatsx.hlstats_actions b, player_tiers c 
            where a.actionId = b.id
            and a.playerId = c.playerId
            and eventTime > '2018-01-24'
            and b.code like 'kill_streak%'
            group by c.playerId, c.playerDisplayName, b.description
            order by reward_player desc;