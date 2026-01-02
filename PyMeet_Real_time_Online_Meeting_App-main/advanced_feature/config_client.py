"""
Config for CLIENT - runs on client machine (meeting_gui_client).
Need to set SERVER_HOST to the server's IP address in LAN/VPN network.
"""

# Server IP address:
# - If running client on same machine as server: use "127.0.0.1"
# - If different machine: enter server's LAN IP or RadminVPN IP (e.g. "26.45.123.10")
SERVER_HOST = "127.0.0.1" # Localhost for running client and server on same machine

TCP_PORT = 8888
UDP_PORT_VOICE = 9999
UDP_PORT_VIDEO = 10000

UDP_PORT = UDP_PORT_VOICE

GATEWAY_PORT = 8765
WS_PORT = GATEWAY_PORT

APP_NAME = "PyMeet – Client"
