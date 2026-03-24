"""
╔══════════════════════════════════════════════════════════════════╗
║         QUIZ ARENA — Full-Screen Premium Login v3                ║
║         Real DB stats  •  Python Tkinter + SQLite                ║
╚══════════════════════════════════════════════════════════════════╝
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
import datetime
import math
import platform

# ────────────────────────────────────────────────────────────────
#  DATABASE
# ────────────────────────────────────────────────────────────────

DB_PATH = "quiz_arena.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()

    # USER table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS USER (
            User_ID   INTEGER PRIMARY KEY AUTOINCREMENT,
            Username  TEXT NOT NULL UNIQUE,
            Email     TEXT NOT NULL UNIQUE,
            Password  TEXT NOT NULL,
            Join_Date TEXT NOT NULL
        )
    """)

    # ADMIN table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ADMIN (
            Admin_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL UNIQUE
        )
    """)

    # TOPIC table (from ER diagram)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS TOPIC (
            Topic_ID         INTEGER PRIMARY KEY AUTOINCREMENT,
            Topic_Name       TEXT NOT NULL UNIQUE,
            Difficulty_Level TEXT NOT NULL
        )
    """)

    # QUESTION table (from ER diagram)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS QUESTION (
            Question_ID    INTEGER PRIMARY KEY AUTOINCREMENT,
            Topic_ID       INTEGER NOT NULL,
            Question_Text  TEXT NOT NULL,
            Option_A       TEXT NOT NULL,
            Option_B       TEXT NOT NULL,
            Option_C       TEXT NOT NULL,
            Option_D       TEXT NOT NULL,
            Correct_Option TEXT NOT NULL,
            FOREIGN KEY (Topic_ID) REFERENCES TOPIC(Topic_ID)
        )
    """)

    # QUIZ_ATTEMPT table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS QUIZ_ATTEMPT (
            Attempt_ID      INTEGER PRIMARY KEY AUTOINCREMENT,
            User_ID         INTEGER NOT NULL,
            Topic_ID        INTEGER NOT NULL,
            Start_Time      TEXT,
            End_Time        TEXT,
            Score           INTEGER DEFAULT 0,
            Correct_Answers INTEGER DEFAULT 0,
            FOREIGN KEY (User_ID)  REFERENCES USER(User_ID),
            FOREIGN KEY (Topic_ID) REFERENCES TOPIC(Topic_ID)
        )
    """)

    conn.commit()
    conn.close()


