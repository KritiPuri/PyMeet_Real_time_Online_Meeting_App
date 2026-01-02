"""
LobbyView (updated) - waiting room: create room, view room list & join rooms.
- Displays username in header.
- Double-click room to quickly join; Enter also joins.
- Has quick input box to join by name if you don't want to select from list.
"""
import re
import tkinter as tk
from tkinter import ttk, messagebox
from typing import List

FONT_H1 = ("Segoe UI", 16, "bold")


class ValidEntry(ttk.Frame):
    def __init__(self, parent, label: str, pattern=None, placeholder: str = ""):
        super().__init__(parent)
        ttk.Label(self, text=label).pack(anchor=tk.W)
        inner = ttk.Frame(self, style="Panel.TFrame")
        inner.pack(fill=tk.X, pady=4)
        self.var = tk.StringVar()
        self.entry = ttk.Entry(inner, textvariable=self.var)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8, pady=6)
        self.pattern = pattern
        if placeholder:
            self.entry.insert(0, placeholder)

    def value(self) -> str:
        return self.var.get().strip()

    def valid(self) -> bool:
        v = self.value()
        if not v:
            return False
        if self.pattern is None:
            return True
        return bool(self.pattern.fullmatch(v))


class LobbyView(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, style="TFrame")
        self.app = app

        hdr = ttk.Frame(self, style="TFrame")
        hdr.pack(fill=tk.X, padx=16, pady=10)
        self.lbl_title = ttk.Label(hdr, text="Lobby", font=FONT_H1)
        self.lbl_title.pack(side=tk.LEFT)
        ttk.Button(hdr, text="Logout", style="Danger.TButton", command=lambda: self.app.show("LoginView")).pack(side=tk.RIGHT)

        body = ttk.Frame(self, style="TFrame")
        body.pack(fill=tk.BOTH, expand=True, padx=16, pady=10)

        # Create room
        create = ttk.Labelframe(body, text="Create new room", style="Card.TLabelframe", padding=16)
        create.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))
        self.ent_room = ValidEntry(create, "Room name", pattern=re.compile(r"^[A-Za-z0-9_.-]{1,32}$"))
        self.ent_room.pack(fill=tk.X)
        ttk.Button(create, text="Create room", style="Primary.TButton", command=self._create).pack(anchor=tk.E, pady=(12, 0))

        # Join room
        join = ttk.Labelframe(body, text="Available rooms", style="Card.TLabelframe", padding=16)
        join.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(8, 0))

        self.lst_rooms = tk.Listbox(join, height=14, bg="#0f172a", fg="#e5e7eb", highlightthickness=0, selectbackground="#271ec3")
        self.lst_rooms.pack(fill=tk.BOTH, expand=True)
        self.lst_rooms.bind("<Double-1>", lambda e: self._join_sel())
        self.lst_rooms.bind("<Return>", lambda e: self._join_sel())

        quick = ttk.Frame(join, style="Panel.TFrame")
        quick.pack(fill=tk.X, pady=(10, 0))
        ttk.Label(quick, text="Enter room name to join quickly:").pack(anchor=tk.W)
        self.ent_quick = ttk.Entry(quick)
        self.ent_quick.pack(fill=tk.X, pady=(4, 0))

        row = ttk.Frame(join, style="Panel.TFrame")
        row.pack(fill=tk.X, pady=(10, 0))
        ttk.Button(row, text="Refresh room list", command=self.app.refresh_rooms).pack(side=tk.LEFT)
        ttk.Button(row, text="Join room", style="Primary.TButton", command=self._join_action).pack(side=tk.RIGHT)

    # lifecycle
    def on_show(self):
        # Update header with username
        u = getattr(self.app, "username", None) or "—"
        self.lbl_title.configure(text=f"Lobby – {u}")
        self.app.refresh_rooms()

    # callbacks from app
    def populate_rooms(self, rooms: List[dict]) -> None:
        self.lst_rooms.delete(0, tk.END)
        for r in rooms:
            self.lst_rooms.insert(tk.END, f"{r['name']}  [{r['users']}]")

    # actions
    def _create(self):
        if not self.ent_room.valid():
            messagebox.showwarning("Room", "Room name must contain only letters, numbers, '_', '-', '.' and be up to 32 characters.")
            return
        self.app.create_room(self.ent_room.value())

    def _join_sel(self):
        sel = self.lst_rooms.curselection()
        if not sel:
            return
        name = self.lst_rooms.get(sel[0]).split("  [")[0]
        self.app.join_room(name)

    def _join_action(self):
        # prefer quick input; if empty then use selection list
        name = self.ent_quick.get().strip()
        if name:
            if not re.fullmatch(r"^[A-Za-z0-9_.-]{1,32}$", name):
                messagebox.showwarning("Room", "Room name must contain only letters, numbers, '_', '-', '.' and be up to 32 characters")
                return
            self.app.join_room(name)
            return
        self._join_sel()
