# START QUIZ ARENA 2.1

import tkinter as tk
from tkinter import messagebox
import random, time

# ═══════════════════════════════════════════════════════
#  COLOUR PALETTE
# ═══════════════════════════════════════════════════════
BG      = "#0B0F1A"
SURF    = "#111827"
SURF2   = "#1A2236"
SURF3   = "#212F45"
BORDER  = "#263048"
ORANGE  = "#F97316"
ORANGE2 = "#FB923C"
TEXT    = "#F1F5F9"
TEXT2   = "#94A3B8"
TEXT3   = "#475569"
GREEN   = "#10B981"
BLUE    = "#3B82F6"
PURPLE  = "#8B5CF6"
RED     = "#EF4444"
YELLOW  = "#F59E0B"
TEAL    = "#06B6D4"
WHITE   = "#FFFFFF"

# ═══════════════════════════════════════════════════════
#  QUIZ DATA
# ═══════════════════════════════════════════════════════
TOPICS = {
    "DSA": {
        "color": ORANGE, "icon": "DSA",
        "desc": "Data Structures & Algorithms",
        "questions": [
            {"q": "What is the time complexity of Binary Search?",
             "opts": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "ans": 1,
             "exp": "Binary Search halves the search space each step -> O(log n)."},
            {"q": "Which data structure uses LIFO principle?",
             "opts": ["Queue", "Stack", "Tree", "Graph"], "ans": 1,
             "exp": "Stack = Last-In-First-Out."},
            {"q": "Worst-case time complexity of QuickSort?",
             "opts": ["O(n log n)", "O(n)", "O(n^2)", "O(log n)"], "ans": 2,
             "exp": "When pivot is always min/max, QuickSort degrades to O(n^2)."},
            {"q": "Which traversal visits root FIRST?",
             "opts": ["Inorder", "Postorder", "Preorder", "Level-order"], "ans": 2,
             "exp": "Preorder: Root -> Left -> Right."},
            {"q": "Which sorting algorithm is stable AND O(n log n)?",
             "opts": ["QuickSort", "HeapSort", "MergeSort", "SelectionSort"], "ans": 2,
             "exp": "MergeSort is stable and always O(n log n)."},
            {"q": "A complete binary tree with n leaves has how many nodes?",
             "opts": ["2n-1", "n+1", "2n", "n-1"], "ans": 0,
             "exp": "A full binary tree with n leaves has 2n-1 total nodes."},
            {"q": "Best data structure for BFS traversal?",
             "opts": ["Stack", "Queue", "Heap", "Array"], "ans": 1,
             "exp": "BFS uses a Queue (FIFO) to explore nodes level by level."},
            {"q": "Space complexity of Merge Sort?",
             "opts": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "ans": 2,
             "exp": "Merge Sort requires O(n) extra space for temporary arrays."},
            {"q": "What is the average time complexity of Hash Table lookup?",
             "opts": ["O(n)", "O(log n)", "O(1)", "O(n^2)"], "ans": 2,
             "exp": "Hash tables provide O(1) average-case lookup with a good hash function."},
            {"q": "Which data structure is used for implementing recursion?",
             "opts": ["Queue", "Stack", "Heap", "Tree"], "ans": 1,
             "exp": "Function call stack is a Stack (LIFO) used for recursion."},
        ]
    },
    "DBMS": {
        "color": TEAL, "icon": "DB",
        "desc": "Database Management Systems",
        "questions": [
            {"q": "Which normal form removes partial dependencies?",
             "opts": ["1NF", "2NF", "3NF", "BCNF"], "ans": 1,
             "exp": "2NF removes partial dependencies on the primary key."},
            {"q": "ACID stands for?",
             "opts": [
                 "Atomicity, Consistency, Isolation, Durability",
                 "Atomicity, Concurrency, Integrity, Durability",
                 "Access, Consistency, Isolation, Data",
                 "Atomicity, Consistency, Integration, Data"], "ans": 0,
             "exp": "ACID = Atomicity, Consistency, Isolation, Durability."},
            {"q": "Which JOIN returns ALL rows from BOTH tables?",
             "opts": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"], "ans": 3,
             "exp": "FULL OUTER JOIN returns all rows from both tables."},
            {"q": "Primary key does NOT allow?",
             "opts": ["Duplicate values only", "NULL values only",
                      "Both NULL and duplicate", "Foreign key refs"], "ans": 2,
             "exp": "Primary key must be UNIQUE AND NOT NULL."},
            {"q": "Which command permanently removes a table?",
             "opts": ["DELETE", "TRUNCATE", "DROP", "REMOVE"], "ans": 2,
             "exp": "DROP removes the table structure itself."},
            {"q": "What does a foreign key enforce?",
             "opts": ["Uniqueness", "Referential integrity", "NOT NULL", "Check constraint"], "ans": 1,
             "exp": "Foreign key enforces referential integrity between tables."},
            {"q": "Which command saves a transaction permanently?",
             "opts": ["SAVE", "ROLLBACK", "COMMIT", "END"], "ans": 2,
             "exp": "COMMIT makes all changes in a transaction permanent."},
            {"q": "What is a deadlock in DBMS?",
             "opts": ["A slow query", "Two transactions waiting for each other indefinitely",
                      "A corrupted index", "A failed backup"], "ans": 1,
             "exp": "Deadlock: two transactions each hold a lock the other needs."},
        ]
    },
    "OS": {
        "color": PURPLE, "icon": "OS",
        "desc": "Operating Systems",
        "questions": [
            {"q": "Which scheduling algorithm can cause starvation?",
             "opts": ["Round Robin", "FCFS", "Priority Scheduling", "SJF"], "ans": 2,
             "exp": "Priority Scheduling can starve low-priority processes."},
            {"q": "Deadlock requires which FOUR conditions simultaneously?",
             "opts": [
                 "Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait",
                 "Starvation, Aging, Preemption, Priority",
                 "Thrashing, Paging, Segmentation, Swapping",
                 "None of the above"], "ans": 0,
             "exp": "Coffman: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait."},
            {"q": "Virtual memory is typically stored on?",
             "opts": ["RAM", "Cache", "Hard Disk (Swap)", "Registers"], "ans": 2,
             "exp": "Swap space on disk acts as an extension of RAM."},
            {"q": "A semaphore with value 1 is called?",
             "opts": ["Counting semaphore", "Binary semaphore", "Mutex", "Monitor"], "ans": 1,
             "exp": "A binary semaphore has only two values: 0 and 1."},
            {"q": "Which page replacement has the lowest page fault rate?",
             "opts": ["FIFO", "LRU", "Optimal (OPT)", "MRU"], "ans": 2,
             "exp": "OPT replaces the page not used for longest future time."},
            {"q": "Which Unix system call creates a new process?",
             "opts": ["exec()", "fork()", "spawn()", "create()"], "ans": 1,
             "exp": "fork() creates a child by duplicating the parent process."},
            {"q": "What is thrashing in OS?",
             "opts": [
                 "Excessive CPU usage",
                 "Excessive paging causing low CPU utilisation",
                 "Memory fragmentation",
                 "Process starvation"], "ans": 1,
             "exp": "Thrashing: process spends more time paging than executing."},
            {"q": "Which memory allocation avoids external fragmentation?",
             "opts": ["First Fit", "Best Fit", "Worst Fit", "Paging"], "ans": 3,
             "exp": "Paging divides memory into fixed-size frames, eliminating external fragmentation."},
        ]
    },
    "C++": {
        "color": BLUE, "icon": "C+",
        "desc": "C++ Programming Language",
        "questions": [
            {"q": "Same function name with different parameters is called?",
             "opts": ["Inheritance", "Polymorphism", "Overloading", "Encapsulation"], "ans": 2,
             "exp": "Function overloading: same name, different signatures."},
            {"q": "What does 'virtual' keyword enable in C++?",
             "opts": ["Compile-time polymorphism", "Runtime polymorphism",
                      "Data hiding", "Multiple inheritance"], "ans": 1,
             "exp": "virtual enables dynamic dispatch / runtime polymorphism."},
            {"q": "Which operator accesses members via pointer?",
             "opts": [".", "->", "::", "*"], "ans": 1,
             "exp": "Arrow operator (->) dereferences and accesses a member."},
            {"q": "STL stands for?",
             "opts": ["Standard Template Library", "Simple Template Library",
                      "Static Template Language", "Structured Template Library"], "ans": 0,
             "exp": "STL = Standard Template Library."},
            {"q": "Which smart pointer has EXCLUSIVE ownership?",
             "opts": ["shared_ptr", "weak_ptr", "unique_ptr", "auto_ptr"], "ans": 2,
             "exp": "unique_ptr cannot be copied - sole ownership."},
            {"q": "A pure virtual function is defined as?",
             "opts": ["No parameters", "=0", "static", "const"], "ans": 1,
             "exp": "Pure virtual (=0) makes the class abstract."},
            {"q": "Which is NOT an OOP principle?",
             "opts": ["Inheritance", "Polymorphism", "Compilation", "Encapsulation"], "ans": 2,
             "exp": "OOP pillars: Inheritance, Polymorphism, Encapsulation, Abstraction."},
        ]
    },
    "Python": {
        "color": RED, "icon": "Py",
        "desc": "Python Programming Language",
        "questions": [
            {"q": "Which keyword defines a generator function?",
             "opts": ["return", "yield", "generate", "produce"], "ans": 1,
             "exp": "yield pauses and returns a value, making a generator function."},
            {"q": "GIL stands for?",
             "opts": ["Global Import Library", "Global Interpreter Lock",
                      "General Interface Layer", "Generic Iteration Loop"], "ans": 1,
             "exp": "GIL = Global Interpreter Lock in CPython."},
            {"q": "Which method is called when an object is CREATED?",
             "opts": ["__init__", "__new__", "__create__", "__start__"], "ans": 0,
             "exp": "__init__ initialises a new object after creation."},
            {"q": "Output of: list(range(1, 10, 3))?",
             "opts": ["[1,3,5,7,9]", "[1,4,7]", "[1,4,7,10]", "[3,6,9]"], "ans": 1,
             "exp": "range(1,10,3) -> 1, 4, 7 (step 3, stops before 10)."},
            {"q": "Which returns an iterator of paired tuples?",
             "opts": ["map()", "filter()", "zip()", "enumerate()"], "ans": 2,
             "exp": "zip() pairs elements from multiple iterables into tuples."},
            {"q": "What is a decorator in Python?",
             "opts": ["A class variable", "A function that modifies another function",
                      "A type of loop", "An exception handler"], "ans": 1,
             "exp": "Decorators wrap a function to modify/extend its behaviour."},
            {"q": "Which data type is IMMUTABLE in Python?",
             "opts": ["List", "Dictionary", "Set", "Tuple"], "ans": 3,
             "exp": "Tuples are immutable - cannot be changed after creation."},
            {"q": "What does 'pass' do in Python?",
             "opts": ["Skips a function", "Does nothing (placeholder)", "Returns None", "Breaks loop"], "ans": 1,
             "exp": "pass is a null statement used as a placeholder in Python."},
        ]
    },
    "Networks": {
        "color": YELLOW, "icon": "CN",
        "desc": "Computer Networks",
        "questions": [
            {"q": "Which OSI layer handles routing of packets?",
             "opts": ["Data Link", "Network", "Transport", "Session"], "ans": 1,
             "exp": "Layer 3 (Network) routes packets via IP addresses."},
            {"q": "TCP uses which type of connection?",
             "opts": ["Connectionless", "Connection-oriented", "Broadcast", "Multicast"], "ans": 1,
             "exp": "TCP is connection-oriented, using 3-way handshake."},
            {"q": "Default subnet mask for Class C IP?",
             "opts": ["255.0.0.0", "255.255.0.0", "255.255.255.0", "255.255.255.255"], "ans": 2,
             "exp": "Class C: first 24 bits = network -> 255.255.255.0."},
            {"q": "DNS primarily operates on which port?",
             "opts": ["80", "21", "53", "443"], "ans": 2,
             "exp": "DNS uses UDP/TCP port 53."},
            {"q": "Which protocol assigns IPs automatically?",
             "opts": ["DNS", "ARP", "DHCP", "FTP"], "ans": 2,
             "exp": "DHCP = Dynamic Host Configuration Protocol."},
            {"q": "HTTPS uses which default port?",
             "opts": ["80", "8080", "443", "21"], "ans": 2,
             "exp": "HTTPS runs over TLS/SSL on port 443."},
            {"q": "Which device operates at OSI Layer 2?",
             "opts": ["Router", "Hub", "Switch", "Repeater"], "ans": 2,
             "exp": "Switches operate at the Data Link Layer (Layer 2)."},
        ]
    },
    "Java": {
        "color": "#FF6B6B", "icon": "Ja",
        "desc": "Java Programming Language",
        "questions": [
            {"q": "Which keyword prevents method overriding in Java?",
             "opts": ["static", "final", "private", "abstract"], "ans": 1,
             "exp": "final prevents a method from being overridden."},
            {"q": "Java's garbage collector manages?",
             "opts": ["Stack memory", "Heap memory", "Register memory", "Cache"], "ans": 1,
             "exp": "GC manages heap memory by removing unreachable objects."},
            {"q": "Which interface must be implemented for threading?",
             "opts": ["Callable", "Runnable", "Thread", "Executor"], "ans": 1,
             "exp": "Implementing Runnable and overriding run() enables threading."},
            {"q": "Default value of an int array element in Java?",
             "opts": ["null", "-1", "0", "undefined"], "ans": 2,
             "exp": "Java initialises int array elements to 0 by default."},
            {"q": "Which collection does NOT allow duplicates?",
             "opts": ["ArrayList", "LinkedList", "HashSet", "Vector"], "ans": 2,
             "exp": "HashSet is a Set - no duplicates allowed."},
            {"q": "What does 'static' mean in Java?",
             "opts": ["Belongs to instance", "Belongs to class", "Cannot change", "Always public"], "ans": 1,
             "exp": "Static members belong to the class, not any specific instance."},
        ]
    },
    "SQL": {
        "color": "#F59E0B", "icon": "SQL",
        "desc": "SQL & Database Queries",
        "questions": [
            {"q": "Which aggregate counts ALL rows including NULLs?",
             "opts": ["COUNT(col)", "COUNT(*)", "SUM(*)", "COUNT(DISTINCT col)"], "ans": 1,
             "exp": "COUNT(*) counts all rows; COUNT(col) ignores NULLs."},
            {"q": "HAVING clause filters?",
             "opts": ["Individual rows", "Grouped results", "Table columns", "Joins"], "ans": 1,
             "exp": "HAVING filters groups after GROUP BY."},
            {"q": "Which removes duplicate rows from results?",
             "opts": ["UNIQUE", "DISTINCT", "DIFFERENT", "FILTER"], "ans": 1,
             "exp": "SELECT DISTINCT removes duplicate rows."},
            {"q": "COALESCE() does what?",
             "opts": ["Joins strings", "Returns first non-NULL value",
                      "Rounds a number", "Converts type"], "ans": 1,
             "exp": "COALESCE(a,b,c) returns the first non-NULL argument."},
            {"q": "Which SQL clause sorts the result set?",
             "opts": ["GROUP BY", "HAVING", "ORDER BY", "WHERE"], "ans": 2,
             "exp": "ORDER BY sorts results; ASC/DESC specifies direction."},
            {"q": "What does the LIKE operator do?",
             "opts": ["Exact match", "Pattern matching", "Range filter", "NULL check"], "ans": 1,
             "exp": "LIKE enables pattern matching using % and _ wildcards."},
        ]
    },
}

