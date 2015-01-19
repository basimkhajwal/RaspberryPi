#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer


html = """

<!DOCTYPE html>
<html>
	<head>
		<title>Light Level's</title>
		
		<style type="text/css">
			strong, #a{
				padding-right: 20em;
			}
			
			*{
				text-align:center;
			}
			
		</style>
	</head>

	<body>
		<h1>Light Levels:</h1>
		<p><span id="a">Time:</span>Light level (lower is more light):</p>
		<p>
			%INFO%
		</p>
	</body>
	
</html>
"""


PORT_NUMBER = 80

class MyHandler(BaseHTTPRequestHandler):
	
    def do_HEAD(s):
	s.send_response(200)
	s.send_header("Content-type", "text/html")
	s.end_headers()
	
    #Handler for the GET requests
    def do_GET(s):
            
	s.send_response(200)
        s.send_header("Content-type", "text/html")
		
        s.end_headers()
		
	f = open('output/lightReadings.txt', 'r');
		
	stri = ""
		
	for line in f.read().split("\n"):
	    sections = line.split("\t")
	    
	    if len(sections) == 2:
	    	stri += "<strong>" + sections[0] + "</strong> " + sections[1] + "<br>"
		
	f.close()

	

	contents = html.replace("%INFO%", stri)
		
        s.wfile.write(contents)

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), MyHandler)
    print 'Started httpserver on port ' , PORT_NUMBER

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
