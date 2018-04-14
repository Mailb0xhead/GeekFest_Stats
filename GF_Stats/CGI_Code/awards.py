#!e:/Python36/python.exe
import sys
import datetime
import pyodbc
import logging
import gf_procs

logging.basicConfig(filename='gf.log',level=logging.INFO, format='%(asctime)s %(message)s')

cnx = pyodbc.connect("DSN=geek")
cursor = cnx.cursor()
run_date = '2018-02-01'


def award(query, run_date, whereclause):
##   print(query.format(run_date, whereclause))
   
   if whereclause == 'none':
      award_list = list(cursor.execute(query.format(run_date)))
   else:
      award_list = list(cursor.execute(query.format(run_date, whereclause)))
##   try:
##      top = award_list[0]
##   except:
##      top = 'none'
##   print(query.format(run_date, whereclause))
   return award_list

def table_row(img, title, player, description):
   line1 = '<TR><td align=center><img src="{0}"><BR><Font size=-2><B>{1}</B></FONT></TD>'
   line2 = '<td><B>{0}</B> <BR><font size=-2>{1}</font></td></TR>'
   print(line1.format(img, title))
   print(line2.format(player,description))

def table_row2(img, title, awd, desc):
   line1 = '<TR><td align=center width="100"><img src="{0}"><BR><Font size=-2><B>{1}</B></FONT></TD><td width="100">'
   line2 = '<B><div class="flip-container"><center><div class="flipper"><div class="frontsm">{0}</B><BR>'
   line3 = '<font size=-2>{0} {1}</font></div><div class="backsm"><font size="1">{2}</font></div></div></div></td></TR>'
   win_count = 0
   print(line1.format(img, title))
   try:
      x1test = awd[0].events
   except:
      print(line2.format('none'))
      return
   try:
      x2test = awd[1].events
      if awd[0].events == awd[1].events:
         print(line2.format('TIE',awd[0].events))
      else:
         print(line2.format(awd[0].player,awd[0].events))
      pList = ''
      for i in range (0,5):
         try:
            pList+=(awd[i].player+'  ['+awd[i].events[-8:-1]+']<br>')
         except:
            try:
               pList+= (awd[i].player+'  ['+str(round(awd[i].events,2))+']<br>')
            except:
               continue
      print(line3.format(awd[0].events,desc,pList))
   except:
      print(line2.format(awd[0].player,awd[0].events))
      print(line3.format(awd[0].events,desc,''))
      
      
   

q_killstreak = """SELECT c.playerDisplayName as player, description as events, reward_player 
            FROM hlstatsx.hlstats_events_playeractions a, hlstatsx.hlstats_actions b, player_tiers c 
            where a.actionId = b.id
            and a.playerId = c.playerId
            and eventTime > '{0}'
            and {1}
            group by c.playerId, c.playerDisplayName, b.description
            order by reward_player desc;
    """

q_redshirt = """select count(*) as events, victimId, b.playerDisplayName as player
            from hlstatsx.hlstats_events_frags a, player_tiers b 
            where eventTime > {0} 
            and a.victimId = b.playerId
            group by victimId, playerDisplayName order by events desc;
    """

q_skiller = """select killerId, b.playerDisplayName as player, count(*) as events
            from hlstatsx.hlstats_events_frags a, player_tiers b
            where {1} and a.killerId = b.playerId and a.eventTime > '{0}'
            group by killerId, b.playerDisplayName
            order by events desc;
    """

q_headhunter = """select killerId, b.playerDisplayName as player, count(*) as events 
            from hlstatsx.hlstats_events_frags a, player_tiers b
            where {1} and eventTime > '{0}' and a.killerId = b.playerId
            group by killerId
            order by events desc ; 
     """

q_mbh = """select victimId, b.playerDisplayName as player, count(*) as events
            from hlstatsx.hlstats_events_frags a, player_tiers b
            where {1} and eventTime > '{0}' and a.victimId = b.playerId
            group by victimId, playerDisplayName 
            order by events desc;
    """

q_arms = """select count(*) as events, u.playerDisplayName as player
            from (select distinct weapon, b.playerDisplayName
            from hlstatsx.hlstats_events_frags a, hlstatsx.player_tiers b
            where {1} and a.eventTime > '{0}'
            ) u
            group by u.playerDisplayName
            order by events desc;
      """
