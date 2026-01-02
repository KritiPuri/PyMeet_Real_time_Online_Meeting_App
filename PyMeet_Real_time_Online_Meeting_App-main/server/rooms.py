from typing import Dict, Set, Optional

# Room list: room_name -> set(username)
rooms: Dict[str, Set[str]] = {}

def create_room(room: str):
    """Create a new room if it doesn't exist"""
    rooms.setdefault(room, set())

def join_room(username: str, room: str, clients: Dict):
    """Add user to room"""
    create_room(room)
    rooms[room].add(username)
    clients[username].room = room

def leave_room(username: str, clients: Dict):
    """User leaves current room"""
    room = clients[username].room
    if room and room in rooms:
        rooms[room].discard(username)
        if not rooms[room]:
            del rooms[room]
    clients[username].room = None

def get_user_room(username: str, clients: Dict) -> Optional[str]:
    """Get user's current room"""
    return clients[username].room if username in clients else None

def list_rooms():
    """List of all rooms"""
    return list(rooms.keys())

def list_users(room: str):
    """List of users in a room"""
    return list(rooms.get(room, []))
