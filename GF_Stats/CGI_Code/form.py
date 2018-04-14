#!e:/Python36/python.exe
# Define the form
content_header =  "Content-Type: text/html\n"
html_page = """
<html>
   <head> </head>
   <body>
      <h1>Entry Form</h1>
      <form method=post action=form.py>
      <p><label>Title: </label><input type=text name=title value=%(title)s ></p >
      <p>Description: </p>
      <textarea name = desc rows=4 cols=60 >%(desc)s</textarea >
      <p><a href=newinfo.py?name=TESTWORKS>CLICK HERE</a></p>
      <p><label>Email-id: <input type=text name=email value=%(email)s ></label></p >
      <button type=”submit”>Submit</button>
      <h4>%(message)s<h4>
      </form>
   </body></html>
"""
# Python Code

import cgi
def process_form(email, title, desc):
   return "Your entry for: "+email+" has been processed"
form = cgi.FieldStorage()
email = form.getvalue("email","")
title = form.getvalue("title","")
desc = form.getvalue("desc","")
if not email or not title:
   message = "Please enter Title and Email"
else:
   message = process_form(email, title, desc)
   email = title = desc = ""
# present the form
print (content_header)
print (html_page % {"title":title, "email":email, "desc":desc, "message":message})