q_tk = """SELECT count(*) as events, playerDisplayName as player
            FROM hlstatsx.hlstats_events_teamkills a, player_tiers b
            where {1} and eventTime > '{0}'
            group by playerDisplayName order by events desc;
      """

q_action = """SELECT c.playerDisplayName as player, count(*) as events
            FROM hlstatsx.hlstats_events_playeractions a, hlstatsx.hlstats_actions b, player_tiers c 
            where a.actionId = b.id and a.playerId = c.playerId
            and {1} and eventTime > '{0}'
            group by c.playerDisplayName
            order by events desc;
            """

pageStyle = """
   <style>


   .center {
     margin: auto;
     position: relative;
     text-align: center;
     width: 80%;
   }
   table {
  border-collapse: collapse;
  border: 1px solid gray;
   float: left;
  margin: 3px;
}
   .gray {
        background-color:#EEEEEE;
        }
        
  tr:hover {
     background-color: #f5f5f5;
   }

   .flip-container {
	perspective: 100%;
}
	/* flip the pane when hovered */
	.flip-container:hover .flipper, .flip-container.hover .flipper {
		transform: rotateY(180deg);
	}

.flip-container, .front, .back {
	width: 100%;
	height: 25%;

}

/* flip speed goes here */
.flipper {
	transition: 0.6s;
	transform-style: preserve-3d;
	position: relative;
}

/* hide back of pane during swap */
.front, .back {
	backface-visibility: hidden;
      
	position: absolute;
	top: -50;
	left: 10;
}
.backsm, .frontsm {
	backface-visibility: hidden;
	width: 100px;
        word-wrap: break-word;
	position: absolute;
	top: -25;
	left: 0;
}


/* front pane, placed above back */
.front {
	z-index: 2;
	/* for firefox 31 */
	transform: rotateY(0deg);
	word-wrap: break-word;
}

/* back, initially hidden pane */
.back, .backsm {
	transform: rotateY(180deg);
}

   </style>
            """

htmlFormat = """
    <center></br>

    </center>
    """
a_img = {'generic':'/hlstatsimg/games/csgo/ribbons/1_silenced.png',
         'kill_streak':'/hlstatsimg/games/csgo/ribbons/4_mostkills.png',
         'red_shirt':'/hlstatsimg/games/csgo/ribbons/6_redshirt.png',
         'shot_head':'/hlstatsimg/games/csgo/ribbons/6_headshot.png',
         'grenade':'/hlstatsimg/games/csgo/ribbons/4_hegrenade.png',
         'knife':'/hlstatsimg/games/csgo/ribbons/4_knife.png',
         'dualies':'/hlstatsimg/games/csgo/ribbons/2_elite.png',
         'shotgun':'/hlstatsimg/games/csgo/ribbons/2_sawedoff.png',
         'sniper':'/hlstatsimg/games/csgo/ribbons/1_ssg08.png',
         'pistol':'/hlstatsimg/games/csgo/ribbons/1_glock.png',
         'deagle':'/hlstatsimg/games/csgo/ribbons/1_deagle.png',
         'pyro':'/hlstatsimg/games/csgo/ribbons/2_firebomb.png',
         'hmg':'/hlstatsimg/games/csgo/ribbons/2_negev.png',
         'tazer':'/hlstatsimg/games/csgo/ribbons/2_taser.png',
         'arms':'/hlstatsimg/games/csgo/ribbons/4_arms_dealer.png',
         'target':'/hlstatsimg/games/csgo/ribbons/6_target.png',
         'wesley':'/hlstatsimg/games/csgo/ribbons/1_teamkilled.png',
         'n00b':'/hlstatsimg/games/csgo/ribbons/6_suicide.png',
         'bombs':'/hlstatsimg/games/csgo/ribbons/3_planted_the_bomb.png',
         'hero':'/hlstatsimg/games/csgo/ribbons/3_rescued_a_hostage.png',
         'defuse':'/hlstatsimg/games/csgo/ribbons/3_defused_the_bomb.png',
         'nohero':'/hlstatsimg/games/csgo/ribbons/3_rescued_a_hostage.png',
         'nodeliver':'/hlstatsimg/games/csgo/ribbons/6_planted_the_bomb.png',
         'noscout':'/hlstatsimg/games/csgo/ribbons/3_defused_the_bomb.png',

         'head_shot':'/hlstatsimg/games/csgo/ribbons/4_headshot.png'}
