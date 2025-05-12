#navigate to http://localhost:8000/metrics and check fake gpu_temp

# gpu_fake_exporter.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import random

class H(BaseHTTPRequestHandler): #extending BaseHTTPRequestHandler to define custom handlers (get, post, etc)
    def do_GET(self): #cusom GET
        #only scrape data from /metrics path
        if self.path != "/metrics":
            self.send_response(404); self.end_headers(); return
        temp = 40 + random.randint(0, 20) #randome temp between 40 and 60
        #expected prometheus text format (human readable title, graph type, value)
        body = f"""# HELP gpu_temp_c Fake GPU temperature
# TYPE gpu_temp_c gauge
gpu_temp_c {temp}
"""

        self.send_response(200); self.end_headers() #send ok response to prometheus, and ends header
        self.wfile.write(body.encode()) #BaseHTTPRequestHandler method to write to server

HTTPServer(('', 8000), H).serve_forever() #create and and listen on all networks '' (0.0.0.0) on port 8000 forever, using H class custom handlers