def hash_pw(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()


# ── REAL LIVE STATS FROM DATABASE ────────────────────────────────

def get_live_stats() -> dict:
    """Query actual counts from the DB — no fake numbers."""
    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()

    user_count     = cur.execute("SELECT COUNT(*) FROM USER").fetchone()[0]
    question_count = cur.execute("SELECT COUNT(*) FROM QUESTION").fetchone()[0]
    topic_count    = cur.execute("SELECT COUNT(*) FROM TOPIC").fetchone()[0]
    attempt_count  = cur.execute("SELECT COUNT(*) FROM QUIZ_ATTEMPT").fetchone()[0]

    conn.close()
    return {
        "users":     user_count,
        "questions": question_count,
        "topics":    topic_count,
        "attempts":  attempt_count,
    }


def fmt_stat(n: int, noun: str) -> tuple[str, str]:
    """Return (display_number, label) — honest zero-friendly."""
    if n == 0:
        return "—", noun
    elif n >= 1000:
        return f"{n/1000:.1f}K", noun
    else:
        return str(n), noun


# ── AUTH ──────────────────────────────────────────────────────────

def db_register(username, email, password):
    if not username or not email or not password:
        return False, "All fields are required."
    if len(password) < 6:
        return False, "Password must be at least 6 characters."
    if "@" not in email or "." not in email.split("@")[-1]:
        return False, "Enter a valid email address."
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute(
            "INSERT INTO USER (Username, Email, Password, Join_Date) VALUES (?,?,?,?)",
            (username, email, hash_pw(password), datetime.date.today().isoformat())
        )
        conn.commit()
        conn.close()
        return True, f"Welcome aboard, {username}!  Your account is ready."
    except sqlite3.IntegrityError as e:
        conn.close()
        if "Username" in str(e): return False, "Username already taken. Try another."
        if "Email"    in str(e): return False, "This email is already registered."
        return False, "Registration failed. Please try again."


def db_login(username, password):
    if not username or not password:
        return False, "Please fill in both fields."
    conn = sqlite3.connect(DB_PATH)
    row  = conn.execute(
        "SELECT User_ID, Username FROM USER WHERE Username=? AND Password=?",
        (username, hash_pw(password))
    ).fetchone()
    conn.close()
    if row:
        return True, f"Welcome back, {row[1]}!"
    return False, "Invalid username or password. Please try again."


# ────────────────────────────────────────────────────────────────
#  PALETTE
# ────────────────────────────────────────────────────────────────

P = {
    "bg_card":    "#FFFFFF",
    "bg_side":    "#1A1F36",
    "bg_input":   "#F9F8F6",
    "bg_input_f": "#FFFFFF",
    "navy_lt":    "#2D3561",
    "orange":     "#FF6B2B",
    "orange_h":   "#E55A1A",
    "teal":       "#00B8A9",
    "teal_h":     "#009688",
    "text_h":     "#111827",
    "text_b":     "#374151",
    "text_m":     "#6B7280",
    "text_l":     "#9CA3AF",
    "border":     "#E5E7EB",
    "border_f":   "#FF6B2B",
    "white":      "#FFFFFF",
    "divider":    "#F3F4F6",
    "zero_fg":    "#4B5563",   # muted colour when stat is zero / dashes
}


# ────────────────────────────────────────────────────────────────
#  FONTS  (scale with screen)
# ────────────────────────────────────────────────────────────────

def make_fonts(scale: float = 1.0):
    s = scale
    return {
        "brand":  ("Georgia",           int(20*s), "bold"),
        "h1":     ("Georgia",           int(24*s), "bold"),
        "h2":     ("Georgia",           int(18*s), "bold"),
        "sub":    ("Segoe UI",          int(11*s)),
        "label":  ("Segoe UI",          int(10*s), "bold"),
        "input":  ("Segoe UI",          int(12*s)),
        "btn":    ("Segoe UI",          int(12*s), "bold"),
        "small":  ("Segoe UI",          int(10*s)),
        "tiny":   ("Segoe UI",           int(9*s)),
        "tag":    ("Segoe UI",           int(9*s), "bold"),
        "stat_n": ("Georgia",           int(22*s), "bold"),
        "stat_l": ("Segoe UI",           int(9*s)),
        "quote":  ("Georgia",           int(10*s), "italic"),
        "hero":   ("Georgia",           int(26*s), "bold"),
        "zero":   ("Segoe UI",          int(10*s), "italic"),
    }


# ────────────────────────────────────────────────────────────────
#  ANIMATED DOT CANVAS
# ────────────────────────────────────────────────────────────────

class DotsCanvas(tk.Canvas):
    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self._phase = 0
        self._dots  = []
        self.bind("<Configure>", self._on_resize)
        self._animate()

    def _on_resize(self, e=None):
        self._dots = []
        w = self.winfo_width()
        h = self.winfo_height()
        step = 36
        for x in range(step, w, step):
            for y in range(step, h, step):
                self._dots.append((x, y))

    def _animate(self):
        self.delete("dot")
        for i, (x, y) in enumerate(self._dots):
            val  = math.sin(self._phase + i * 0.18) * 0.5 + 0.5
            grey = int(55 + val * 60)
            col  = f"#{grey:02x}{grey:02x}{min(grey+25,255):02x}"
            r    = 1.2 + val * 1.6
            self.create_oval(x-r, y-r, x+r, y+r,
                             fill=col, outline="", tags="dot")
        self._phase += 0.04
        self.after(60, self._animate)


# ────────────────────────────────────────────────────────────────
#  BORDERED ENTRY
# ────────────────────────────────────────────────────────────────

class BorderEntry(tk.Frame):
    def __init__(self, parent, show=None, F=None, **kw):
        super().__init__(parent, bg=P["bg_card"], **kw)
        self._F = F or {}
        self._outer = tk.Frame(self, bg=P["border"], padx=1, pady=1)
        self._outer.pack(fill="x")
        self._inner = tk.Frame(self._outer, bg=P["bg_input"])
        self._inner.pack(fill="x")
        self.entry = tk.Entry(
            self._inner,
            font=self._F.get("input", ("Segoe UI", 12)),
            bg=P["bg_input"], fg=P["text_b"],
            insertbackground=P["orange"],
            relief="flat", bd=0,
            show=show or "",
        )
        self.entry.pack(fill="x", padx=14, pady=12)
        self.entry.bind("<FocusIn>",  self._on_focus)
        self.entry.bind("<FocusOut>", self._on_blur)

    def _on_focus(self, _):
        self._outer.config(bg=P["border_f"])
        self._inner.config(bg=P["bg_input_f"])
        self.entry.config(bg=P["bg_input_f"])

    def _on_blur(self, _):
        self._outer.config(bg=P["border"])
        self._inner.config(bg=P["bg_input"])
        self.entry.config(bg=P["bg_input"])

    def get(self):         return self.entry.get()
    def set_show(self, c): self.entry.config(show=c)
    def focus_set(self):   self.entry.focus_set()


# ────────────────────────────────────────────────────────────────
#  FLAT BUTTON
# ────────────────────────────────────────────────────────────────

class FlatBtn(tk.Label):
    def __init__(self, parent, text, command,
                 bg=None, fg="#FFFFFF", hover=None, F=None, **kw):
        self._bg    = bg    or P["orange"]
        self._hover = hover or P["orange_h"]
        self._cmd   = command
        _F = F or {}
        super().__init__(parent, text=text,
                         font=_F.get("btn", ("Segoe UI", 12, "bold")),
                         bg=self._bg, fg=fg,
                         pady=13, cursor="hand2", relief="flat", **kw)
        self.bind("<Enter>",    lambda _: self.config(bg=self._hover))
        self.bind("<Leave>",    lambda _: self.config(bg=self._bg))
        self.bind("<Button-1>", lambda _: self._cmd())


# ────────────────────────────────────────────────────────────────
#  STAT CARD (shows real DB value, graceful when zero)
# ────────────────────────────────────────────────────────────────

def stat_card(parent, num_str: str, label: str, F: dict, is_zero: bool = False):
    """Small stat box for the left panel sidebar."""
    box = tk.Frame(parent, bg=P["navy_lt"], padx=14, pady=10)
    num_col = P["zero_fg"] if is_zero else P["orange"]
    tk.Label(box, text=num_str, font=F["stat_n"],
             bg=P["navy_lt"], fg=num_col).pack()
    tk.Label(box, text=label,   font=F["stat_l"],
             bg=P["navy_lt"], fg="#9CA3AF").pack()
    return box


# ────────────────────────────────────────────────────────────────
#  MAIN APP
# ────────────────────────────────────────────────────────────────

class QuizArenaApp(tk.Tk):

    def __init__(self):
        super().__init__()
        init_db()

        self.title("Quiz Arena")
        self.configure(bg=P["bg_card"])

        # ── FULL SCREEN ──────────────────────────────────────────
        os_name = platform.system()
        if os_name == "Windows":
            self.state("zoomed")          # maximised with taskbar on Windows
        elif os_name == "Darwin":         # macOS
            self.attributes("-zoomed", True)
        else:                             # Linux
            self.attributes("-zoomed", True)

        self.resizable(True, True)

        # calculate a font scale based on screen height
        self.update_idletasks()
        sh = self.winfo_screenheight()
        self._scale = max(0.85, min(1.3, sh / 900))
        self._F = make_fonts(self._scale)

        self._show_login()

    # ── helpers ──────────────────────────────────────────────────

    def _clear(self):
        for w in self.winfo_children():
            w.destroy()

    def _left_width(self) -> int:
        """38% of current window width, capped 340-520."""
        self.update_idletasks()
        w = self.winfo_width() or self.winfo_screenwidth()
        return max(340, min(520, int(w * 0.38)))

    # ── shared left panel builder ────────────────────────────────

    def _build_left(self, parent, accent_color: str,
                    headline: str, sub_text: str,
                    extra_widget_fn=None) -> tk.Frame:

        lw = self._left_width()
        left = tk.Frame(parent, bg=P["bg_side"], width=lw)
        left.pack(side="left", fill="y")
        left.pack_propagate(False)

        # animated background
        bg_canvas = DotsCanvas(left, bg=P["bg_side"], highlightthickness=0)
        bg_canvas.place(relwidth=1, relheight=1)

        # content frame centred inside
        lc = tk.Frame(left, bg=P["bg_side"])
        lc.place(relx=0.08, rely=0.48, anchor="w")

        # logo row
        logo_row = tk.Frame(lc, bg=P["bg_side"])
        logo_row.pack(anchor="w", pady=(0, 26))

        logo_box = tk.Frame(logo_row, bg=accent_color)
        logo_box.pack(side="left")
        tk.Label(logo_box, text=" QA ",
                 font=self._F["brand"],
                 bg=accent_color, fg=P["white"],
                 padx=6, pady=4).pack()

        tk.Label(logo_row, text="  Quiz Arena",
                 font=self._F["brand"],
                 bg=P["bg_side"], fg=P["white"]).pack(side="left")

        # headline
        tk.Label(lc, text=headline,
                 font=self._F["hero"],
                 bg=P["bg_side"], fg=P["white"],
                 justify="left").pack(anchor="w", pady=(0, 12))

        # sub text
        tk.Label(lc, text=sub_text,
                 font=self._F["sub"],
                 bg=P["bg_side"], fg="#8899BB",
                 justify="left").pack(anchor="w", pady=(0, 26))

        # ── REAL STATS FROM DB ───────────────────────────────────
        stats = get_live_stats()

        stat_data = [
            fmt_stat(stats["questions"], "Questions"),
            fmt_stat(stats["users"],     "Users"),
            fmt_stat(stats["topics"],    "Topics"),
        ]

        stats_row = tk.Frame(lc, bg=P["bg_side"])
        stats_row.pack(anchor="w", pady=(0, 6))

        for num_str, lbl in stat_data:
            is_zero = (num_str == "—")
            card = stat_card(stats_row, num_str, lbl, self._F, is_zero)
            card.pack(side="left", padx=(0, 8))

        # "Be the first!" hint when all zeros
        if stats["users"] == 0:
            tk.Label(lc,
                     text="✨  Be the very first to join Quiz Arena!",
                     font=self._F["zero"],
                     bg=P["bg_side"], fg="#6B7280").pack(anchor="w", pady=(6, 14))
        else:
            tk.Label(lc, text="", bg=P["bg_side"]).pack(pady=8)  # spacer

        # extra content (tags / perks) injected by caller
        if extra_widget_fn:
            extra_widget_fn(lc)

        # bottom quote
        tk.Label(left, text='"Code. Compete. Conquer."',
                 font=self._F["quote"],
                 bg=P["bg_side"], fg="#4B5563").place(
                 relx=0.5, rely=0.97, anchor="s")

        # bottom colour accent strip
        tk.Frame(left, bg=accent_color, height=4).place(
            relx=0, rely=1.0, anchor="sw", relwidth=1)

        return left

    # ═══════════════════════════════════════════════════════════
    #  LOGIN SCREEN
    # ═══════════════════════════════════════════════════════════

    def _show_login(self):
        self._clear()
        self.configure(bg=P["bg_card"])

        root = tk.Frame(self, bg=P["bg_card"])
        root.pack(fill="both", expand=True)

        # ── LEFT ─────────────────────────────────────────────────
        def login_extras(lc):
            tags_r1 = tk.Frame(lc, bg=P["bg_side"])
            tags_r1.pack(anchor="w", pady=(0, 5))
            tags_r2 = tk.Frame(lc, bg=P["bg_side"])
            tags_r2.pack(anchor="w")
            for t in ["#DSA", "#DBMS", "#OS"]:
                tk.Label(tags_r1, text=t, font=self._F["tag"],
                         bg="#2D3561", fg="#93C5FD",
                         padx=8, pady=4).pack(side="left", padx=(0, 6))
            for t in ["#CN", "#Python", "#C++"]:
                tk.Label(tags_r2, text=t, font=self._F["tag"],
                         bg="#2D3561", fg="#93C5FD",
                         padx=8, pady=4).pack(side="left", padx=(0, 6))

        self._build_left(
            root,
            accent_color=P["orange"],
            headline="Master CSE.\nClimb the\nLeaderboard.",
            sub_text="Practice DSA, DBMS, OS,\nNetworks & more with real\ncompetitive challenges.",
            extra_widget_fn=login_extras,
        )

        # ── RIGHT ────────────────────────────────────────────────
        right = tk.Frame(root, bg=P["bg_card"])
        right.pack(side="left", fill="both", expand=True)

        form = tk.Frame(right, bg=P["bg_card"])
        form.place(relx=0.5, rely=0.5, anchor="center")

        # heading
        tk.Label(form, text="Sign in to",
                 font=self._F["sub"],
                 bg=P["bg_card"], fg=P["text_m"]).pack(anchor="w")
        tk.Label(form, text="Quiz Arena",
                 font=self._F["h1"],
                 bg=P["bg_card"], fg=P["text_h"]).pack(anchor="w")
        tk.Frame(form, bg=P["orange"], height=3, width=60).pack(
                 anchor="w", pady=(5, 24))

        # username
        tk.Label(form, text="USERNAME", font=self._F["label"],
                 bg=P["bg_card"], fg=P["text_m"]).pack(anchor="w")
        self.l_user = BorderEntry(form, F=self._F, width=350)
        self.l_user.pack(fill="x", pady=(4, 16))

        # password
        tk.Label(form, text="PASSWORD", font=self._F["label"],
                 bg=P["bg_card"], fg=P["text_m"]).pack(anchor="w")
        self.l_pwd = BorderEntry(form, show="*", F=self._F, width=350)
        self.l_pwd.pack(fill="x", pady=(4, 0))

        # show pwd + forgot
        pw_row = tk.Frame(form, bg=P["bg_card"])
        pw_row.pack(fill="x", pady=(8, 22))

        self._lshow = tk.BooleanVar()
        tk.Checkbutton(
            pw_row, text="Show password",
            variable=self._lshow,
            command=lambda: self.l_pwd.set_show(
                "" if self._lshow.get() else "*"),
            bg=P["bg_card"], fg=P["text_m"],
            selectcolor=P["bg_card"],
            activebackground=P["bg_card"],
            font=self._F["small"], bd=0, cursor="hand2",
        ).pack(side="left")

        tk.Label(pw_row, text="Forgot password?",
                 font=(self._F["small"][0], self._F["small"][1], "bold"),
                 bg=P["bg_card"], fg=P["orange"],
                 cursor="hand2").pack(side="right")

        # sign-in button
        FlatBtn(form, "Sign In  →", self._do_login,
                bg=P["orange"], hover=P["orange_h"], F=self._F).pack(fill="x")

        # divider
        sep = tk.Frame(form, bg=P["bg_card"])
        sep.pack(fill="x", pady=20)
        tk.Frame(sep, bg=P["divider"], height=1).pack(fill="x")
        tk.Label(sep, text=" OR ", font=self._F["tiny"],
                 bg=P["bg_card"], fg=P["text_l"]).place(relx=0.5, y=-8, anchor="n")

        # switch
        sw = tk.Frame(form, bg=P["bg_card"])
        sw.pack()
        tk.Label(sw, text="New to Quiz Arena?  ",
                 font=self._F["small"],
                 bg=P["bg_card"], fg=P["text_m"]).pack(side="left")
        ca = tk.Label(sw, text="Create Account →",
                      font=(self._F["small"][0], self._F["small"][1], "bold"),
                      bg=P["bg_card"], fg=P["orange"], cursor="hand2")
        ca.pack(side="left")
        ca.bind("<Button-1>", lambda _: self._show_register())

        # terms
        tk.Label(form,
                 text="By signing in you agree to our Terms of Service & Privacy Policy.",
                 font=self._F["tiny"],
                 bg=P["bg_card"], fg=P["text_l"],
                 wraplength=340, justify="center").pack(pady=(20, 0))

        self.bind("<Return>", lambda _: self._do_login())
        self.l_user.focus_set()

    # ═══════════════════════════════════════════════════════════
    #  REGISTER SCREEN
    # ═══════════════════════════════════════════════════════════

    def _show_register(self):
        self._clear()
        self.configure(bg=P["bg_card"])

        root = tk.Frame(self, bg=P["bg_card"])
        root.pack(fill="both", expand=True)

        # ── LEFT ─────────────────────────────────────────────────
        def register_extras(lc):
            perks = [
                ("🏆", "Compete on Live Leaderboards"),
                ("📚", "CSE Topics — Added by Admin"),
                ("🎯", "Track Your Progress Daily"),
                ("🏅", "Earn Badges & Certificates"),
            ]
            for icon, text in perks:
                row = tk.Frame(lc, bg=P["bg_side"])
                row.pack(anchor="w", pady=4)
                tk.Label(row, text=icon,
                         font=self._F["sub"],
                         bg=P["bg_side"]).pack(side="left")
                tk.Label(row, text=f"  {text}",
                         font=self._F["small"],
                         bg=P["bg_side"], fg="#CBD5E1").pack(side="left")

        self._build_left(
            root,
            accent_color=P["teal"],
            headline="Start Your\nJourney\nToday.",
            sub_text="Create a free account and start\ncompeting with CSE students\nworldwide.",
            extra_widget_fn=register_extras,
        )

        # ── RIGHT ────────────────────────────────────────────────
        right = tk.Frame(root, bg=P["bg_card"])
        right.pack(side="left", fill="both", expand=True)

        form = tk.Frame(right, bg=P["bg_card"])
        form.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(form, text="Join the arena,",
                 font=self._F["sub"],
                 bg=P["bg_card"], fg=P["text_m"]).pack(anchor="w")
        tk.Label(form, text="Create Account",
                 font=self._F["h1"],
                 bg=P["bg_card"], fg=P["text_h"]).pack(anchor="w")
        tk.Frame(form, bg=P["teal"], height=3, width=60).pack(
                 anchor="w", pady=(5, 20))

        # username
        tk.Label(form, text="USERNAME", font=self._F["label"],
                 bg=P["bg_card"], fg=P["text_m"]).pack(anchor="w")
        self.r_user = BorderEntry(form, F=self._F, width=350)
        self.r_user.pack(fill="x", pady=(4, 14))

        # email
        tk.Label(form, text="EMAIL ADDRESS", font=self._F["label"],
                 bg=P["bg_card"], fg=P["text_m"]).pack(anchor="w")
        self.r_email = BorderEntry(form, F=self._F, width=350)
        self.r_email.pack(fill="x", pady=(4, 14))

        # password
        tk.Label(form, text="PASSWORD", font=self._F["label"],
                 bg=P["bg_card"], fg=P["text_m"]).pack(anchor="w")
        self.r_pwd = BorderEntry(form, show="*", F=self._F, width=350)
        self.r_pwd.pack(fill="x", pady=(4, 2))
        tk.Label(form, text="Minimum 6 characters",
                 font=self._F["tiny"],
                 bg=P["bg_card"], fg=P["text_l"]).pack(anchor="w", pady=(0, 12))

        # confirm password
        tk.Label(form, text="CONFIRM PASSWORD", font=self._F["label"],
                 bg=P["bg_card"], fg=P["text_m"]).pack(anchor="w")
        self.r_cpwd = BorderEntry(form, show="*", F=self._F, width=350)
        self.r_cpwd.pack(fill="x", pady=(4, 0))

        # show passwords toggle
        self._rshow = tk.BooleanVar()
        def _toggle_r():
            ch = "" if self._rshow.get() else "*"
            self.r_pwd.set_show(ch)
            self.r_cpwd.set_show(ch)

        tk.Checkbutton(
            form, text="Show passwords",
            variable=self._rshow, command=_toggle_r,
            bg=P["bg_card"], fg=P["text_m"],
            selectcolor=P["bg_card"],
            activebackground=P["bg_card"],
            font=self._F["small"], bd=0, cursor="hand2",
        ).pack(anchor="w", pady=(10, 18))

        # register button (teal)
        FlatBtn(form, "Create Account  →", self._do_register,
                bg=P["teal"], fg=P["white"], hover=P["teal_h"],
                F=self._F).pack(fill="x")

        # switch back
        sw = tk.Frame(form, bg=P["bg_card"])
        sw.pack(pady=(16, 0))
        tk.Label(sw, text="Already have an account?  ",
                 font=self._F["small"],
                 bg=P["bg_card"], fg=P["text_m"]).pack(side="left")
        si = tk.Label(sw, text="Sign In →",
                      font=(self._F["small"][0], self._F["small"][1], "bold"),
                      bg=P["bg_card"], fg=P["orange"], cursor="hand2")
        si.pack(side="left")
        si.bind("<Button-1>", lambda _: self._show_login())

        tk.Label(form,
                 text="By registering you agree to our Terms of Service & Privacy Policy.",
                 font=self._F["tiny"],
                 bg=P["bg_card"], fg=P["text_l"],
                 wraplength=340, justify="center").pack(pady=(18, 0))

        self.bind("<Return>", lambda _: self._do_register())
        self.r_user.focus_set()

    # ═══════════════════════════════════════════════════════════
    #  ACTIONS
    # ═══════════════════════════════════════════════════════════

    def _do_login(self):
        u = self.l_user.get().strip()
        p = self.l_pwd.get()
        ok, msg = db_login(u, p)
        if ok:
            messagebox.showinfo("✅  Welcome!", msg, parent=self)
            # TODO: navigate to Topic Selection screen (next phase)
        else:
            messagebox.showerror("❌  Login Failed", msg, parent=self)

    def _do_register(self):
        u  = self.r_user.get().strip()
        e  = self.r_email.get().strip()
        p  = self.r_pwd.get()
        cp = self.r_cpwd.get()
        if p != cp:
            messagebox.showerror("❌  Mismatch",
                                 "Passwords do not match. Please try again.",
                                 parent=self)
            return
        ok, msg = db_register(u, e, p)
        if ok:
            messagebox.showinfo("✅  Account Created!", msg, parent=self)
            self._show_login()   # go back to login after success
        else:
            messagebox.showerror("❌  Registration Failed", msg, parent=self)


# ────────────────────────────────────────────────────────────────
#  ENTRY POINT
# ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = QuizArenaApp()
    app.mainloop()