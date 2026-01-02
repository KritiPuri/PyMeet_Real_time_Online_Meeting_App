"""
Config for SERVER - runs on server machine (main.py).
Server will listen on all network interfaces (0.0.0.0).
"""

# Server host: listen on all IPs
SERVER_HOST = "0.0.0.0"
TCP_PORT = 8888

# UDP media ports
UDP_PORT_VOICE = 9999
UDP_PORT_VIDEO = 10000

# Backward compat (if old code calls UDP_PORT)
UDP_PORT = UDP_PORT_VOICE

# WebSocket Gateway
GATEWAY_PORT = 8765
WS_PORT = GATEWAY_PORT

APP_NAME = "PyMeet – Server"
