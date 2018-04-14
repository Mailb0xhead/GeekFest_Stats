#!e:/Python36/python.exe
import sys
import datetime
import pyodbc
import logging
import gf_procs

logging.basicConfig(filename='gf.log',level=logging.INFO, format='%(asctime)s %(message)s')

cnx = pyodbc.connect("DSN=geek")
cursor = cnx.cursor()

def award(query, run_date, whereclause):
   
   if whereclause == 'none':
      award_list = list(cursor.execute(query.format(run_date)))
   else:
      award_list = list(cursor.execute(query.format(run_date, whereclause)))
##   try:
##      top = award_list[0]
##   except:
##      top = 'none'
  
   return award_list

def table_row(img, title, awd, desc):
   print('<div class="tile2 metal">')
   line1 = '<div class="graphic"><center><img src="{0}"><BR><Font size=-2><B>{1}</B></FONT></div><div class="award azul">'
   line2 = '<B>{0}</B><BR>'
   line3 = '<font size=-2>{0} {1}</font></div></div>'
   print(line1.format(img, title))
   try:
      prev_val = awd[0].events
      for row in awd:
         if (row.events == prev_val):
            print(line2.format(row.player,row.events))
            prev_val = row.events
      print(line3.format(awd[0].events,desc))
   except:
      print(line2.format('none'))