LEADERBOARD = [
    {"rank":1,  "name":"Arjun Sharma",  "score":9850,"badge":"#1","solved":142,"streak":45,"tier":"Diamond"},
    {"rank":2,  "name":"Priya Singh",   "score":9420,"badge":"#2","solved":138,"streak":32,"tier":"Diamond"},
    {"rank":3,  "name":"Rahul Gupta",   "score":8990,"badge":"#3","solved":131,"streak":28,"tier":"Platinum"},
    {"rank":4,  "name":"Sneha Patel",   "score":8600,"badge":"#4","solved":125,"streak":21,"tier":"Platinum"},
    {"rank":5,  "name":"Vikram Joshi",  "score":8200,"badge":"#5","solved":119,"streak":17,"tier":"Gold"},
    {"rank":6,  "name":"Ananya Rao",    "score":7850,"badge":"#6","solved":112,"streak":14,"tier":"Gold"},
    {"rank":7,  "name":"Dev Malhotra",  "score":7400,"badge":"#7","solved":108,"streak":11,"tier":"Gold"},
    {"rank":8,  "name":"Kavya Nair",    "score":6950,"badge":"#8","solved":99, "streak":9, "tier":"Silver"},
    {"rank":9,  "name":"Ravi Kumar",    "score":6500,"badge":"#9","solved":93, "streak":7, "tier":"Silver"},
    {"rank":10, "name":"Meera Iyer",    "score":6100,"badge":"#10","solved":87,"streak":5, "tier":"Silver"},
    {"rank":11, "name":"Karan Mehta",   "score":5800,"badge":"#11","solved":82,"streak":4, "tier":"Bronze"},
    {"rank":12, "name":"Divya Reddy",   "score":5400,"badge":"#12","solved":76,"streak":3, "tier":"Bronze"},
    {"rank":13, "name":"Amir Khan",     "score":5100,"badge":"#13","solved":71,"streak":2, "tier":"Bronze"},
    {"rank":14, "name":"Pooja Verma",   "score":4700,"badge":"#14","solved":65,"streak":1, "tier":"Rookie"},
    {"rank":15, "name":"Suresh Babu",   "score":4300,"badge":"#15","solved":60,"streak":0, "tier":"Rookie"},
]

ACHIEVEMENTS = [
    {"name":"First Blood",    "desc":"Complete your first quiz",          "icon":"TGT","unlocked":True,  "pts":50},
    {"name":"Speed Demon",    "desc":"Finish a quiz in under 60 seconds", "icon":"ZAP","unlocked":True,  "pts":100},
    {"name":"Hat Trick",      "desc":"Score 100% three times in a row",   "icon":"HAT","unlocked":False, "pts":200},
    {"name":"Perfect Score",  "desc":"Get 100% on any topic quiz",        "icon":"GEM","unlocked":False, "pts":150},
    {"name":"Topic Conquer",  "desc":"Complete all 8 topics at least once","icon":"CUP","unlocked":False,"pts":500},
    {"name":"Streak Master",  "desc":"Maintain a 7-day study streak",     "icon":"FIR","unlocked":False, "pts":300},
    {"name":"Night Owl",      "desc":"Study between 11 PM and 2 AM",      "icon":"OWL","unlocked":False, "pts":75},
    {"name":"Comeback Kid",   "desc":"Score 80%+ after failing once",     "icon":"FLX","unlocked":True,  "pts":125},
    {"name":"Knowledge Pro",  "desc":"Solve 50 questions total",          "icon":"BKS","unlocked":False, "pts":200},
    {"name":"Quiz Marathon",  "desc":"Complete 10 quizzes in one day",    "icon":"RUN","unlocked":False, "pts":250},
    {"name":"Accuracy King",  "desc":"Maintain 90%+ accuracy overall",    "icon":"AIM","unlocked":False, "pts":350},
    {"name":"Early Bird",     "desc":"Study before 7 AM",                 "icon":"SUN","unlocked":False, "pts":75},
]

DAILY = [
    {"topic":"DSA",      "title":"Array Master Challenge",   "bonus":250,"tlimit":45},
    {"topic":"Python",   "title":"Python Puzzle Sprint",     "bonus":200,"tlimit":60},
    {"topic":"DBMS",     "title":"SQL Speed Run",            "bonus":175,"tlimit":50},
    {"topic":"Networks", "title":"Network Ninja Challenge",  "bonus":150,"tlimit":40},
    {"topic":"OS",       "title":"OS Concepts Blitz",        "bonus":225,"tlimit":55},
]

TIPS = [
    "Binary Search only works on SORTED arrays.",
    "Use a HashSet when you need O(1) lookup without duplicates.",
    "Always handle NULL in SQL with IS NULL, not = NULL.",
    "In OS, LRU is practical while OPT is theoretical-only.",
    "Python lists are mutable; tuples are immutable.",
    "TCP guarantees delivery; UDP prioritises speed.",
    "Normalization reduces redundancy in databases.",
    "virtual keyword in C++ enables runtime polymorphism.",
    "Java's final class cannot be extended (subclassed).",
    "Deadlock can be broken by preempting resources.",
    "Always analyse time AND space complexity together.",
    "In SQL, GROUP BY comes before HAVING but after WHERE.",
    "Stack overflow occurs when recursion depth exceeds the call stack size.",
    "A B-tree node can hold multiple keys — used in database indexing.",
    "Python's dict maintains insertion order since Python 3.7+.",
]

ROADMAPS = {
    "DSA": ["Arrays & Strings", "Linked Lists", "Stacks & Queues", "Trees & Graphs",
            "Sorting & Searching", "Dynamic Programming", "Greedy Algorithms", "Backtracking"],
    "DBMS": ["Relational Model", "SQL Basics", "Normalization", "Transactions & ACID",
             "Indexing", "Query Optimization", "NoSQL Basics", "Concurrency Control"],
    "OS":   ["Process Management", "CPU Scheduling", "Memory Management", "Virtual Memory",
             "File Systems", "Deadlocks", "I/O Management", "Security"],
    "Networks": ["OSI Model", "TCP/IP", "Routing Protocols", "DNS & DHCP",
                 "HTTP/HTTPS", "Network Security", "Wireless Networks", "Subnetting"],
}

