#!/usr/bin/env python3
"""
Simple HTTP Server for OLS 3D Viewer
Serves the HTML file and data files for the Cesium-based OLS viewer
"""

import http.server
import socketserver
import os
import webbrowser
import threading
import time

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve files with proper CORS headers"""
    
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Override to provide cleaner logging"""
        print(f"[{self.address_string()}] {format % args}")

def open_browser(url, delay=2):
    """Open browser after a delay"""
    time.sleep(delay)
    print(f"🌐 Opening {url} in your default browser...")
    webbrowser.open(url)

def main():
    # Configuration
    PORT = 8000
    HOST = 'localhost'
    
    print("🛩️ OLS 3D Viewer - Python HTTP Server")
    print("=" * 50)
    
    # Change to the project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    print(f"📁 Serving from: {project_dir}")
    print(f"🌐 Server will run on: http://{HOST}:{PORT}")
    
    # Create the server
    with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 Server started on http://{HOST}:{PORT}")
        print("\n📋 Available pages:")
        print(f"   • Main viewer: http://{HOST}:{PORT}/examples/ols_3d_cesium_professional.html")
        print(f"   • Data folder: http://{HOST}:{PORT}/data/")
        print("\n⌨️  Press Ctrl+C to stop the server")
        
        # Start browser opening in background
        browser_thread = threading.Thread(
            target=open_browser, 
            args=(f"http://{HOST}:{PORT}/examples/ols_3d_cesium_professional.html",)
        )
        browser_thread.daemon = True
        browser_thread.start()
        
        try:
            # Start serving
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped by user")
        except OSError as e:
            if "Address already in use" in str(e):
                print(f"❌ Port {PORT} is already in use!")
                print(f"💡 Try a different port or stop the existing server")
                print(f"   Alternative: python -m http.server {PORT + 1}")
            else:
                print(f"❌ Server error: {e}")

if __name__ == "__main__":
    main()