def table_row2(img, title, awd, desc):
   line1 = '<TR><td align=center><img src="{0}"><BR><Font size=-2><B>{1}</B></FONT></TD><td>'
   line2 = '<B>{0}</B><BR>'
   line3 = '<font size=-2>{0} {1}</font></td></TR>'
   print(line1.format(img, title))
   try:
      prev_val = awd[0].events
      for row in awd:
         if (row.events == prev_val):
            try:
               print(line2.format(row.player,row.events))
            except:
               print(line2.format('none'))
            prev_val = row.events
      print(line3.format(awd[0].events,desc))
   except:
      print(line2.format('none'))
      
      
   

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

   .pagina{
      width:auto;
      height:auto;
   }
   .linha{
      width:90%;
      padding:5px;
      height:auto;
      display:table;
      align: center;
      font-size:x-large;
      font-variant:small-caps;
      
   }
   .tile{
      position: relative;
      height:100px;
      width:32.5%;
      float:left;
      margin:0 5px 0 0;
      padding:2px;
      background-image: url("metal_bkg.jpg");
   }
    .tile2{
      height:70px;
      width:250px;
      float:left;
      margin:0 5px 0 0;
      padding:2px;
      background-image: url("metal_bkg.jpg");
   }
   .graphic{
      height:70px;
      width:70px;
      float:left;
      margin:0 2px 0 0;
      padding:2px;
   }

   .award{
      float:left;
      text-align: left;
   }
   

   .metal{
      background-image: url("/lt_metal.jpg");
   }
   .rough{
   background-image: url("/metal_bkg.jpg");
   }

   .gold{
      background-image: url("/gold2.jpg");
   }

   
   .tileLargo{
      width:210px;
   }
   .azul{
      background:#4682B4;
   }
   .verde{
      background-color: #2E8B57;
   }

   .negro{
      background-color: #000000;
   }
   </style>
            """

htmlFormat = """
    <center></br>

    </center>
    """
a_img = {'generic':'/hlstatsimg/games/csgo/dawards/w_ak47.png',
         'kill_streak':'/hlstatsimg/games/csgo/dawards/w_ak47.png',
         'red_shirt':'/hlstatsimg/games/csgo/dawards/o_headshot.png',
         'head_shot':'/hlstatsimg/games/csgo/dawards/o_headshot.png'}

gf_procs.set_header(4)
print(pageStyle)
run_date = '2018-01-24'
color = ['rgb(225, 180, 90)','rgb(204, 204, 204)','rgb(170, 136, 68)']
print('<center><DIV class="pagina">')
print('<br>')
print('<div class="linha gold"><B>GeekFest Champions</b></DIV>')
print('<div class="linha negro">')
print('<div class="tile metal">')
print('<div>GRAPHIC</div>')
print('<div>GEN X WINNER</div>')
print('</div>')
print('<div class="tile metal">')
print('<div>GRAPHIC</div>')
print('<div>GEN Y WINNER</div>')
print('</div>')
print('<div class="tile metal">')
print('<div>GRAPHIC</div>')
print('<div>GEN Z WINNER</div>')
print('</div>')
print('</div>')
print('<center><DIV class="pagina">')
print('<div class="linha gold">')
table_row(a_img['kill_streak'],'KILL STREAK',award(q_killstreak, run_date, """b.code like 'kill_streak%'"""),'')
table_row(a_img['red_shirt'],'RED SHIRT',award(q_redshirt, run_date, 'none'),' Total Deaths')
table_row(a_img['generic'],'SILENCED',award(q_skiller, run_date, """weapon in ('usp_silencer','m4a1_silencer')"""),' Total kills with silencer')
table_row(a_img['head_shot'],'HEAD HUNTER',award(q_headhunter, run_date, 'headshot = 1'),' Total Headshots')
table_row(a_img['head_shot'],'MAILBOXHEAD',award(q_mbh, run_date, 'headshot = 1'),' Shots to the head')
print('</div>')
print('<table style="font-size: large; float:left;font-family: Arial,Helvetica,sans-serif;"><tbody>')
table_row2(a_img['kill_streak'],'GRENADIER',award(q_skiller, run_date, """weapon = 'hegrenade'"""),' Grenade kills')
table_row2(a_img['kill_streak'],'KNIFER',award(q_skiller, run_date, """weapon in ('knife_t','knife_default_ct')"""),' Knife kills')
table_row2(a_img['head_shot'],'I WANNA BE A COWBOY',award(q_skiller, run_date, """weapon = 'elite'"""),' Total dualie kills')
table_row2(a_img['kill_streak'],'THE TERMINATOR',award(q_skiller, run_date, """weapon in('nova','xm1014','mag7','sawedoff')"""),' Shotgun Kills')
table_row2(a_img['kill_streak'],'EAGLE EYE',award(q_skiller, run_date, """weapon = 'ssg08'"""),' Snipes')
print('</tr></table>')

print('<table style="font-size: large; float:left;font-family: Arial,Helvetica,sans-serif;"><tbody>')
table_row2(a_img['kill_streak'],'PEA SHOOTER',award(q_skiller, run_date, """weapon in('p2000','usp','usp_silencer','glock','p250','fiveseven','elite','deagle','revolver')"""),' Pistol kills')
table_row2(a_img['kill_streak'],'HAND CANNON',award(q_skiller, run_date, """weapon = 'deagle'"""),' Desert Eagle blasts')
table_row2(a_img['head_shot'],'BIG GUNS',award(q_skiller, run_date, """weapon in('m249','negev')"""),' HMG Mow Downs')
table_row2(a_img['kill_streak'],'PYROMANIAC',award(q_skiller, run_date, """weapon = 'inferno'"""),' Players burnt to ashes')
table_row2(a_img['kill_streak'],'ZAPPY',award(q_skiller, run_date, """weapon = 'taser'"""),' Tazer kills')
print('</tr></table>')

print('<table style="font-size: large; float:left;font-family: Arial,Helvetica,sans-serif;"><tbody>')
table_row2(a_img['kill_streak'],'ARMS DEALER',award(q_arms, run_date, """a.killerId = b.playerId"""),' Weapons used to kill')
table_row2(a_img['kill_streak'],'TARGET PRACTICE',award(q_arms, run_date, """a.victimId = b.playerId"""),' Weapons killed by')
table_row2(a_img['head_shot'],'WESLEY CRUSHER',award(q_tk, run_date, """a.victimId = b.playerId"""),' deaths by a team member')
table_row2(a_img['kill_streak'],'n00b',award(q_tk, run_date, """a.killerId = b.playerId"""),' Team kills')
table_row2(a_img['kill_streak'],'SABATEUR',award(q_action, run_date, """b.code like 'Planted_The_Bomb%' """),' Bomb Plants')
print('</tr></table>')

print('<table style="font-size: large; float:left;font-family: Arial,Helvetica,sans-serif;"><tbody>')
table_row2(a_img['kill_streak'],'RESCUE HERO',award(q_action, run_date, """b.code like 'Rescued_A_Hostage%'"""),' Hostages Rescued')
table_row2(a_img['kill_streak'],'SAVIOR',award(q_action, run_date, """b.code like 'Defused_The_Bomb%'"""),' Bombs Defused')
table_row2(a_img['kill_streak'],'HERO WANNABE',award(q_action, run_date, """b.code like 'Touched_A_Hostage%'"""),' Attempts to rescue')
table_row2(a_img['kill_streak'],'FAILED TO DELIVER',award(q_action, run_date, """b.code like 'Dropped_The_Bomb%'"""),' Failed bomb carries')
table_row2(a_img['kill_streak'],'NOT A BOYSCOUT',award(q_action, run_date, """b.code like 'Begin_Bomb_Defuse_With_Kit%'"""),' No kit defusals')


print('</tr></table>')
 
gf_procs.set_footer()