gf_procs.set_header(4)
x_win = gf_procs.get_data('playerGroup',1, run_date)
y_win = gf_procs.get_data('playerGroup',2, run_date)
z_win = gf_procs.get_data('playerGroup',3, run_date)
print(pageStyle)

color = ['rgb(225, 180, 90)','rgb(204, 204, 204)','rgb(170, 136, 68)']
print('<center>')
print('<BR><div class="awesome" style="text-align: center; font-size: x-large; font-weight: bold;">GEEKFEST CHAMPIONS</DIV>')
print('<br><table style="width: 90%; font-family: Arial,Helvetica,sans-serif; margin-left:5%; margin-right:5%; font-size: large; text-transform: capitalize;"><tbody><tr>')
print('<td width="100px"><img src="/genxguy.jpg" height="100" width="100"></TD>')
print('<td style="font-size: x-large;">')
print('<div class="flip-container"><center><div class="flipper">')
print('<div class="front">GEN X')
try:
   print('<BR><font size = "6">'+x_win[0].playerDisplayName)
   print('<BR><font size = "3">'+x_win[0].playerRealName+'</DIV>')
except:
   print('<BR>NONE</div>')
print('<div class="back">')
for i in range (0,5):
   try:
      print(x_win[i].playerDisplayName+'  ['+str(round(x_win[i].KTD,2))+']<br>')
   except:
      continue
print('</DIV></DIV></DIV></TD>')
print('<td  width="100px"><img src="/genyguy.jpg" height="100" width="100"></TD>')
print('<td style="font-size: x-large;">')
print('<div class="flip-container"><center><div class="flipper">')
print('<div class="front">GEN Y')
try:
   print('<BR><font size = "6">'+y_win[0].playerDisplayName)
   print('<BR><font size = "3">'+y_win[0].playerRealName+'</DIV>')
except:
   print('<BR>NONE</div>')
print('<div class="back">')
for i in range (0,5):
   try:
      print(y_win[i].playerDisplayName+'  ['+str(round(y_win[i].KTD,2))+']<br>')
   except:
      continue
print('</DIV></DIV></DIV></TD>')
print('<td width="100px"><img src="/genzguy.jpg" height="100" width="100"></TD>')
print('<td style="font-size: x-large;">')
print('<div class="flip-container"><center><div class="flipper">')
print('<div class="front">GEN Z')
try:
   print('<BR><font size = "6">'+z_win[0].playerDisplayName)
   print('<BR><font size = "3">'+z_win[0].playerRealName+'</DIV>')
except:
   print('<BR>NONE</div>')
print('<div class="back">')
for i in range (0,5):
   try:
      print(z_win[i].playerDisplayName+'  ['+str(round(z_win[i].KTD,2))+']<br>')
   except:
      continue
print('</DIV></DIV></DIV></TD>')
print('</tr></table></DIV>')

print('<div style="width: 98%; margin-left: 1%; margin-right: 1%">')
print('<br><table class="gray" style="font-size: large; float:left;font-family: Arial,Helvetica,sans-serif; clear:left;"><tbody>')
print('<tr><td colspan=2 style="background-color: #BBBBBB; text-align:center;">Warrior Class</td></tr>')
table_row2(a_img['kill_streak'],'KILL STREAK',award(q_killstreak, run_date, """b.code like 'kill_streak%'"""),'')
table_row2(a_img['knife'],'KNIFER',award(q_skiller, run_date, """weapon in ('knife_t','knife_default_ct')"""),' Knife kills')
table_row2(a_img['arms'],'ARMS DEALER',award(q_arms, run_date, """a.killerId = b.playerId"""),' Weapons used to kill')
table_row2(a_img['grenade'],'GRENADIER',award(q_skiller, run_date, """weapon = 'hegrenade'"""),' Grenade kills')
table_row2(a_img['head_shot'],'HEAD HUNTER',award(q_headhunter, run_date, 'headshot = 1'),' Total Headshots')
print('</tr></table>')

