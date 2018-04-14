#!e:/Python36/python.exe
import sys
import datetime
import pyodbc
import logging
import gf_procs

logging.basicConfig(filename='gf.log',level=logging.INFO, format='%(asctime)s %(message)s')

cnx = pyodbc.connect("DSN=geek")
cursor = cnx.cursor()

style="""
<style>
.tile {
height:130px;
width:250px;
float:left;
margin:25px 5px 0 0;
padding:5px;
background-image:url("/dogtag.jpg");
background-repeat: no-repeat;
}

.indent {
    margin-left: 65px;
    margin-top: 10px;
    color: #444547
    font-family: sans-serif, Arial, Helvetica;
    }
    
</style>
"""
htmlFormat = """
  <center>
    
  </center>
"""
q_geeks = "select * from hlstatsx.geeks order by handle"

geeks = list(cursor.execute(q_geeks))

gf_procs.set_header(5)
print(style)
for row in geeks:
    print('<DIV class="tile"><div class="indent"><font size="4"><b>'+row.handle.upper()+'</b></font>')
    print('<BR><i>'+row.firstname+' </i>')
    print('<BR>Location: '+row.location+' ')
    print('<BR>Member Since: '+"{:%Y}".format(row.memberSince))
    print('<BR><font size = "2"><B>GF2K18:'+row.attendingGF2018+'</b></font></DIV></div>')

print('<BR><BR>GF2K12 Stats:  <a href="https://docs.google.com/spreadsheets/d/1jHva53qfLlvwaQDcpyAWKumWTDGL5xaIY4Xi0Cd7iuA/edit#gid=0">GF2K12</a>')
print('<BR><BR>GF2K11 Stats:  <a href="https://docs.google.com/spreadsheets/d/1VaEhj9Old1RC4vjqHZr2abv-R2iswEw3w4OlOentnfQ">GF2K11</a>')

 
gf_procs.set_footer()
