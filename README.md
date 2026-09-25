# Study Planner

A clean, modular, and beginner-friendly command-line Study Task Organizer built with pure Python.

---

## 1. Project Description

**Study Planner** is a terminal-based productivity tool developed for students to plan, track, and manage their daily academic study schedule. It helps students keep track of study topics across multiple subjects, assign realistic time estimates, prioritize critical chapters, monitor completion progress, and view insightful study analytics.

The project is designed to reflect the skills of a first-year student completing a **Python Essentials** course, using standard programming constructs, clear modular design, and basic Object-Oriented Programming (OOP) without any external libraries, frameworks, or databases.

---

## 2. Features

1. **Add Study Task**: Add a new study session with subject name, specific topic, duration (in minutes), priority level, and optional tags (Exam preparation, Revision, Practical).
2. **View All Tasks**: Display all study tasks in a clean tabular view showing IDs, status indicators, priorities, durations, and topics.
3. **Search Tasks**: Search tasks instantly by Task ID, Subject, or Topic name using membership matching.
4. **Mark Task as Completed**: Toggle task status from `Pending` to `Completed` with automatic status indicators (`[✓]`).
5. **Delete Task**: Remove tasks with an interactive confirmation prompt to prevent accidental deletions.
6. **Filter by Subject**: List all existing subjects without duplicates using Python sets and view tasks belonging to a chosen subject.
7. **Filter by Status**:
   - **View Pending Tasks**: Focus on upcoming study sessions.
   - **View Completed Tasks**: Review accomplished study goals.
8. **Study Summary & Statistics**:
   - Total planned study sessions, completed count, and pending count.
   - Completion percentage calculated with arithmetic operators.
   - Total study time converted into minutes, hours/minutes, and decimal hours.
   - Average study time, minimum session time, and maximum session time calculated using the Python `array` data structure.
   - Priority distribution breakdown using a Python dictionary.
   - Total unique subjects count using a Python set.
9. **Interactive Command-Line Menu**: Continues running smoothly in a loop until the user chooses to exit.
10. **Robust Input Validation**: Validates blank text, non-digit inputs, out-of-range numbers, and invalid menu options using standard conditional loops without crashing.

---

## 3. Technologies Used

- **Programming Language**: Python 3 (Python 3.6+)
- **Standard Library Modules**:
  - `array`: For typed numerical storage and duration calculations.
- **Operating Environment**: Any standard terminal / console (macOS Terminal, Linux Shell, Windows Command Prompt / PowerShell).
- **Dependencies**: None. Pure Python standard library.

---

## 4. Python Concepts Demonstrated

This project strictly adheres to the **Python Essentials** syllabus and practically applies every topic:

| # | Syllabus Concept | Where and How It Is Used in the Code |
|---|---|---|
| 1 | **Python fundamentals** | Script execution, indentation, comments, variable definitions, and docstrings. |
| 2 | **Input and output operations** | Interactive user prompts via `input()`, formatted outputs via `print()`, header banners. |
| 3 | **Variables and basic data types** | `int` (task_id, duration), `float` (percentage, hours), `str` (subject, topic), `bool` (is_exam, status checks). |
| 4 | **`type()` function** | `utils.inspect_task_types()` displays the dynamic data type of each attribute; type verification checks. |
| 5 | **Type conversion** | `int()` for user menu inputs, `float()` for division and percentages, `str()` for ID search matching. |
| 6 | **Arithmetic operators** | `+` (total time), `-` (pending = total - completed), `*` (drawing lines `"=" * 44`), `/` (averages, percentages), `//` (hours calculation), `%` (remaining minutes), `**` (priority effort score calculation). |
| 7 | **Assignment operators** | `=`, `+=` (incrementing IDs, accumulating time in loops), `-=` (decrementing counts). |
| 8 | **Membership operators** | `in` and `not in`: used in `search_tasks()`, validating menu choices, and checking priority dictionaries. |
| 9 | **Identity operators** | `is` and `is not`: used in `if task is None:`, `if task is not None:`, and checking variable types (`type(x) is int`). |
| 10 | **Bitwise operators** | Bit flags for optional attributes: `&` (bitwise AND to test flags), `\|` (bitwise OR to set flags), `<<` (left shift for flag values: `1 << 0`, `1 << 1`, `1 << 2`). |
| 11 | **Logical AND operator** | `if num < min_val or num > max_val:` and `if duration >= 5 and duration <= 720:`. |
| 12 | **Logical OR operator** | `if id_match or subject_match or topic_match:` in search matching and menu option checks. |
| 13 | **Logical NOT operator** | `if not query:`, `if not raw_val:`, `if not deleted:` for clean input validation. |
| 14 | **Relational operators** | `==`, `!=`, `<`, `>`, `<=`, `>=` throughout task comparisons, loops, and status updates. |
| 15 | **Division operators & mixed types** | Floor division (`//`), modulo (`%`), and exact float division (`/`) when converting study minutes into hours and decimals. |
| 16 | **Operator precedence & associativity** | Parentheses used in percentage calculation `(completed * 100.0) / total` and study effort calculation `(weight ** 2) * duration`. |
| 17 | **Core data structures** | |
|    | - **List** | `self.tasks = []` in `StudyPlanner` for storing task objects; dynamic filtering lists. |
|    | - **Tuple** | `PRIORITY_TUPLE = ("Low", "Medium", "High")` and `STATUS_TUPLE = ("Pending", "Completed")`. |
|    | - **Set** | `unique_subjects = set()` to dynamically extract distinct subject names without duplicates. |
|    | - **Dictionary** | `task.to_dict()` converting task instances to dictionaries, priority weights mapping, and summary distribution dictionary. |
|    | - **Frozenset** | `ALLOWED_PRIORITIES = frozenset(["Low", "Medium", "High"])` representing immutable system configuration. |
| 18 | **Control flow statements** | `if`, `if-else`, `if-elif-else`, nested conditions, `for` loops, `while` loops, `break`, and `continue`. |
| 19 | **Functions** | Modular, well-documented functions with parameters and return values in `utils.py` and `main.py`. |
| 20 | **Modules and packages** | Multi-file modular architecture: `main.py` imports `planner` and `utils`; `planner.py` imports `utils`. |
| 21 | **Array data structure** | Python's standard `array.array('i')` used in `calculate_summary()` for numerical processing of task durations. |
| 22 | **Object-Oriented Programming (OOP)** | Classes `StudyTask` and `StudyPlanner`, `__init__` constructors, instance attributes (`self.subject`), and instance methods (`mark_completed()`). |