print('<table class="gray" style="font-size: large; float:left;font-family: Arial,Helvetica,sans-serif;"><tbody>')
print('<tr><td colspan=2 style="background-color: #BBBBBB; text-align:center;">Assassin Class</td></tr>')
table_row2(a_img['generic'],'SILENCED',award(q_skiller, run_date, """weapon in ('usp_silencer','m4a1_silencer')"""),' Total kills with silencer')
table_row2(a_img['sniper'],'EAGLE EYE',award(q_skiller, run_date, """weapon = 'ssg08'"""),' Snipes')
table_row2(a_img['wesley'],'MISTAKEN IDENTITY',award(q_tk, run_date, """a.victimId = b.playerId"""),' deaths by a team member')
table_row2(a_img['pistol'],'PEA SHOOTER',award(q_skiller, run_date, """weapon in('p2000','usp','usp_silencer','glock','p250','fiveseven','elite','deagle','revolver')"""),' Pistol kills')
table_row2(a_img['deagle'],'HAND CANNON',award(q_skiller, run_date, """weapon = 'deagle'"""),' Desert Eagle blasts')
print('</tr></table>')

print('<table class="gray" style="font-size: large; float:left;font-family: Arial,Helvetica,sans-serif;"><tbody>')
print('<tr><td colspan=2 style="background-color: #BBBBBB; text-align:center;">Specialist Class</td></tr>')
table_row2(a_img['shotgun'],'THE TERMINATOR',award(q_skiller, run_date, """weapon in('nova','xm1014','mag7','sawedoff')"""),' Shotgun Kills')
table_row2(a_img['hmg'],'BIG GUNS',award(q_skiller, run_date, """weapon in('m249','negev')"""),' LMG Mow Downs')
table_row2(a_img['dualies'],'I WANNA BE A COWBOY',award(q_skiller, run_date, """weapon = 'elite'"""),' Total dualie kills')
table_row2(a_img['pyro'],'PYROMANIAC',award(q_skiller, run_date, """weapon = 'inferno'"""),' Players burnt to ashes')
table_row2(a_img['tazer'],'ZAPPY',award(q_skiller, run_date, """weapon = 'taser'"""),' Tazer kills')
print('</tr></table>')

print('<table class="gray" style="font-size: large; float:left;font-family: Arial,Helvetica,sans-serif;"><tbody>')
print('<tr><td colspan=2 style="background-color: #BBBBBB; text-align:center;">n00b Class</td></tr>')
table_row2(a_img['red_shirt'],'RED SHIRT',award(q_redshirt, run_date, 'none'),' Total Deaths')
table_row2(a_img['nodeliver'],'FAILED TO DELIVER',award(q_action, run_date, """b.code like 'Dropped_The_Bomb%'"""),' Failed bomb carries')
table_row2(a_img['shot_head'],'MAILBOXHEAD',award(q_mbh, run_date, 'headshot = 1'),' Shots to the head')
table_row2(a_img['target'],'TARGET PRACTICE',award(q_arms, run_date, """a.victimId = b.playerId"""),' Weapons killed by')
table_row2(a_img['n00b'],'n00b',award(q_tk, run_date, """a.killerId = b.playerId"""),' Team kills')
print('</tr></table>')

print('<table class="gray" style="font-size: large; float:left;font-family: Arial,Helvetica,sans-serif;"><tbody>')
print('<tr><td colspan=2 style="background-color: #BBBBBB; text-align:center;">Hero Class</td></tr>')
table_row2(a_img['bombs'],'SABATEUR',award(q_action, run_date, """b.code like 'Planted_The_Bomb%' """),' Bomb Plants')
table_row2(a_img['hero'],'RESCUE HERO',award(q_action, run_date, """b.code like 'Rescued_A_Hostage%'"""),' Hostages Rescued')
table_row2(a_img['defuse'],'SAVIOR',award(q_action, run_date, """b.code like 'Defused_The_Bomb%'"""),' Bombs Defused')
table_row2(a_img['nohero'],'HERO WANNABE',award(q_action, run_date, """b.code like 'Touched_A_Hostage%'"""),' Attempts to rescue')
table_row2(a_img['noscout'],'NOT A BOYSCOUT',award(q_action, run_date, """b.code like 'Begin_Bomb_Defuse_With_Kit%'"""),' No kit defusals')


print('</tr></table></DIV>')
 
gf_procs.set_footer()
