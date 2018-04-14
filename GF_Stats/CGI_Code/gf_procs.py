#!e:/Python36/python.exe
import sys
import datetime
import pyodbc
import time

cnx = pyodbc.connect("DSN=geek")
cursor = cnx.cursor()



def get_data(field, tier, run_date):
    query = """
        select killerId as playerId, playerDisplayName, (sum(tot.kills)/sum(tot.deaths)) as KTD, t.playerTier, t.playerGroup, t.playerRealName from (
        SELECT killerId, 0 as deaths, count(*) as kills
        FROM hlstatsx.hlstats_events_frags a, hlstatsx.player_tiers b
        WHERE a.victimId = b.playerId and a.eventTime > '{2}'
        group by killerId
        UNION
        Select victimId, count(*) as deaths, 0 as kills
        FROM hlstatsx.hlstats_events_frags a, hlstatsx.player_tiers b
        WHERE a.killerId = b.playerId and a.eventTime > '{2}'
        group by victimId) tot, hlstatsx.player_tiers t
        where tot.killerId = t.playerId 
        and {0} = {1}
        group by killerId
        order by KTD desc;
    """
   
    player_table = cursor.execute(query.format(field, tier, run_date))
    tier_stats = list(player_table)
    return(tier_stats)

def maps_list(run_date):
    query_map = "select distinct map from hlstatsx.hlstats_events_frags where eventTime > {0}"
    return(cursor.execute(query_map.format(run_date)))

def get_map_rank(run_date,d_map):
    query = """
        select map, killerId as playerId, playerDisplayName, (sum(tot.kills)/sum(tot.deaths)) as KTD, t.playerTier, t.playerGroup from (
        SELECT map, killerId, 0 as deaths, count(*) as kills FROM 
        (select * from hlstatsx.hlstats_events_frags a where eventTime > '{0}') as aa
        group by killerId, map
        UNION
        Select map, victimId, count(*) as deaths, 0 as kills FROM 
        (select * from hlstatsx.hlstats_events_frags b where eventTime > '{0}') as bb
        group by victimId, map
        ) tot, hlstatsx.player_tiers t
        where tot.killerId = t.playerId
        and map = '{1}'
        group by playerId, map, playerDisplayName
        order by map, KTD desc;
    """
    return(cursor.execute(query.format(run_date,d_map)))

def set_header(active):
    class1 = class2 = class3 = class4 = class5 = ''
    if active == 1:
        class1 = 'active'
    elif active == 2:
        class2 = 'active'
    elif active == 3:
        class3 = 'active'
    elif active == 4:
        class4 = 'active'
    elif active == 5:
        class5 = 'active'

    print("Content-Type: text/html\n\n")  # html markup follows
    print("""
        <style>
        
        table {
               border-collapse: collapse;
               --float: left;
        }

        table, th, td {
               border: 1px solid grey;
               padding: 5px;
        }
        
        p {
          text-align: center;
          font-size: 150%;
          font-weight: bold;
          color: red;
          margin-top:0px;
        }
        ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #333;

            width: 100%;
        }

        li {
            float: left;
            border-right: 1px solid #bbb;
        }

        li a {
            display: block;
            color: white;
            text-align: center;
            padding: 8px 26px;
            text-decoration: none;
        }

        li a:hover {
            background-color: #111;
        }

        .active {
            background-color: #4CAF50;
        }

        .awesome {
      
          width:100%;
          margin: 0 auto;
          text-align: center;
          color:#313131;
          font-size:125px;
          font-weight: bold;
          -webkit-animation:colorchange 20s infinite alternate;
        }

        @-webkit-keyframes colorchange {
        0% {
        
        color: blue;
      }
      
      10% {
        
        color: #8e44ad;
      }
      
      20% {
        
        color: #1abc9c;
      }
      
      30% {
        
        color: #d35400;
      }
      
      40% {
        
        color: blue;
      }
      
      50% {
        
        color: #34495e;
      }
      
      60% {
        
        color: blue;
      }
      
      70% {
        
        color: #2980b9;
      }
      80% {
     
        color: #f1c40f;
      }
      
      90% {
     
        color: #2980b9;
      }
      
      100% {
        
        color: pink;
      }
    }
        </style>
        <meta http-equiv="refresh" content="30" >
    """)

    print("""
        <html>
          <Title>Geekfest Generations</Title>
          <body id="bkd">
          <div style="text-align: center;"><img src="/gf_gen_header.gif"
                alt="GeekFest Generations" title="Geekfest Generations" style="width: 463px; height: 84px; max-width: 90%"><br>
          </div>
    """)
    print('<ul>')
    print('<li><a class="'+class1+'" href="tiers.py">Tiers</a></li>')
    print('<li><a class="'+class2+'" href="gfgen.py">Generations</a></li>')
    print('<li><a class="'+class3+'" href="gfmaprank.py">Maps</a></li>')
    print('<li><a class="'+class4+'" href="awards.py">Awards</a></li>')
    print('<li><a class="'+class5+'" href="geeks.py">Geek Info</a></li>')
    print('<li style="float:right"><a href="/hlstats.php?mode=players&game=csgo">HLStatsX (full)</a></li>')
    print('</ul>')


def set_footer():
    htmlFooter = """
        </body>
        </html>
    """
    print(htmlFooter)
