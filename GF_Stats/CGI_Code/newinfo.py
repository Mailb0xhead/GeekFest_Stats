#!e:/Python36/python.exe
# Define the form
content_header =  "Content-Type: text/html\n"
html_page = """
<html>
   <head> </head>
   <body>
      <h1>New Entry</h1>
      <p>Thank you for submitting %(name)s</p></br>
      <a href=form.py>Return to form</a>
   </body></html>
"""
# Python Code

import cgi
def process_form(email, title, desc):
   return "Your entry for: "+email+" has been processed"
form = cgi.FieldStorage()
#email = form.getvalue("email","")
name = form.getvalue("name","")
#desc = form.getvalue("desc","")
if not name:
   message = "Please enter Title and Email"
# present the form
print (content_header)
print (html_page % {"name":name})