# ═══════════════════════════════════════════════════════
#  ROBUST SCROLL FRAME  ← completely rewritten
# ═══════════════════════════════════════════════════════
class ScrollFrame(tk.Frame):
    """
    A frame that scrolls vertically.
    Put all child widgets inside  self.inner  — exactly as before.
    Mousewheel works on the canvas AND on every widget inside it.
    """
    def __init__(self, parent, bg=BG, **kw):
        super().__init__(parent, bg=bg, **kw)
        self.bg = bg

        # Canvas + scrollbar
        self._canvas = tk.Canvas(self, bg=bg, highlightthickness=0, bd=0)
        self._vsb    = tk.Scrollbar(self, orient="vertical",
                                    command=self._canvas.yview,
                                    troughcolor=SURF, relief="flat",
                                    width=8, bd=0)
        self._canvas.configure(yscrollcommand=self._vsb.set)

        self._vsb.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)

        # Inner frame lives inside the canvas
        self.inner = tk.Frame(self._canvas, bg=bg)
        self._win_id = self._canvas.create_window(
            (0, 0), window=self.inner, anchor="nw")

        # Resize callbacks
        self.inner.bind("<Configure>",  self._on_inner_configure)
        self._canvas.bind("<Configure>", self._on_canvas_configure)

        # Bind mousewheel on the canvas itself
        self._bind_mousewheel(self._canvas)

    # ── internal callbacks ──────────────────────────────
    def _on_inner_configure(self, _event=None):
        self._canvas.configure(
            scrollregion=self._canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self._canvas.itemconfig(self._win_id, width=event.width)

    def _scroll(self, event):
        # Windows / macOS send delta; Linux sends Button-4/5
        if event.num == 4:
            self._canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self._canvas.yview_scroll(1, "units")
        else:
            self._canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_mousewheel(self, widget):
        """Recursively bind mousewheel to widget and all its children."""
        widget.bind("<MouseWheel>", self._scroll, add="+")   # Windows / macOS
        widget.bind("<Button-4>",   self._scroll, add="+")   # Linux scroll up
        widget.bind("<Button-5>",   self._scroll, add="+")   # Linux scroll down
        for child in widget.winfo_children():
            self._bind_mousewheel(child)

    def bind_all_children(self):
        """
        Call this AFTER you have finished building all widgets in self.inner.
        It walks the entire subtree and attaches the scroll handler.
        """
        self._bind_mousewheel(self.inner)

    # Public helper kept for backward compatibility
    def bind_mousewheel(self, widget):
        self._bind_mousewheel(widget)


# ═══════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════
def lighter(hex_col, amt=22):
    try:
        h = hex_col.lstrip("#")
        r, g, b = int(h[:2],16), int(h[2:4],16), int(h[4:],16)
        return "#{:02x}{:02x}{:02x}".format(
            min(255,r+amt), min(255,g+amt), min(255,b+amt))
    except Exception:
        return hex_col

def mkbtn(parent, text, bg, fg=WHITE, size=11, bold=True, cmd=None, **kw):
    w = "bold" if bold else "normal"
    b = tk.Button(parent, text=text, bg=bg, fg=fg,
                  font=("Segoe UI", size, w),
                  relief="flat", cursor="hand2",
                  activebackground=lighter(bg),
                  activeforeground=fg,
                  command=cmd, **kw)
    b.bind("<Enter>", lambda e: b.config(bg=lighter(b.cget("bg"))))
    b.bind("<Leave>", lambda e: b.config(bg=bg))
    return b

def sec_title(parent, text, bg=BG):
    f = tk.Frame(parent, bg=bg)
    f.pack(fill="x", padx=28, pady=(22, 10))
    tk.Frame(f, bg=ORANGE, width=4).pack(side="left", fill="y", padx=(0,10))
    tk.Label(f, text=text, bg=bg, fg=TEXT,
             font=("Segoe UI",14,"bold")).pack(side="left")
    return f


# ═══════════════════════════════════════════════════════
#  MAIN APP
# ═══════════════════════════════════════════════════════
class QuizArena(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Arena  v2.1")
        self.configure(bg=BG)
        self.geometry("1366x768")
        self.minsize(1100, 680)
        try:
            self.state("zoomed")
        except Exception:
            pass

        self.user = {
            "name": "", "score": 0, "solved": 0,
            "correct": 0, "streak": 5, "quizzes": 0,
            "topic_scores": {t: {"solved":0,"correct":0} for t in TOPICS},
        }
        self._activities = []
        self._frame      = None
        self._pages      = {}
        self._nav_btns   = {}
        self.show_login()

    def _switch(self, frame):
        if self._frame:
            self._frame.destroy()
        self._frame = frame
        frame.pack(fill="both", expand=True)

    # ═══════════════════════════════════════════════════
    #  LOGIN
    # ═══════════════════════════════════════════════════
    def show_login(self):
        root = tk.Frame(self, bg=WHITE)
        self._switch(root)

        # Left hero canvas
        left_cv = tk.Canvas(root, bg="#08101C", highlightthickness=0, width=500)
        left_cv.pack(side="left", fill="y")

        def _draw(e=None):
            left_cv.delete("all")
            w = left_cv.winfo_width() or 500
            h = left_cv.winfo_height() or 800
            for x in range(24, w, 42):
                for y in range(24, h, 42):
                    left_cv.create_oval(x-2,y-2,x+2,y+2, fill="#1A2540", outline="")
            left_cv.create_rectangle(44,64,116,106, fill=ORANGE, outline="")
            left_cv.create_text(80,85, text="QA", font=("Segoe UI Black",18,"bold"), fill=WHITE)
            left_cv.create_text(132,85, text="Quiz Arena", font=("Segoe UI",16,"bold"), fill=WHITE, anchor="w")
            left_cv.create_text(44,158, text="Master CSE.", font=("Segoe UI Black",26,"bold"), fill=WHITE, anchor="w")
            left_cv.create_text(44,198, text="Climb the", font=("Segoe UI Black",26,"bold"), fill=WHITE, anchor="w")
            left_cv.create_text(44,238, text="Leaderboard.", font=("Segoe UI Black",26,"bold"), fill=ORANGE, anchor="w")
            left_cv.create_text(44,278, fill=TEXT2, anchor="w", width=w-60,
                                text="Practice DSA, DBMS, OS, Networks & more",
                                font=("Segoe UI",11))
            left_cv.create_text(44,298, fill=TEXT2, anchor="w",
                                text="with real competitive challenges.", font=("Segoe UI",11))
            sx = 44
            for val, lbl in [("800+","Questions"),("1.2K","Users"),(str(len(TOPICS)),"Topics")]:
                left_cv.create_rectangle(sx,330,sx+112,388, fill=SURF3, outline="")
                left_cv.create_text(sx+56,350, text=val, font=("Segoe UI Black",14,"bold"), fill=ORANGE)
                left_cv.create_text(sx+56,372, text=lbl, font=("Segoe UI",9), fill=TEXT2)
                sx += 120
            tags = ["#DSA","#DBMS","#OS","#CN","#Python","#C++","#Java","#SQL"]
            tx, ty = 44, 412
            for tag in tags:
                tw = len(tag)*9+18
                left_cv.create_rectangle(tx,ty,tx+tw,ty+26, fill=SURF3, outline="")
                left_cv.create_text(tx+tw//2,ty+13, text=tag, font=("Consolas",10,"bold"), fill=TEXT)
                tx += tw+8
                if tx > w-80: tx=44; ty+=34
            left_cv.create_text(w//2, h-38, text='"Code. Compete. Conquer."',
                                font=("Segoe UI",11,"italic"), fill=TEXT3)
            left_cv.create_rectangle(0,h-5,w,h, fill=ORANGE, outline="")

        left_cv.bind("<Configure>", _draw)
        self.after(80, _draw)

        # Right login panel
        right = tk.Frame(root, bg=WHITE)
        right.pack(side="right", fill="both", expand=True)

        form = tk.Frame(right, bg=WHITE)
        form.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(form, text="Sign in to", bg=WHITE, fg="#555555",
                 font=("Segoe UI",13)).grid(row=0, column=0, columnspan=2, sticky="w")
        tk.Label(form, text="Quiz Arena", bg=WHITE, fg="#0D1117",
                 font=("Segoe UI Black",30,"bold")).grid(row=1, column=0, columnspan=2, sticky="w")
        tk.Frame(form, bg=ORANGE, height=3, width=70).grid(
            row=2, column=0, columnspan=2, sticky="w", pady=(5,28))

        tk.Label(form, text="USERNAME", bg=WHITE, fg="#333333",
                 font=("Segoe UI",9,"bold")).grid(row=3, column=0, columnspan=2, sticky="w")
        self._uvar = tk.StringVar()
        ue = tk.Entry(form, textvariable=self._uvar, font=("Segoe UI",13),
                      bg=WHITE, fg="#0D1117", relief="solid", bd=2, width=30,
                      highlightthickness=2, highlightcolor=ORANGE,
                      highlightbackground="#CCCCCC", insertbackground="#0D1117")
        ue.grid(row=4, column=0, columnspan=2, sticky="ew", ipady=10, pady=(5,18))

        tk.Label(form, text="PASSWORD", bg=WHITE, fg="#333333",
                 font=("Segoe UI",9,"bold")).grid(row=5, column=0, columnspan=2, sticky="w")
        self._pvar = tk.StringVar()
        pe = tk.Entry(form, textvariable=self._pvar, show="*", font=("Segoe UI",13),
                      bg="#F5F5F5", fg="#0D1117", relief="solid", bd=2, width=30,
                      highlightthickness=2, highlightcolor=ORANGE,
                      highlightbackground="#CCCCCC", insertbackground="#0D1117")
        pe.grid(row=6, column=0, columnspan=2, sticky="ew", ipady=10, pady=(5,10))

        spv = tk.BooleanVar()
        tk.Checkbutton(form, text=" Show password", variable=spv, bg=WHITE, fg="#555555",
                       font=("Segoe UI",10), activebackground=WHITE,
                       command=lambda: pe.config(show="" if spv.get() else "*")
                       ).grid(row=7, column=0, sticky="w")
        fp = tk.Label(form, text="Forgot password?", bg=WHITE, fg=ORANGE,
                      font=("Segoe UI",10,"bold"), cursor="hand2")
        fp.grid(row=7, column=1, sticky="e")
        fp.bind("<Button-1>", lambda e: messagebox.showinfo(
            "Forgot Password", "A password reset link will be sent to your registered email."))

        def _login():
            u = self._uvar.get().strip()
            p = self._pvar.get().strip()
            if not u:
                messagebox.showerror("Login Failed", "Please enter your username.")
                ue.focus_set(); return
            if not p:
                messagebox.showerror("Login Failed", "Please enter your password.")
                pe.focus_set(); return
            self.user["name"] = u.title()
            self.show_main()

        sign_btn = tk.Button(form, text="Sign In  ->",
                             font=("Segoe UI",14,"bold"),
                             bg=ORANGE, fg=WHITE, relief="flat", bd=0,
                             activebackground=ORANGE2, activeforeground=WHITE,
                             cursor="hand2", command=_login)
        sign_btn.grid(row=8, column=0, columnspan=2, sticky="ew", ipady=13, pady=(20,0))
        sign_btn.bind("<Enter>", lambda e: sign_btn.config(bg=ORANGE2))
        sign_btn.bind("<Leave>", lambda e: sign_btn.config(bg=ORANGE))

        for entry in [ue, pe]:
            entry.bind("<Return>", lambda e: _login())

        tk.Frame(form, bg="#EEEEEE", height=1).grid(
            row=9, column=0, columnspan=2, sticky="ew", pady=22)

        ca_row = tk.Frame(form, bg=WHITE); ca_row.grid(row=10, column=0, columnspan=2)
        tk.Label(ca_row, text="New to Quiz Arena?  ", bg=WHITE, fg="#888888",
                 font=("Segoe UI",11)).pack(side="left")
        ca = tk.Label(ca_row, text="Create Account ->", bg=WHITE, fg=ORANGE,
                      font=("Segoe UI",11,"bold"), cursor="hand2")
        ca.pack(side="left")
        ca.bind("<Button-1>", lambda e: self._register_popup())

        tk.Label(form, text="By signing in you agree to our Terms of Service & Privacy Policy.",
                 bg=WHITE, fg="#AAAAAA",
                 font=("Segoe UI",9)).grid(row=11, column=0, columnspan=2, pady=(12,0))

        form.columnconfigure(0, weight=1)
        form.columnconfigure(1, weight=1)
        ue.focus_set()

    def _register_popup(self):
        pop = tk.Toplevel(self, bg=SURF)
        pop.title("Create Account — Quiz Arena")
        pop.geometry("440x480"); pop.grab_set(); pop.resizable(False,False)
        tk.Label(pop, text="Create Account", bg=SURF, fg=ORANGE,
                 font=("Segoe UI Black",18,"bold")).pack(pady=(28,4))
        tk.Label(pop, text="Join thousands of CSE students on Quiz Arena!",
                 bg=SURF, fg=TEXT2, font=("Segoe UI",11)).pack(pady=(0,20))
        entries = {}
        for field, show in [("Full Name",""),("Username",""),("Email",""),("Password","*")]:
            tk.Label(pop, text=field, bg=SURF, fg=TEXT2,
                     font=("Segoe UI",10)).pack(anchor="w", padx=44)
            e = tk.Entry(pop, bg=SURF2, fg=TEXT, show=show, font=("Segoe UI",12),
                         relief="flat", width=30, insertbackground=TEXT,
                         highlightthickness=1, highlightbackground=BORDER, highlightcolor=ORANGE)
            e.pack(ipady=8, padx=44, pady=(2,12)); entries[field]=e
        def _reg():
            if not entries["Username"].get().strip():
                messagebox.showerror("Error","Username is required.",parent=pop); return
            pop.destroy()
            messagebox.showinfo("Success","Account created! Please log in.",parent=self)
        mkbtn(pop,"Register",ORANGE,cmd=_reg,size=13,padx=0).pack(fill="x",padx=44,ipady=9,pady=4)

    # ═══════════════════════════════════════════════════
    #  MAIN LAYOUT
    # ═══════════════════════════════════════════════════
    def show_main(self):
        root = tk.Frame(self, bg=BG)
        self._switch(root)

        # ── Sidebar ──────────────────────────────────────
        sidebar = tk.Frame(root, bg=SURF, width=250)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        logo_bar = tk.Frame(sidebar, bg=ORANGE, height=60)
        logo_bar.pack(fill="x"); logo_bar.pack_propagate(False)
        logo_inner = tk.Frame(logo_bar, bg=ORANGE)
        logo_inner.place(x=14, rely=0.5, anchor="w")
        tk.Label(logo_inner, text=" QA ", bg=WHITE, fg=ORANGE,
                 font=("Segoe UI Black",12,"bold"), padx=4, pady=2).pack(side="left")
        tk.Label(logo_inner, text="  Quiz", bg=ORANGE, fg=WHITE,
                 font=("Segoe UI Black",14,"bold")).pack(side="left")
        tk.Label(logo_inner, text="Arena", bg=ORANGE, fg="#0D1117",
                 font=("Segoe UI Black",14,"bold")).pack(side="left")

        tk.Frame(sidebar, bg=BORDER, height=1).pack(fill="x")
        ucard = tk.Frame(sidebar, bg=SURF2, padx=14, pady=14, cursor="hand2")
        ucard.pack(fill="x", padx=10, pady=12)
        ucard.bind("<Button-1>", lambda e: self._nav_to("Profile"))

        initials = self.user["name"][:2].upper() if len(self.user["name"])>=2 else self.user["name"][:1].upper()
        tk.Label(ucard, text=initials, bg=ORANGE, fg=WHITE,
                 font=("Segoe UI Black",13,"bold"), width=4, height=2).pack(side="left",padx=(0,12))
        uinfo = tk.Frame(ucard, bg=SURF2); uinfo.pack(side="left",fill="both",expand=True)
        self._sb_name = tk.Label(uinfo, text=self.user["name"], bg=SURF2, fg=TEXT,
                                  font=("Segoe UI",11,"bold"), anchor="w")
        self._sb_name.pack(anchor="w")
        self._sb_score = tk.Label(uinfo,
                                   text=f"Score: 0  |  Streak: {self.user['streak']}",
                                   bg=SURF2, fg=TEXT2, font=("Segoe UI",9), anchor="w")
        self._sb_score.pack(anchor="w")

        NAV_ITEMS = [
            ("Dashboard",    "[=]",  "MAIN"),
            ("Topics",       "[T]",  None),
            ("Practice",     "[P]",  None),
            ("Daily",        "[!]",  None),
            ("Leaderboard",  "[L]",  "COMPETE"),
            ("Achievements", "[A]",  None),
            ("Roadmap",      "[R]",  None),
            ("Profile",      "[U]",  "ACCOUNT"),
            ("Settings",     "[S]",  None),
        ]
        self._nav_btns = {}
        for item in NAV_ITEMS:
            name, icon, section = item
            if section:
                tk.Label(sidebar, text=section, bg=SURF, fg=TEXT3,
                         font=("Segoe UI",8,"bold")).pack(anchor="w", padx=18, pady=(12,3))
            nb = tk.Button(sidebar, text=f"  {name}", bg=SURF, fg=TEXT2,
                           font=("Segoe UI",12), relief="flat", anchor="w",
                           padx=18, pady=11, cursor="hand2",
                           activebackground=SURF2, activeforeground=ORANGE,
                           command=lambda n=name: self._nav_to(n))
            nb.pack(fill="x")
            self._nav_btns[name] = nb

        tk.Frame(sidebar, bg=BORDER, height=1).pack(fill="x", pady=8)
        streak_card = tk.Frame(sidebar, bg=SURF2, padx=16, pady=14)
        streak_card.pack(fill="x", padx=10, pady=(0,10))
        tk.Label(streak_card, text="CURRENT STREAK", bg=SURF2, fg=TEXT2,
                 font=("Segoe UI",8,"bold")).pack(anchor="w")
        self._sb_streak = tk.Label(streak_card, text=str(self.user["streak"]),
                                    bg=SURF2, fg=ORANGE, font=("Segoe UI Black",32,"bold"))
        self._sb_streak.pack(anchor="w")
        tk.Label(streak_card, text="days in a row", bg=SURF2, fg=TEXT3,
                 font=("Segoe UI",9)).pack(anchor="w")

        tk.Button(sidebar, text="  Logout", bg=SURF, fg=RED, font=("Segoe UI",11),
                  relief="flat", anchor="w", padx=18, pady=10, cursor="hand2",
                  activebackground=SURF2, command=self._logout).pack(
                  fill="x", side="bottom", pady=4)

        # ── Content area ─────────────────────────────────
        self._content = tk.Frame(root, bg=BG)
        self._content.pack(side="right", fill="both", expand=True)

        self._pages = {}
        self._build_pages()
        self._nav_to("Dashboard")

    def _nav_to(self, name):
        for n, b in self._nav_btns.items():
            if n == name:
                b.config(bg=SURF3, fg=ORANGE, font=("Segoe UI",12,"bold"))
            else:
                b.config(bg=SURF, fg=TEXT2, font=("Segoe UI",12))
        for n, p in self._pages.items():
            if n == name:
                p.pack(fill="both", expand=True)
            else:
                p.pack_forget()

    def _build_pages(self):
        builders = {
            "Dashboard":    self._pg_dashboard,
            "Topics":       self._pg_topics,
            "Practice":     self._pg_practice,
            "Daily":        self._pg_daily,
            "Leaderboard":  self._pg_leaderboard,
            "Achievements": self._pg_achievements,
            "Roadmap":      self._pg_roadmap,
            "Profile":      self._pg_profile,
            "Settings":     self._pg_settings,
        }
        for name, builder in builders.items():
            f = tk.Frame(self._content, bg=BG)
            self._pages[name] = f
            builder(f)

    def _logout(self):
        if messagebox.askyesno("Logout","Are you sure you want to logout?"):
            self.show_login()

    def _refresh_sidebar(self):
        if hasattr(self,"_sb_name"):
            self._sb_name.config(text=self.user["name"])
        if hasattr(self,"_sb_score"):
            self._sb_score.config(
                text=f"Score: {self.user['score']}  |  Streak: {self.user['streak']}")
        if hasattr(self,"_sb_streak"):
            self._sb_streak.config(text=str(self.user["streak"]))

    # ═══════════════════════════════════════════════════
    #  HELPER — build a page with a fixed topbar + scrollable body
    # ═══════════════════════════════════════════════════
    def _make_scroll_page(self, parent, title, subtitle=""):
        """Returns (topbar_frame, scroll_inner_frame, scroll_frame_obj)."""
        topbar = tk.Frame(parent, bg=SURF, height=60)
        topbar.pack(fill="x"); topbar.pack_propagate(False)
        ltop = tk.Frame(topbar, bg=SURF); ltop.pack(side="left", padx=22, pady=10)
        tk.Label(ltop, text=f"  {title}", bg=SURF, fg=TEXT,
                 font=("Segoe UI",17,"bold")).pack(anchor="w")
        if subtitle:
            tk.Label(ltop, text=subtitle, bg=SURF, fg=TEXT2,
                     font=("Segoe UI",10)).pack(anchor="w")
        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x")
        sf = ScrollFrame(parent, bg=BG)
        sf.pack(fill="both", expand=True)
        return topbar, sf.inner, sf

    # ═══════════════════════════════════════════════════
    #  PAGE — DASHBOARD
    # ═══════════════════════════════════════════════════
    def _pg_dashboard(self, parent):
        # Fixed topbar (not part of scroll)
        topbar = tk.Frame(parent, bg=SURF, height=66)
        topbar.pack(fill="x"); topbar.pack_propagate(False)
        ltop = tk.Frame(topbar, bg=SURF); ltop.pack(side="left", padx=28, pady=10)
        self._greet = tk.Label(ltop, text=f"Welcome back, {self.user['name']}",
                                bg=SURF, fg=TEXT, font=("Segoe UI",17,"bold"))
        self._greet.pack(anchor="w")
        tk.Label(ltop, text=time.strftime("%A, %d %B %Y  |  Ready to level up?"),
                 bg=SURF, fg=TEXT2, font=("Segoe UI",10)).pack(anchor="w")
        rtop = tk.Frame(topbar, bg=SURF); rtop.pack(side="right", padx=20, pady=14)
        mkbtn(rtop,"  Daily Challenge", ORANGE, size=11,
              cmd=lambda: self._nav_to("Daily")).pack(side="right")
        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x")

        # ── Scrollable body ───────────────────────────────
        sf = ScrollFrame(parent, bg=BG)
        sf.pack(fill="both", expand=True)
        inn = sf.inner
        P = 28

        # HERO BANNER
        hero = tk.Frame(inn, bg=SURF3, padx=30, pady=24)
        hero.pack(fill="x", padx=P, pady=(20,0))
        hleft = tk.Frame(hero, bg=SURF3); hleft.pack(side="left",fill="both",expand=True)
        tk.Label(hleft, text=f"Master CSE, {self.user['name'].split()[0]}.",
                 bg=SURF3, fg=TEXT, font=("Segoe UI Black",20,"bold")).pack(anchor="w")
        tk.Label(hleft, text="Climb the Leaderboard.",
                 bg=SURF3, fg=ORANGE, font=("Segoe UI Black",20,"bold")).pack(anchor="w")
        tk.Label(hleft,
                 text="Practice DSA, DBMS, OS, Networks & more with real competitive challenges.",
                 bg=SURF3, fg=TEXT2, font=("Segoe UI",11), wraplength=500, justify="left"
                 ).pack(anchor="w", pady=(8,12))
        mkbtn(hleft,"  Start Learning Now  ->", ORANGE, size=12,
              cmd=lambda: self._nav_to("Topics"), padx=16, pady=8).pack(anchor="w")
        hright = tk.Frame(hero, bg=SURF3); hright.pack(side="right",padx=(20,0))
        rank_box = tk.Frame(hright, bg=SURF, padx=30, pady=16); rank_box.pack()
        tk.Label(rank_box, text="# --", bg=SURF, fg=ORANGE,
                 font=("Segoe UI Black",30,"bold")).pack()
        tk.Label(rank_box, text="GLOBAL RANK", bg=SURF, fg=TEXT3,
                 font=("Segoe UI",9,"bold")).pack()
        tk.Label(hright, text="Rookie Tier", bg=SURF3, fg=TEXT2,
                 font=("Segoe UI",10)).pack(pady=(8,0))

        # STAT CARDS
        sec_title(inn, "Your Stats at a Glance")
        stat_row = tk.Frame(inn, bg=BG)
        stat_row.pack(fill="x", padx=P)

        def acc():
            return round(self.user["correct"]/max(self.user["solved"],1)*100) if self.user["solved"] else 0

        cards_cfg = [
            ("Total Score",  lambda: str(self.user["score"]),                              ORANGE, "Points earned overall"),
            ("Quizzes Done", lambda: str(self.user["quizzes"]),                            GREEN,  "Total quizzes taken"),
            ("Accuracy",     lambda: f"{acc()}%",                                          BLUE,   "Correct vs attempted"),
            ("Day Streak",   lambda: str(self.user["streak"]),                             YELLOW, "Consecutive days active"),
            ("Solved",       lambda: str(self.user["solved"]),                             PURPLE, "Total questions answered"),
            ("Badges",       lambda: str(sum(a["unlocked"] for a in ACHIEVEMENTS)),       TEAL,   "Achievements unlocked"),
        ]
        for i,(title,vfn,accent,sub) in enumerate(cards_cfg):
            r, c = divmod(i, 3)
            stat_row.columnconfigure(c, weight=1)
            card = tk.Frame(stat_row, bg=SURF, padx=18, pady=18)
            card.grid(row=r, column=c, padx=6, pady=6, sticky="nsew")
            tk.Frame(card, bg=accent, width=4).pack(side="left",fill="y",padx=(0,14))
            rp = tk.Frame(card, bg=SURF); rp.pack(side="left",fill="both",expand=True)
            tk.Label(rp, text=vfn(), bg=SURF, fg=accent,
                     font=("Segoe UI Black",28,"bold")).pack(anchor="w")
            tk.Label(rp, text=title, bg=SURF, fg=TEXT2,
                     font=("Segoe UI",10,"bold")).pack(anchor="w")
            tk.Label(rp, text=sub, bg=SURF, fg=TEXT3,
                     font=("Segoe UI",9)).pack(anchor="w",pady=(2,0))

        # QUICK START
        sec_title(inn, "Quick Start — Choose a Topic")
        qs_grid = tk.Frame(inn, bg=BG); qs_grid.pack(fill="x",padx=P)
        for i,(tname,td) in enumerate(TOPICS.items()):
            r, c = divmod(i, 4)
            qs_grid.columnconfigure(c, weight=1)
            tb = tk.Button(qs_grid, text=f"  {tname}", bg=SURF, fg=TEXT,
                           font=("Segoe UI",12,"bold"), relief="flat", cursor="hand2",
                           padx=12, pady=22,
                           activebackground=td["color"], activeforeground=WHITE,
                           command=lambda n=tname: self._launch_quiz(n))
            tb.grid(row=r*2, column=c, padx=5, pady=(5,0), sticky="nsew")
            tk.Frame(qs_grid, bg=td["color"], height=3).grid(
                row=r*2+1, column=c, padx=5, pady=(0,5), sticky="ew")
            tb.bind("<Enter>", lambda e,b=tb,col=td["color"]: b.config(bg=col,fg=WHITE))
            tb.bind("<Leave>", lambda e,b=tb: b.config(bg=SURF,fg=TEXT))

        # PERFORMANCE BY TOPIC
        sec_title(inn, "Performance by Topic")
        perf = tk.Frame(inn, bg=SURF, padx=24, pady=20)
        perf.pack(fill="x", padx=P)
        for tname, td in TOPICS.items():
            ts  = self.user["topic_scores"][tname]
            pct = round(ts["correct"]/max(ts["solved"],1)*100) if ts["solved"] else 0
            row = tk.Frame(perf, bg=SURF); row.pack(fill="x",pady=5)
            tk.Label(row, text=tname, bg=SURF, fg=TEXT, font=("Segoe UI",10,"bold"),
                     width=14, anchor="w").pack(side="left")
            bwrap = tk.Frame(row, bg=SURF); bwrap.pack(side="left",fill="x",expand=True,padx=(12,16))
            bg_b  = tk.Frame(bwrap, bg=SURF3, height=10); bg_b.pack(fill="x")
            tk.Frame(bg_b, bg=td["color"], height=10).place(x=0,y=0,relheight=1,relwidth=pct/100)
            pcol = GREEN if pct>=70 else (YELLOW if pct>=40 else (RED if pct>0 else TEXT3))
            tk.Label(row, text=f"{pct}%", bg=SURF, fg=pcol,
                     font=("Consolas",10,"bold"), width=5, anchor="e").pack(side="right")
            tk.Label(row, text=f"{ts['solved']} q", bg=SURF, fg=TEXT3,
                     font=("Segoe UI",9), width=8, anchor="e").pack(side="right")

        # ACTIVITY + MINI LEADERBOARD
        sec_title(inn, "Recent Activity & Top Players")
        bot = tk.Frame(inn, bg=BG); bot.pack(fill="x",padx=P)

        act_outer = tk.Frame(bot, bg=SURF, padx=20, pady=18)
        act_outer.pack(side="left",fill="both",expand=True,padx=(0,10))
        tk.Label(act_outer, text="Recent Activity", bg=SURF, fg=TEXT,
                 font=("Segoe UI",12,"bold")).pack(anchor="w",pady=(0,10))
        self._act_frame = tk.Frame(act_outer, bg=SURF)
        self._act_frame.pack(fill="x")
        self._render_activity()

        lb_outer = tk.Frame(bot, bg=SURF, padx=18, pady=18, width=310)
        lb_outer.pack(side="right",fill="y")
        lb_outer.pack_propagate(False)
        tk.Label(lb_outer, text="Top Players", bg=SURF, fg=TEXT,
                 font=("Segoe UI",12,"bold")).pack(anchor="w",pady=(0,10))
        for e in LEADERBOARD[:8]:
            row = tk.Frame(lb_outer, bg=SURF2, padx=10, pady=8)
            row.pack(fill="x",pady=2)
            rc = ORANGE if e["rank"]<=3 else TEXT3
            tk.Label(row, text=f"#{e['rank']}", bg=SURF2, fg=rc,
                     font=("Segoe UI",10,"bold"), width=5, anchor="w").pack(side="left")
            tk.Label(row, text=e["name"].split()[0], bg=SURF2, fg=TEXT,
                     font=("Segoe UI",10)).pack(side="left",padx=6)
            tier_colors = {"Diamond":BLUE,"Platinum":PURPLE,"Gold":YELLOW,"Silver":TEXT2,"Bronze":"#CD7F32","Rookie":TEXT3}
            tc = tier_colors.get(e.get("tier",""),TEXT3)
            tk.Label(row, text=e.get("tier",""), bg=SURF2, fg=tc,
                     font=("Segoe UI",9), width=9).pack(side="right")
            tk.Label(row, text=str(e["score"]), bg=SURF2, fg=GREEN,
                     font=("Consolas",10,"bold")).pack(side="right")

        # DAILY TIP
        sec_title(inn, "Study Tip of the Day")
        tip_card = tk.Frame(inn, bg=SURF3, padx=24, pady=18)
        tip_card.pack(fill="x",padx=P)
        self._tip_var = tk.StringVar(value=random.choice(TIPS))
        tk.Label(tip_card, textvariable=self._tip_var, bg=SURF3, fg=TEXT,
                 font=("Segoe UI",12), wraplength=860, justify="left"
                 ).pack(side="left",fill="x",expand=True)
        mkbtn(tip_card,"New Tip",SURF,fg=ORANGE,size=10,
              cmd=lambda: self._tip_var.set(random.choice(TIPS))).pack(side="right")

        # ALL TOPICS OVERVIEW GRID
        sec_title(inn, "All Topics Overview")
        tov_grid = tk.Frame(inn, bg=BG); tov_grid.pack(fill="x",padx=P)
        for i,(tname,td) in enumerate(TOPICS.items()):
            r, c = divmod(i, 4)
            tov_grid.columnconfigure(c, weight=1)
            card = tk.Frame(tov_grid, bg=SURF, padx=14, pady=16)
            card.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
            tk.Frame(card, bg=td["color"], height=4).pack(fill="x",pady=(0,10))
            tk.Label(card, text=tname, bg=SURF, fg=TEXT,
                     font=("Segoe UI",12,"bold")).pack()
            tk.Label(card, text=f"{len(td['questions'])} Questions",
                     bg=SURF, fg=TEXT2, font=("Segoe UI",9)).pack(pady=(2,0))
            ts  = self.user["topic_scores"][tname]
            pct = round(ts["correct"]/max(ts["solved"],1)*100) if ts["solved"] else 0
            outer = tk.Frame(card, bg=SURF3, height=5); outer.pack(fill="x",pady=(8,8))
            tk.Frame(outer, bg=td["color"], height=5).place(x=0,y=0,relheight=1,relwidth=pct/100)
            mkbtn(card,"Start", td["color"], size=9,
                  cmd=lambda n=tname: self._launch_quiz(n), pady=4, padx=10).pack()

        # ACHIEVEMENTS PREVIEW
        sec_title(inn, "Achievements Preview")
        ach_row = tk.Frame(inn, bg=BG); ach_row.pack(fill="x",padx=P)
        for i,a in enumerate(ACHIEVEMENTS[:6]):
            r, c = divmod(i, 3)
            ach_row.columnconfigure(c, weight=1)
            locked = not a["unlocked"]
            ab     = SURF2 if locked else SURF
            card   = tk.Frame(ach_row, bg=ab, padx=16, pady=16)
            card.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
            ib = TEXT3 if locked else ORANGE
            tk.Label(card, text=a["name"], bg=ib, fg=WHITE,
                     font=("Segoe UI",11,"bold"), padx=6, pady=4).pack(anchor="w")
            tk.Label(card, text=a["desc"], bg=ab,
                     fg=TEXT2 if not locked else TEXT3,
                     font=("Segoe UI",9), wraplength=160).pack(anchor="w",pady=(6,2))
            tk.Label(card, text=f"+{a['pts']} pts", bg=ab,
                     fg=ORANGE if not locked else TEXT3,
                     font=("Consolas",10,"bold")).pack(anchor="w")
            tk.Label(card, text="Unlocked" if not locked else "Locked",
                     bg=ab, fg=GREEN if not locked else TEXT3,
                     font=("Segoe UI",9,"bold")).pack(anchor="w",pady=(4,0))

        # FOOTER
        tk.Frame(inn, bg=BORDER, height=1).pack(fill="x",padx=P,pady=(28,0))
        footer = tk.Frame(inn, bg=SURF, padx=P, pady=28)
        footer.pack(fill="x")
        cols = tk.Frame(footer, bg=SURF); cols.pack(fill="x")

        brand = tk.Frame(cols, bg=SURF); brand.pack(side="left",padx=(0,60),anchor="n")
        blogo = tk.Frame(brand, bg=SURF); blogo.pack(anchor="w")
        tk.Label(blogo, text=" QA ", bg=ORANGE, fg=WHITE,
                 font=("Segoe UI Black",12,"bold"), padx=4, pady=2).pack(side="left")
        tk.Label(blogo, text="  QuizArena", bg=SURF, fg=TEXT,
                 font=("Segoe UI Black",14,"bold")).pack(side="left")
        tk.Label(brand,
                 text="The premier platform for\nCSE students to practice\nand compete.",
                 bg=SURF, fg=TEXT2, font=("Segoe UI",10), justify="left"
                 ).pack(anchor="w",pady=(10,6))
        tk.Label(brand, text='"Code. Compete. Conquer."',
                 bg=SURF, fg=TEXT3, font=("Segoe UI",9,"italic")).pack(anchor="w")

        pl = tk.Frame(cols, bg=SURF); pl.pack(side="left",padx=(0,60),anchor="n")
        tk.Label(pl, text="Platform", bg=SURF, fg=TEXT,
                 font=("Segoe UI",11,"bold")).pack(anchor="w",pady=(0,10))
        for lnk in ["Dashboard","Topics","Practice","Daily Challenge","Leaderboard","Achievements","Roadmap"]:
            lb = tk.Label(pl, text=lnk, bg=SURF, fg=TEXT2, font=("Segoe UI",10), cursor="hand2")
            lb.pack(anchor="w",pady=2)
            lb.bind("<Enter>", lambda e,l=lb: l.config(fg=ORANGE))
            lb.bind("<Leave>", lambda e,l=lb: l.config(fg=TEXT2))

        tl = tk.Frame(cols, bg=SURF); tl.pack(side="left",padx=(0,60),anchor="n")
        tk.Label(tl, text="Topics", bg=SURF, fg=TEXT,
                 font=("Segoe UI",11,"bold")).pack(anchor="w",pady=(0,10))
        for t in TOPICS:
            lb = tk.Label(tl, text=t, bg=SURF, fg=TEXT2, font=("Segoe UI",10), cursor="hand2")
            lb.pack(anchor="w",pady=2)
            lb.bind("<Enter>", lambda e,l=lb: l.config(fg=ORANGE))
            lb.bind("<Leave>", lambda e,l=lb: l.config(fg=TEXT2))

        ab = tk.Frame(cols, bg=SURF); ab.pack(side="left",anchor="n")
        tk.Label(ab, text="About Quiz Arena", bg=SURF, fg=TEXT,
                 font=("Segoe UI",11,"bold")).pack(anchor="w",pady=(0,10))
        for fact in ["Built for CSE Students","8 Technical Topics","800+ Practice Questions",
                     "Real Competitive Rankings","Instant Score and Feedback",
                     "Daily Challenges","Achievement Badges","100% Free to Use"]:
            row = tk.Frame(ab, bg=SURF); row.pack(anchor="w",pady=2)
            tk.Label(row, text="  >  ", bg=SURF, fg=ORANGE, font=("Segoe UI",10)).pack(side="left")
            tk.Label(row, text=fact, bg=SURF, fg=TEXT2, font=("Segoe UI",10)).pack(side="left")

        tk.Frame(footer, bg=BORDER, height=1).pack(fill="x",pady=(22,14))
        bot_bar = tk.Frame(footer, bg=SURF); bot_bar.pack(fill="x")
        yr = time.strftime("%Y")
        tk.Label(bot_bar,
                 text=f"© {yr} Quiz Arena  |  All Rights Reserved  |  Made with love for CSE Students",
                 bg=SURF, fg=TEXT3, font=("Segoe UI",9)).pack(side="left")
        tk.Label(bot_bar, text="v2.1  |  Python + Tkinter",
                 bg=SURF, fg=TEXT3, font=("Consolas",9)).pack(side="right")

        tk.Frame(inn, bg=BG, height=20).pack()

        # ── Bind scroll on ALL children after build ───────
        sf.bind_all_children()

    def _render_activity(self):
        for w in self._act_frame.winfo_children():
            w.destroy()
        if not self._activities:
            tk.Label(self._act_frame,
                     text="No activity yet — start a quiz to see your results here!",
                     bg=SURF, fg=TEXT3, font=("Segoe UI",10,"italic")).pack(anchor="w")
        else:
            for act in self._activities[-6:][::-1]:
                row = tk.Frame(self._act_frame, bg=SURF2, padx=14, pady=9)
                row.pack(fill="x",pady=3)
                dot_col = GREEN if act["pct"]>=60 else (YELLOW if act["pct"]>=40 else RED)
                tk.Frame(row, bg=dot_col, width=6, height=6).pack(
                    side="left",padx=(0,10),pady=2,anchor="center")
                tk.Label(row, text=act["title"], bg=SURF2, fg=TEXT,
                         font=("Segoe UI",11,"bold")).pack(side="left")
                tk.Label(row, text=act["when"], bg=SURF2, fg=TEXT3,
                         font=("Segoe UI",9)).pack(side="right")
                col_s = GREEN if act["pct"]>=60 else (YELLOW if act["pct"]>=40 else RED)
                tk.Label(row, text=f"Score: {act['pct']}%", bg=SURF2, fg=col_s,
                         font=("Segoe UI",10,"bold")).pack(side="right",padx=16)

    # ═══════════════════════════════════════════════════
    #  PAGE — TOPICS
    # ═══════════════════════════════════════════════════
    def _pg_topics(self, parent):
        _, inn, sf = self._make_scroll_page(
            parent, "All Topics", f"{len(TOPICS)} Topics Available")
        grid = tk.Frame(inn, bg=BG); grid.pack(fill="x",padx=28,pady=20)
        for i,(tname,td) in enumerate(TOPICS.items()):
            r, c = divmod(i, 2)
            grid.columnconfigure(c, weight=1)
            card = tk.Frame(grid, bg=SURF, padx=24, pady=22)
            card.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
            ts  = self.user["topic_scores"][tname]
            pct = round(ts["correct"]/max(ts["solved"],1)*100) if ts["solved"] else 0
            tk.Frame(card, bg=td["color"], height=4).pack(fill="x",pady=(0,14))
            top = tk.Frame(card, bg=SURF); top.pack(fill="x")
            tk.Label(top, text=td["icon"], bg=td["color"], fg=WHITE,
                     font=("Segoe UI",14,"bold"), width=5, height=1
                     ).pack(side="left",padx=(0,16))
            info = tk.Frame(top, bg=SURF); info.pack(side="left",fill="both",expand=True)
            tk.Label(info, text=tname, bg=SURF, fg=TEXT,
                     font=("Segoe UI",15,"bold")).pack(anchor="w")
            tk.Label(info, text=td["desc"], bg=SURF, fg=TEXT2,
                     font=("Segoe UI",10)).pack(anchor="w")
            tk.Label(top, text=f"{len(td['questions'])} Qs",
                     bg=SURF3, fg=TEXT2, font=("Consolas",9,"bold"), padx=8, pady=3
                     ).pack(side="right",anchor="n")
            tk.Frame(card, bg=BORDER, height=1).pack(fill="x",pady=14)
            tk.Label(card, text=f"Progress: {pct}%  ({ts['solved']} questions solved)",
                     bg=SURF, fg=TEXT2, font=("Segoe UI",9)).pack(anchor="w")
            bg_b = tk.Frame(card, bg=SURF3, height=8); bg_b.pack(fill="x",pady=(4,14))
            tk.Frame(bg_b, bg=td["color"], height=8).place(x=0,y=0,relheight=1,relwidth=pct/100)
            btns = tk.Frame(card, bg=SURF); btns.pack(fill="x")
            mkbtn(btns,"Start Quiz",td["color"],
                  cmd=lambda n=tname: self._launch_quiz(n),
                  size=11,padx=20,pady=7).pack(side="left",padx=(0,8))
            mkbtn(btns,"Practice Mode",SURF2,fg=TEXT2,
                  cmd=lambda n=tname: self._launch_quiz(n,practice=True),
                  size=11,padx=14,pady=7).pack(side="left")
        tk.Frame(inn, bg=BG, height=20).pack()
        sf.bind_all_children()

    # ═══════════════════════════════════════════════════
    #  PAGE — PRACTICE
    # ═══════════════════════════════════════════════════
    def _pg_practice(self, parent):
        _, inn, sf = self._make_scroll_page(parent, "Practice Sets")
        tk.Label(inn, text="Choose a practice mode:",
                 bg=BG, fg=TEXT, font=("Segoe UI",13,"bold")).pack(anchor="w",padx=28,pady=(20,4))
        tk.Label(inn, text="Practice sets are untimed — perfect for learning without pressure.",
                 bg=BG, fg=TEXT2, font=("Segoe UI",10)).pack(anchor="w",padx=28,pady=(0,18))

        modes = [
            ("Topic-Specific","Select one topic and drill all questions.",ORANGE,None),
            ("Mixed Bag","Random questions from ALL topics.",PURPLE,"mixed"),
            ("Weak Areas","Focus on your lowest-accuracy topic.",RED,"weak"),
        ]
        mrow = tk.Frame(inn, bg=BG); mrow.pack(fill="x",padx=28,pady=(0,20))
        for i,(title,desc,col,mode) in enumerate(modes):
            mrow.columnconfigure(i, weight=1)
            mc = tk.Frame(mrow, bg=SURF, padx=20, pady=20)
            mc.grid(row=0,column=i,padx=8,sticky="nsew")
            tk.Frame(mc, bg=col, height=4).pack(fill="x",pady=(0,12))
            tk.Label(mc, text=title, bg=SURF, fg=col,
                     font=("Segoe UI",13,"bold")).pack(anchor="w")
            tk.Label(mc, text=desc, bg=SURF, fg=TEXT2, font=("Segoe UI",10),
                     wraplength=200, justify="left").pack(anchor="w",pady=(6,14))
            mkbtn(mc,"Start",col,cmd=lambda m=mode: self._launch_practice(m),
                  size=11,padx=18,pady=7).pack(anchor="w")

        sec_title(inn, "Practice by Topic")
        for tname, td in TOPICS.items():
            ts  = self.user["topic_scores"][tname]
            pct = round(ts["correct"]/max(ts["solved"],1)*100) if ts["solved"] else 0
            row = tk.Frame(inn, bg=SURF, padx=20, pady=13)
            row.pack(fill="x",padx=28,pady=4)
            tk.Label(row, text=tname, bg=SURF, fg=TEXT,
                     font=("Segoe UI",12,"bold"), width=14, anchor="w").pack(side="left")
            tk.Label(row, text=td["desc"], bg=SURF, fg=TEXT2,
                     font=("Segoe UI",10)).pack(side="left",padx=12)
            tk.Label(row, text=f"{pct}% done", bg=SURF,
                     fg=GREEN if pct>=70 else (YELLOW if pct>0 else TEXT3),
                     font=("Consolas",10,"bold")).pack(side="right",padx=14)
            mkbtn(row,"Practice",SURF3,fg=ORANGE,
                  cmd=lambda n=tname: self._launch_quiz(n,practice=True),
                  size=10,padx=14,pady=5).pack(side="right")
        tk.Frame(inn, bg=BG, height=20).pack()
        sf.bind_all_children()

    def _launch_practice(self, mode):
        if mode == "mixed":
            all_qs = []
            for tname, td in TOPICS.items():
                for q in td["questions"]:
                    all_qs.append({**q,"_topic":tname})
            random.shuffle(all_qs)
            self._launch_quiz_custom("Mixed Bag", PURPLE, all_qs[:10])
        elif mode == "weak":
            best = min(TOPICS.keys(),
                       key=lambda t: (self.user["topic_scores"][t]["correct"] /
                                      max(self.user["topic_scores"][t]["solved"],1)))
            messagebox.showinfo("Weak Area",
                                f"Your weakest topic is: {best}!\nLaunching practice mode…")
            self._launch_quiz(best, practice=True)
        else:
            self._nav_to("Topics")

    # ═══════════════════════════════════════════════════
    #  PAGE — DAILY
    # ═══════════════════════════════════════════════════
    def _pg_daily(self, parent):
        topbar, inn, sf = self._make_scroll_page(parent, "Daily Challenge")
        # add right label to topbar
        tk.Label(topbar, text="Bonus Points  |  Resets Daily",
                 bg=SURF, fg=ORANGE, font=("Segoe UI",10,"bold")).pack(side="right",padx=22)

        tk.Label(inn, text="Today's Challenges",
                 bg=BG, fg=TEXT, font=("Segoe UI",15,"bold")).pack(anchor="w",padx=40,pady=(20,6))
        tk.Label(inn,
                 text="Complete daily challenges to earn bonus points and maintain your streak!",
                 bg=BG, fg=TEXT2, font=("Segoe UI",10)).pack(anchor="w",padx=40,pady=(0,22))

        for ch in DAILY:
            td = TOPICS[ch["topic"]]
            card = tk.Frame(inn, bg=SURF, padx=24, pady=20)
            card.pack(fill="x",padx=40,pady=8)
            tk.Frame(card, bg=td["color"], height=4).pack(fill="x",pady=(0,14))
            lc = tk.Frame(card, bg=SURF); lc.pack(side="left",fill="both",expand=True)
            tk.Label(lc, text=ch["title"], bg=SURF, fg=TEXT,
                     font=("Segoe UI",14,"bold")).pack(anchor="w")
            tk.Label(lc, text=f"Topic: {ch['topic']}  |  Time: {ch['tlimit']}s per question",
                     bg=SURF, fg=TEXT2, font=("Segoe UI",10)).pack(anchor="w",pady=(4,0))
            tk.Label(lc, text=f"{len(td['questions'])} questions  |  Mixed Difficulty",
                     bg=SURF, fg=TEXT3, font=("Segoe UI",9)).pack(anchor="w",pady=(2,0))
            rc = tk.Frame(card, bg=SURF); rc.pack(side="right",padx=(20,0))
            tk.Label(rc, text=f"+{ch['bonus']} pts", bg=SURF, fg=ORANGE,
                     font=("Segoe UI Black",20,"bold")).pack(anchor="e")
            tk.Label(rc, text="BONUS REWARD", bg=SURF, fg=TEXT3,
                     font=("Segoe UI",9)).pack(anchor="e")
            mkbtn(rc,"Start Challenge",td["color"],
                  cmd=lambda n=ch["topic"],b=ch["bonus"]: self._launch_quiz(n,bonus=b),
                  size=11,padx=20,pady=8).pack(anchor="e",pady=(10,0))

        sec_title(inn, "Why Daily Challenges?")
        why = tk.Frame(inn, bg=SURF, padx=28, pady=20)
        why.pack(fill="x",padx=40,pady=(0,20))
        reasons = [
            ("Consistency", "Regular practice builds long-term memory retention."),
            ("Bonus Points", "Daily challenges give extra points not earned in normal quizzes."),
            ("Streak Rewards","Maintaining your streak unlocks special achievements."),
            ("Curated Content","Questions are hand-picked to cover key exam concepts."),
        ]
        for i,(ttl,desc) in enumerate(reasons):
            r, c = divmod(i, 2)
            why.columnconfigure(c, weight=1)
            cell = tk.Frame(why, bg=SURF2, padx=16, pady=14)
            cell.grid(row=r,column=c,padx=6,pady=6,sticky="nsew")
            tk.Label(cell, text=ttl, bg=SURF2, fg=ORANGE,
                     font=("Segoe UI",11,"bold")).pack(anchor="w")
            tk.Label(cell, text=desc, bg=SURF2, fg=TEXT2, font=("Segoe UI",10),
                     wraplength=260, justify="left").pack(anchor="w",pady=(4,0))

        tk.Frame(inn, bg=BG, height=20).pack()
        sf.bind_all_children()

    # ═══════════════════════════════════════════════════
    #  PAGE — LEADERBOARD
    # ═══════════════════════════════════════════════════
    def _pg_leaderboard(self, parent):
        _, inn, sf = self._make_scroll_page(parent, "Leaderboard")

        # Podium
        pod = tk.Frame(inn, bg=BG); pod.pack(pady=22)
        order   = [LEADERBOARD[1], LEADERBOARD[0], LEADERBOARD[2]]
        heights = [90, 120, 68]
        colors  = ["#C0C0C0","#FFD700","#CD7F32"]
        for entry, ht, col in zip(order, heights, colors):
            cf = tk.Frame(pod, bg=BG); cf.pack(side="left",padx=22,anchor="s")
            tk.Label(cf, text=entry["badge"], bg=BG, fg=col,
                     font=("Segoe UI Black",16,"bold")).pack()
            tk.Label(cf, text=entry["name"].split()[0], bg=BG, fg=TEXT,
                     font=("Segoe UI",11,"bold")).pack()
            tk.Label(cf, text=str(entry["score"]), bg=BG, fg=col,
                     font=("Segoe UI Black",13,"bold")).pack()
            tk.Frame(cf, bg=col, width=100, height=ht).pack()

        # Table
        table = tk.Frame(inn, bg=BG); table.pack(fill="x",padx=28,pady=(8,20))
        hrow = tk.Frame(table, bg=SURF3); hrow.pack(fill="x")
        for h_text, w in [("Rank",6),("Player",20),("Score",10),
                           ("Solved",8),("Streak",8),("Tier",10)]:
            tk.Label(hrow, text=h_text, bg=SURF3, fg=TEXT2,
                     font=("Segoe UI",10,"bold"), width=w,
                     anchor="center").pack(side="left",padx=4,pady=10)

        user_entry = {
            "rank": len(LEADERBOARD)+1,
            "name": self.user["name"],
            "score": self.user["score"],
            "badge":"NEW","solved":self.user["solved"],
            "streak":self.user["streak"],"tier":"Rookie",
        }
        all_e = LEADERBOARD + [user_entry]
        all_e.sort(key=lambda e: -e["score"])
        for i,e in enumerate(all_e): e["rank"]=i+1

        for e in all_e:
            is_me = (e["name"]==self.user["name"])
            bg_r  = SURF3 if is_me else (SURF if e["rank"]%2==0 else SURF2)
            row   = tk.Frame(table, bg=bg_r); row.pack(fill="x")
            rc    = ORANGE if e["rank"]<=3 else (BLUE if is_me else TEXT2)
            tk.Label(row, text=f"#{e['rank']}", bg=bg_r, fg=rc,
                     font=("Segoe UI",11,"bold"), width=6, anchor="center"
                     ).pack(side="left",padx=4,pady=9)
            nm = e["name"] + ("  <- You" if is_me else "")
            tk.Label(row, text=nm, bg=bg_r, fg=ORANGE if is_me else TEXT,
                     font=("Segoe UI",11,"bold" if is_me else "normal"),
                     width=20, anchor="w").pack(side="left",padx=4)
            tk.Label(row, text=str(e["score"]), bg=bg_r, fg=GREEN,
                     font=("Consolas",11,"bold"), width=10, anchor="center"
                     ).pack(side="left",padx=4)
            tk.Label(row, text=str(e["solved"]), bg=bg_r, fg=TEXT,
                     font=("Segoe UI",11), width=8, anchor="center").pack(side="left",padx=4)
            tk.Label(row, text=str(e["streak"]), bg=bg_r, fg=YELLOW,
                     font=("Segoe UI",10), width=8, anchor="center").pack(side="left",padx=4)
            tier_colors = {"Diamond":BLUE,"Platinum":PURPLE,"Gold":YELLOW,
                           "Silver":TEXT2,"Bronze":"#CD7F32","Rookie":TEXT3}
            tier_col = tier_colors.get(e.get("tier",""), TEXT3)
            tk.Label(row, text=e.get("tier","--"), bg=bg_r, fg=tier_col,
                     font=("Segoe UI",10,"bold"), width=10, anchor="center"
                     ).pack(side="left",padx=4)

        tk.Frame(inn, bg=BG, height=20).pack()
        sf.bind_all_children()

    # ═══════════════════════════════════════════════════
    #  PAGE — ACHIEVEMENTS
    # ═══════════════════════════════════════════════════
    def _pg_achievements(self, parent):
        unlocked_n = sum(1 for a in ACHIEVEMENTS if a["unlocked"])
        _, inn, sf = self._make_scroll_page(
            parent, "Achievements", f"{unlocked_n}/{len(ACHIEVEMENTS)} Unlocked")

        grid = tk.Frame(inn, bg=BG); grid.pack(fill="x",padx=28,pady=20)
        for i,ach in enumerate(ACHIEVEMENTS):
            r, c = divmod(i, 3)
            grid.columnconfigure(c, weight=1)
            locked = not ach["unlocked"]
            cb     = SURF2 if locked else SURF
            card   = tk.Frame(grid, bg=cb, padx=20, pady=22)
            card.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
            ib = TEXT3 if locked else ORANGE
            tk.Label(card, text=ach["name"], bg=ib, fg=WHITE,
                     font=("Segoe UI",11,"bold"), padx=8, pady=6).pack()
            tk.Label(card, text=ach["desc"], bg=cb,
                     fg=TEXT2 if not locked else TEXT3,
                     font=("Segoe UI",10), wraplength=170).pack(pady=(10,3))
            tk.Label(card, text=f"+{ach['pts']} pts", bg=cb,
                     fg=ORANGE if not locked else TEXT3,
                     font=("Consolas",10,"bold")).pack(pady=(6,2))
            st = "Unlocked" if not locked else "Locked"
            tk.Label(card, text=st, bg=cb, fg=GREEN if not locked else TEXT3,
                     font=("Segoe UI",10,"bold")).pack(pady=(4,0))

        # How to earn more
        sec_title(inn, "How to Earn More Achievements")
        hints_frame = tk.Frame(inn, bg=SURF, padx=24, pady=20)
        hints_frame.pack(fill="x",padx=28,pady=(0,20))
        hints = [
            ("Complete quizzes regularly", "Each quiz attempt counts towards multiple achievements."),
            ("Aim for 100% scores",        "Perfect scores unlock exclusive badges and bonus points."),
            ("Keep your daily streak",      "Log in and practice every day without missing a session."),
            ("Try all 8 topics",           "Topic Conquer badge requires you to clear every subject."),
        ]
        for ttl, desc in hints:
            row = tk.Frame(hints_frame, bg=SURF2, padx=16, pady=12)
            row.pack(fill="x",pady=4)
            tk.Label(row, text=ttl, bg=SURF2, fg=ORANGE,
                     font=("Segoe UI",11,"bold")).pack(anchor="w")
            tk.Label(row, text=desc, bg=SURF2, fg=TEXT2,
                     font=("Segoe UI",10)).pack(anchor="w")

        tk.Frame(inn, bg=BG, height=20).pack()
        sf.bind_all_children()

    # ═══════════════════════════════════════════════════
    #  PAGE — ROADMAP  (new page)
    # ═══════════════════════════════════════════════════
    def _pg_roadmap(self, parent):
        _, inn, sf = self._make_scroll_page(
            parent, "Learning Roadmap", "Structured path to master CSE topics")

        tk.Label(inn,
                 text="Follow these curated roadmaps to systematically build your knowledge in each subject.",
                 bg=BG, fg=TEXT2, font=("Segoe UI",11)).pack(anchor="w",padx=28,pady=(16,20))

        for tname, steps in ROADMAPS.items():
            td = TOPICS[tname]
            sec_title(inn, f"{tname} — {td['desc']}")
            rcard = tk.Frame(inn, bg=SURF, padx=24, pady=18)
            rcard.pack(fill="x",padx=28,pady=(0,6))
            for i, step in enumerate(steps):
                srow = tk.Frame(rcard, bg=SURF2, padx=16, pady=12)
                srow.pack(fill="x",pady=4)
                # step number badge
                tk.Label(srow, text=f"Step {i+1}", bg=td["color"], fg=WHITE,
                         font=("Segoe UI",9,"bold"), padx=8, pady=4
                         ).pack(side="left",padx=(0,14))
                tk.Label(srow, text=step, bg=SURF2, fg=TEXT,
                         font=("Segoe UI",11)).pack(side="left")
                status = "Done" if i < 2 else ("In Progress" if i==2 else "Locked")
                sc     = GREEN if status=="Done" else (YELLOW if status=="In Progress" else TEXT3)
                tk.Label(srow, text=status, bg=SURF2, fg=sc,
                         font=("Segoe UI",9,"bold")).pack(side="right")
            mkbtn(rcard, f"Start {tname} Quiz", td["color"],
                  cmd=lambda n=tname: self._launch_quiz(n),
                  size=11, padx=18, pady=7).pack(anchor="w",pady=(12,0))

        tk.Frame(inn, bg=BG, height=20).pack()
        sf.bind_all_children()

    # ═══════════════════════════════════════════════════
    #  PAGE — PROFILE
    # ═══════════════════════════════════════════════════
    def _pg_profile(self, parent):
        sf = ScrollFrame(parent, bg=BG)
        sf.pack(fill="both", expand=True)
        inn = sf.inner

        # Banner
        banner = tk.Frame(inn, bg=SURF3, height=120)
        banner.pack(fill="x"); banner.pack_propagate(False)
        tk.Frame(banner, bg=ORANGE, height=4).place(x=0,rely=1.0,relwidth=1,y=-4)

        irow = tk.Frame(inn, bg=BG, pady=14, padx=36); irow.pack(fill="x")
        initials = self.user["name"][:2].upper() if len(self.user["name"])>=2 else self.user["name"][:1].upper()
        tk.Label(irow, text=initials, bg=ORANGE, fg=WHITE,
                 font=("Segoe UI Black",26,"bold"), width=4, height=2).pack(side="left",padx=(0,20))
        ninfo = tk.Frame(irow, bg=BG); ninfo.pack(side="left")
        tk.Label(ninfo, text=self.user["name"], bg=BG, fg=TEXT,
                 font=("Segoe UI",22,"bold")).pack(anchor="w")
        tk.Label(ninfo, text="@"+self.user["name"].lower().replace(" ","_"),
                 bg=BG, fg=TEXT2, font=("Consolas",11)).pack(anchor="w")
        tk.Label(ninfo,
                 text=f"Joined {time.strftime('%B %Y')}  |  Rookie Tier  |  {self.user['streak']} Day Streak",
                 bg=BG, fg=TEXT3, font=("Segoe UI",10)).pack(anchor="w",pady=4)
        mkbtn(irow,"Edit Profile",SURF2,fg=ORANGE,
              cmd=self._edit_profile_popup).pack(side="right")

        tk.Frame(inn, bg=BORDER, height=1).pack(fill="x",padx=36,pady=10)
        acc = round(self.user["correct"]/max(self.user["solved"],1)*100) if self.user["solved"] else 0
        srow = tk.Frame(inn, bg=BG); srow.pack(fill="x",padx=36)
        for lbl, val, col in [
            ("Total Score", str(self.user["score"]), ORANGE),
            ("Quizzes",     str(self.user["quizzes"]), GREEN),
            ("Questions",   str(self.user["solved"]), BLUE),
            ("Accuracy",    f"{acc}%", YELLOW),
        ]:
            box = tk.Frame(srow, bg=SURF, padx=22, pady=16)
            box.pack(side="left",expand=True,fill="both",padx=8)
            tk.Label(box, text=val, bg=SURF, fg=col,
                     font=("Segoe UI Black",22,"bold")).pack()
            tk.Label(box, text=lbl, bg=SURF, fg=TEXT2, font=("Segoe UI",10)).pack()

        tk.Frame(inn, bg=BORDER, height=1).pack(fill="x",padx=36,pady=16)
        sec_title(inn, "Topic Progress")
        for tname, td in TOPICS.items():
            ts  = self.user["topic_scores"][tname]
            pct = round(ts["correct"]/max(ts["solved"],1)*100) if ts["solved"] else 0
            row = tk.Frame(inn, bg=SURF, padx=20, pady=12)
            row.pack(fill="x",padx=36,pady=4)
            tk.Label(row, text=tname, bg=SURF, fg=TEXT, font=("Segoe UI",11,"bold"),
                     width=14, anchor="w").pack(side="left")
            wrap = tk.Frame(row, bg=SURF); wrap.pack(side="left",fill="x",expand=True,padx=12)
            bb = tk.Frame(wrap, bg=SURF3, height=9); bb.pack(fill="x")
            tk.Frame(bb, bg=td["color"], height=9).place(x=0,y=0,relheight=1,relwidth=pct/100)
            tk.Label(row, text=f"{ts['solved']} solved  |  {pct}%",
                     bg=SURF, fg=TEXT2, font=("Consolas",9), width=22, anchor="e").pack(side="right")

        tk.Frame(inn, bg=BORDER, height=1).pack(fill="x",padx=36,pady=16)
        sec_title(inn, "Badges Earned")
        brow = tk.Frame(inn, bg=BG); brow.pack(fill="x",padx=36,pady=(0,24))
        unlocked_ach = [a for a in ACHIEVEMENTS if a["unlocked"]]
        if not unlocked_ach:
            tk.Label(brow, text="No badges yet — start taking quizzes!",
                     bg=BG, fg=TEXT3, font=("Segoe UI",10,"italic")).pack(anchor="w")
        for a in unlocked_ach:
            b = tk.Frame(brow, bg=SURF, padx=14, pady=14)
            b.pack(side="left",padx=6)
            tk.Label(b, text=a["name"], bg=ORANGE, fg=WHITE,
                     font=("Segoe UI",9,"bold"), padx=6, pady=4).pack()
            tk.Label(b, text=f"+{a['pts']} pts", bg=SURF, fg=ORANGE,
                     font=("Consolas",9)).pack(pady=(4,0))

        tk.Frame(inn, bg=BG, height=20).pack()
        sf.bind_all_children()

    def _edit_profile_popup(self):
        pop = tk.Toplevel(self, bg=SURF)
        pop.title("Edit Profile"); pop.geometry("420x360")
        pop.grab_set(); pop.resizable(False,False)
        tk.Label(pop, text="Edit Profile", bg=SURF, fg=ORANGE,
                 font=("Segoe UI Black",16,"bold")).pack(pady=(24,16))
        entries = {}
        for field, default in [("Display Name",self.user["name"]),
                                ("Email","user@quizarena.in"),
                                ("Bio","CSE Student | Quiz Enthusiast")]:
            tk.Label(pop, text=field, bg=SURF, fg=TEXT2, font=("Segoe UI",10)).pack(anchor="w",padx=40)
            e = tk.Entry(pop, bg=SURF2, fg=TEXT, font=("Segoe UI",12),
                         relief="flat", width=32, insertbackground=TEXT,
                         highlightthickness=1, highlightbackground=BORDER, highlightcolor=ORANGE)
            e.insert(0, default); e.pack(ipady=8,padx=40,pady=(2,12)); entries[field]=e
        def _save():
            nn = entries["Display Name"].get().strip()
            if nn:
                self.user["name"] = nn.title()
                self._refresh_sidebar()
            pop.destroy()
            messagebox.showinfo("Saved","Profile updated successfully!")
        mkbtn(pop,"Save Changes",ORANGE,cmd=_save,size=12,padx=0
              ).pack(fill="x",padx=40,ipady=9)

    # ═══════════════════════════════════════════════════
    #  PAGE — SETTINGS
    # ═══════════════════════════════════════════════════
    def _pg_settings(self, parent):
        _, inn, sf = self._make_scroll_page(parent, "Settings")
        SECTIONS = [
            ("Account", ORANGE, [
                ("Change Password","->"),("Update Email","->"),
                ("Two-Factor Auth","Enable"),("Connected Apps","Manage"),
            ]),
            ("Quiz Preferences", BLUE, [
                ("Questions per Quiz","5"),("Timer Duration","30s"),
                ("Show Explanation","Always"),("Difficulty","Mixed"),
            ]),
            ("Notifications", GREEN, [
                ("Daily Reminder","On"),("Streak Alerts","On"),
                ("Leaderboard Updates","Off"),("Achievement Alerts","On"),
            ]),
            ("Appearance", PURPLE, [
                ("Theme","Dark"),("Font Size","Medium"),("Animations","On"),
            ]),
            ("Privacy", TEAL, [
                ("Profile Visibility","Public"),("Show on Leaderboard","Yes"),
                ("Data Export","Download"),
            ]),
            ("Danger Zone", RED, [
                ("Reset All Progress","Reset"),("Delete Account","Delete"),
            ]),
        ]
        for sec_name, sec_col, items in SECTIONS:
            sec = tk.Frame(inn, bg=BG, padx=28); sec.pack(fill="x",pady=(10,0))
            tk.Label(sec, text=sec_name, bg=BG, fg=sec_col,
                     font=("Segoe UI",13,"bold")).pack(anchor="w",pady=(0,8))
            for item, val in items:
                row = tk.Frame(sec, bg=SURF, padx=20, pady=14)
                row.pack(fill="x",pady=2)
                tk.Label(row, text=item, bg=SURF, fg=TEXT, font=("Segoe UI",12)).pack(side="left")
                mkbtn(row, val, SURF3, fg=sec_col,
                      cmd=lambda n=item: messagebox.showinfo("Settings",f"'{n}' selected."),
                      size=11, padx=14, pady=4).pack(side="right")
        tk.Frame(inn, bg=BG, height=30).pack()
        sf.bind_all_children()

    # ═══════════════════════════════════════════════════
    #  QUIZ ENGINE
    # ═══════════════════════════════════════════════════
    def _launch_quiz(self, topic_name, practice=False, bonus=0):
        td = TOPICS[topic_name]
        self._launch_quiz_custom(topic_name, td["color"],
                                 td["questions"].copy(),
                                 practice=practice, bonus=bonus,
                                 topic_key=topic_name)

    def _launch_quiz_custom(self, title, color, questions,
                            practice=False, bonus=0, topic_key=None):
        random.shuffle(questions)
        win = tk.Toplevel(self, bg=BG)
        win.title(f"Quiz Arena  —  {title}")
        win.geometry("1000x720"); win.minsize(860,600)
        try:
            win.state("zoomed")
        except Exception:
            pass
        win.grab_set()

        state = {"idx":0,"score":0,"correct":0,"answered":False,"timer":30,"tid":None}

        topbar = tk.Frame(win, bg=SURF, pady=14, padx=24); topbar.pack(fill="x")
        tk.Label(topbar, text=f"{'Practice' if practice else 'Quiz'}  —  {title}",
                 bg=SURF, fg=TEXT, font=("Segoe UI",14,"bold")).pack(side="left")
        prog_lbl = tk.Label(topbar, text="", bg=SURF, fg=TEXT2, font=("Segoe UI",11))
        prog_lbl.pack(side="right",padx=24)
        timer_lbl = tk.Label(topbar, text="30", bg=ORANGE, fg=WHITE,
                             font=("Segoe UI Black",18,"bold"), width=4, padx=8, pady=4)
        if not practice:
            timer_lbl.pack(side="right")
        else:
            tk.Label(topbar, text="Practice Mode  |  No Timer",
                     bg=SURF, fg=TEXT3, font=("Segoe UI",10)).pack(side="right")

        pb_bg   = tk.Frame(win, bg=SURF3, height=4); pb_bg.pack(fill="x")
        pb_fill = tk.Frame(pb_bg, bg=color, height=4)
        pb_fill.place(x=0,y=0,relheight=1,relwidth=0)

        content = tk.Frame(win, bg=BG); content.pack(fill="both",expand=True)
        center  = tk.Frame(content, bg=BG)
        center.place(relx=0.5, rely=0.46, anchor="center", relwidth=0.72)

        q_tag     = tk.Label(center, text="", bg=color, fg=WHITE,
                             font=("Consolas",10,"bold"), padx=12, pady=4)
        q_tag.pack(anchor="w",pady=(0,10))
        q_num_lbl = tk.Label(center, text="", bg=BG, fg=TEXT2, font=("Segoe UI",10))
        q_num_lbl.pack(anchor="w",pady=(0,4))
        q_lbl     = tk.Label(center, text="", bg=BG, fg=TEXT,
                             font=("Segoe UI",16,"bold"), wraplength=680, justify="left")
        q_lbl.pack(anchor="w",pady=(0,18))

        letters  = ["A","B","C","D"]
        opt_ws   = []
        for i in range(4):
            row = tk.Frame(center, bg=SURF); row.pack(fill="x",pady=5)
            ll  = tk.Label(row, text=letters[i], bg=SURF3, fg=TEXT2,
                           font=("Consolas",12,"bold"), width=3, height=1, padx=6, pady=12)
            ll.pack(side="left")
            ol  = tk.Label(row, text="", bg=SURF, fg=TEXT, font=("Segoe UI",13),
                           anchor="w", padx=16, pady=13, cursor="hand2")
            ol.pack(side="left",fill="x",expand=True)
            opt_ws.append((row,ll,ol))

        exp_lbl = tk.Label(center, text="", bg=BG, font=("Segoe UI",12),
                           wraplength=680, justify="left")
        exp_lbl.pack(anchor="w",pady=(8,0))

        nxt_btn = mkbtn(center,"Next Question  ->",ORANGE,size=12,padx=22,pady=10)
        nxt_btn.pack(anchor="e",pady=12)
        nxt_btn.pack_forget()

        def stop_timer():
            if state["tid"]:
                win.after_cancel(state["tid"]); state["tid"]=None

        def tick():
            state["timer"] -= 1
            timer_lbl.config(text=str(state["timer"]))
            if state["timer"] <= 10: timer_lbl.config(bg=RED)
            if state["timer"] <= 0:
                if not state["answered"]: time_up()
            else:
                state["tid"] = win.after(1000, tick)

        def time_up():
            state["answered"] = True
            q = questions[state["idx"]]
            _mark(q["ans"], -1)
            exp_lbl.config(text=f"Time is up!  Correct: {q['opts'][q['ans']]}", fg=RED)
            nxt_btn.pack(anchor="e",pady=12)

        def _mark(correct_idx, chosen):
            for i,(row,ll,ol) in enumerate(opt_ws):
                if i==correct_idx:
                    row.config(bg=GREEN); ll.config(bg=GREEN,fg=WHITE); ol.config(bg=GREEN,fg=WHITE)
                elif i==chosen and chosen!=correct_idx:
                    row.config(bg=RED); ll.config(bg=RED,fg=WHITE); ol.config(bg=RED,fg=WHITE)
                else:
                    ol.config(fg=TEXT3)
                for w in [row,ll,ol]:
                    try:
                        w.unbind("<Button-1>"); w.unbind("<Enter>"); w.unbind("<Leave>")
                    except Exception:
                        pass
                ol.config(cursor="arrow")

        def check(chosen):
            if state["answered"]: return
            stop_timer(); state["answered"]=True
            q   = questions[state["idx"]]
            ans = q["ans"]
            _mark(ans, chosen)
            if chosen==ans:
                state["score"]+=100; state["correct"]+=1
                exp_lbl.config(text="Correct!  +100 pts", fg=GREEN)
            else:
                exp_lbl.config(text=f"Wrong!  Correct answer: {q['opts'][ans]}", fg=RED)
            if practice and q.get("exp"):
                exp_lbl.config(text=exp_lbl.cget("text")+f"\n\nTip: {q['exp']}")
            nxt_btn.pack(anchor="e",pady=12)

        def load_q():
            if state["idx"] >= len(questions):
                show_results(); return
            q = questions[state["idx"]]
            state["answered"]=False; state["timer"]=30
            stop_timer()
            pb_fill.place(relwidth=(state["idx"]+1)/len(questions))
            prog_lbl.config(text=f"Q {state['idx']+1} / {len(questions)}")
            tk_topic = q.get("_topic", title)
            q_tag.config(text=f"  {tk_topic}  ",
                         bg=TOPICS.get(tk_topic,{}).get("color",color))
            q_num_lbl.config(text=f"Question {state['idx']+1} of {len(questions)}")
            q_lbl.config(text=q["q"])
            exp_lbl.config(text="")
            nxt_btn.pack_forget()
            timer_lbl.config(bg=ORANGE)
            for i,(row,ll,ol) in enumerate(opt_ws):
                row.config(bg=SURF); ll.config(bg=SURF3,fg=TEXT2)
                ot = q["opts"][i] if i<len(q["opts"]) else ""
                ol.config(text=ot, bg=SURF, fg=TEXT, cursor="hand2")
                for ww in [row,ol]:
                    ww.bind("<Button-1>", lambda e,c=i: check(c))
                    ww.bind("<Enter>",  lambda e,r2=row,l2=ll,o2=ol:
                            [r2.config(bg=SURF3),l2.config(bg=BORDER),o2.config(bg=SURF3)]
                            if not state["answered"] else None)
                    ww.bind("<Leave>", lambda e,r2=row,l2=ll,o2=ol:
                            [r2.config(bg=SURF),l2.config(bg=SURF3),o2.config(bg=SURF)]
                            if not state["answered"] else None)
            if not practice:
                state["tid"] = win.after(1000, tick)

        def show_results():
            stop_timer()
            self.user["score"]   += state["score"]+bonus
            self.user["solved"]  += len(questions)
            self.user["correct"] += state["correct"]
            self.user["quizzes"] += 1
            tk_key = topic_key if topic_key else list(TOPICS.keys())[0]
            if tk_key in self.user["topic_scores"]:
                self.user["topic_scores"][tk_key]["solved"]  += len(questions)
                self.user["topic_scores"][tk_key]["correct"] += state["correct"]
            pct = round(state["correct"]/len(questions)*100)
            self._activities.append({
                "title": f"{title} {'Practice' if practice else 'Quiz'}",
                "pct":   pct,
                "when":  time.strftime("%H:%M  |  Today"),
            })
            self._refresh_sidebar()

            for ww in win.winfo_children(): ww.destroy()
            rf = tk.Frame(win, bg=BG); rf.pack(fill="both",expand=True)
            ri = tk.Frame(rf, bg=BG)
            ri.place(relx=0.5, rely=0.5, anchor="center")

            grade = GREEN if pct>=70 else (YELLOW if pct>=40 else RED)
            emoji = "Quiz Complete!" if pct>=70 else ("Almost there!" if pct>=40 else "Keep practicing!")
            tk.Label(ri, text=emoji, bg=BG, fg=color,
                     font=("Segoe UI Black",24,"bold")).pack(pady=(0,4))
            tk.Label(ri, text=title, bg=BG, fg=TEXT2, font=("Segoe UI",12)).pack(pady=(0,22))

            sb = tk.Frame(ri, bg=SURF, padx=70, pady=26); sb.pack(pady=10)
            total = state["score"]+bonus
            tk.Label(sb, text=str(total), bg=SURF, fg=grade,
                     font=("Segoe UI Black",52,"bold")).pack()
            tk.Label(sb, text="POINTS"+(f"  (+{bonus} daily bonus)" if bonus else ""),
                     bg=SURF, fg=TEXT2, font=("Segoe UI",10,"bold")).pack()

            srow = tk.Frame(ri, bg=BG); srow.pack(pady=14)
            for lbl, val, col in [
                ("Correct", str(state["correct"]), GREEN),
                ("Wrong",   str(len(questions)-state["correct"]), RED),
                ("Accuracy",f"{pct}%", grade),
            ]:
                box = tk.Frame(srow, bg=SURF, padx=26, pady=13)
                box.pack(side="left",padx=12)
                tk.Label(box, text=val, bg=SURF, fg=col,
                         font=("Segoe UI Black",20,"bold")).pack()
                tk.Label(box, text=lbl, bg=SURF, fg=TEXT2,
                         font=("Segoe UI",10)).pack()

            btns = tk.Frame(ri, bg=BG); btns.pack(pady=18)
            mkbtn(btns,"Retry",SURF2,fg=TEXT,
                  cmd=lambda: [win.destroy(),
                               self._launch_quiz(title) if title in TOPICS else None]
                  ).pack(side="left",padx=8)
            mkbtn(btns,"Dashboard",ORANGE,
                  cmd=lambda: [win.destroy(),self._nav_to("Dashboard")]
                  ).pack(side="left",padx=8)
            mkbtn(btns,"Leaderboard",SURF2,fg=TEXT,
                  cmd=lambda: [win.destroy(),self._nav_to("Leaderboard")]
                  ).pack(side="left",padx=8)

        nxt_btn.config(command=lambda: [state.update({"idx":state["idx"]+1}), load_q()])
        load_q()


# ═══════════════════════════════════════════════════════
#  ENTRY POINT
# ═══════════════════════════════════════════════════════
if __name__ == "__main__":
    app = QuizArena()
    app.mainloop()
