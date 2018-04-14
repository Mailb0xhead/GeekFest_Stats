#!e:/Python36/python.exe
import sys
import datetime
import pyodbc
import logging
import gf_procs

logging.basicConfig(filename='gf.log',level=logging.INFO, format='%(asctime)s %(message)s')

cnx = pyodbc.connect("DSN=geek")
cursor = cnx.cursor()

def get_data(field, tier):
    player_table = cursor.execute(query.format(field, tier))
    tier_stats = list(player_table)
    return(tier_stats)

htmlFormat = """
  <center>
  
  </center>
    """
gf_procs.set_header(3)

tier = ['GenX','GenY','GenZ']
color = ['rgb(225, 180, 90)','rgb(204, 204, 204)','rgb(170, 136, 68)']
bgcolor = ['background-color: rgba(217, 173, 43, 0.37)','rgba(204, 204, 204, 0.37)','rgba(171, 136, 34, 0.37)']
genimg = ['/genx.gif','/geny.gif','/genz.gif']
run_date = '2018-02-16'
c_count = 1
##run_date = datetime.datetime.combine(datetime.date.today(), datetime.time(0,0)) - datetime.timedelta(days = 7)
maps = list(gf_procs.maps_list(run_date))

print('<center><br><table style="width: 80%; font-family: Arial,Helvetica,sans-serif; font-size: large; text-transform: capitalize;"><tbody><tr>')
for row in maps:
    if row.map == '':
        continue
    map_stats = list(gf_procs.get_map_rank(run_date, row.map))
    if map_stats == []:
        continue
    #    print('<td style="vertical-align: top; width: 33%; background-image: url(/genxdef.gif); background-size: cover; background-repeat: no-repeat;"> ')
    print('<td height = "300" style="vertical-align: top; background-image: url(/'+row.map+'.jpg); background-size: cover;"> ')
    print('<table style="width: 100%; text-align: left; margin-left: auto; margin-right: auto; border-color: gray;"')
    print('<tr>')
    print('<tr style="font-weight: bold;">')
    print('<td colspan="2" style="text-align: center; background-color: '+color[1]+'">'+row.map+'</td>')
    print('</tr>')
    print('<td style="font-weight: bold; font-style: italic;"><small>Player</small></td>')
    print('<td style="font-weight: bold; font-style: italic;"><small>KTD</small></td>')
    print('</tr>')


    for player in map_stats:
        try:
            print('<tr style=" background-color: '+bgcolor[1]+';">')
            print('<td style="border-bottom: 1px solid #ddd; font-weight: bold; font-size: 100%;">'+player.playerDisplayName+'</td>')
            print('<td style="border-bottom: 1px solid #ddd;">'+str(round((player.KTD),2))+'</td></tr>')
        except:
            continue
        print('</tr>')

    print('</table></td>')
    c_count += 1
    if c_count > 3:
        print('</tr><tr>')
        c_count = 1
print('</table>')
gf_procs.set_footer()