---

## 5. Project Structure

```
study-planner/
│
├── main.py              # Main user interface, menu loop, and user interaction handlers
├── planner.py           # Core business logic: StudyTask and StudyPlanner OOP classes
├── utils.py             # Helper utilities, mathematical calculations, and input validators
├── requirements.txt     # Documents standard library requirements (zero 3rd-party dependencies)
├── PROJECT_REPORT.md    # Detailed academic project report and test cases
└── README.md            # Comprehensive project documentation
```

---

## 6. Requirements

- **Operating System**: macOS, Windows, or Linux.
- **Python Version**: Python 3.6 or above (Python 3.8+ recommended).
- **External Dependencies**: None. Uses only standard Python library modules (`array`).

---

## 7. Installation & Setup Instructions

Because this project uses pure Python without external dependencies, no installation with `pip` is required.

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-username/study-planner.git
   cd study-planner
   ```

2. **Verify Python 3 is installed**:
   ```bash
   python3 --version
   ```
   *(or `python --version` on Windows)*

---

## 8. How to Run the Project

Execute the following command in your terminal from inside the project directory:

```bash
python3 main.py
```

On Windows Command Prompt / PowerShell:
```bash
python main.py
```

---

## 9. How to Use the Application

Once launched, the application displays a main menu with 10 options:

```
========================================
           STUDY PLANNER
========================================
1. Add Study Task
2. View All Tasks
3. Search Task
4. Mark Task as Completed
5. Delete Task
6. View Tasks by Subject
7. View Pending Tasks
8. View Completed Tasks
9. Study Summary
10. Exit
========================================
Enter your choice (1-10):
```

### Steps to Perform Common Actions:
- **Adding a Task**: Select `1`. Enter the subject name (e.g., `Python`), topic (e.g., `Object Oriented Programming`), duration in minutes (e.g., `60`), and priority (`1` for Low, `2` for Medium, `3` for High).
- **Viewing Tasks**: Select `2` to list all tasks with their current progress and ID numbers.
- **Searching**: Select `3` and type any keyword (e.g., `Math` or `Matrices`).
- **Marking Complete**: Select `4`, enter the Task ID number (e.g., `1`), and the task will be marked as Completed `[✓]`.
- **Viewing Summary**: Select `9` to view a comprehensive breakdown of your study statistics.
- **Exiting**: Select `10` or type `exit` to exit cleanly.

---

## 10. Example Output

### Study Progress Summary (Option 9)
```
============================================
    STUDY PROGRESS SUMMARY
============================================
Total Tasks Recorded       : 4
Completed Tasks            : 2 [✓]
Pending Tasks              : 2 [ ]
Completion Rate            : 50.0%
--------------------------------------------
Study Time Analysis (using Python array & mixed division):
Total Planned Time         : 245 minutes
Formatted Duration         : 4 hours and 5 minutes
Decimal Equivalent         : 4.08 hours
Average Time Per Task      : 61.2 minutes
Shortest Task Duration     : 45 minutes
Longest Task Duration      : 90 minutes
--------------------------------------------
Total Unique Subjects      : 3 (via Python set)
Priority Breakdown (via Python dictionary):
 - Low   : 1 task(s)
 - Medium: 1 task(s)
 - High  : 2 task(s)
--------------------------------------------
```

---

## 11. Limitations

1. **In-Memory Storage**: In strict accordance with the first-year Python Essentials syllabus (which does not include database systems, SQL, or external storage), tasks are maintained in memory during the execution session. When the program exits, tasks reset to the initial sample state.
2. **Terminal Only**: The program operates strictly through a command-line interface and does not feature a graphical window (GUI) or web interface.
3. **Single User**: Designed for an individual student on a local machine.

---

## 12. Future Improvements

When more advanced Python topics are introduced in subsequent semesters, the application can be enhanced with:
- **Persistent Storage**: Saving tasks to text files, JSON files, or a SQLite database.
- **Due Dates & Timestamps**: Integrating Python's `datetime` module to track deadlines and study completion dates.
- **Interactive Timer**: A Pomodoro study timer to track actual study time versus planned time.
- **Graphical Interface**: A modern desktop UI using Tkinter or PyQt, or a lightweight web dashboard.
