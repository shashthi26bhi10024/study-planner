# Academic Project Report: Study Planner

**Course**: Python Essentials (First Year Undergraduate)  
**Project Title**: Study Planner (Terminal-Based Study Task Organizer)  
**Language**: Python 3 (Pure Standard Library)  

---

## 1. Title
**STUDY PLANNER: A Command-Line Study Task Organizer Using Core Python Principles**

---

## 2. Introduction
In a university environment, students encounter multiple academic courses running simultaneously, including core programming, mathematics, physics, and humanities. Managing revision, coursework deadlines, lab preparations, and daily study schedules across these subjects presents a significant time-management challenge.

The **Study Planner** application is a terminal-based utility developed using pure Python. It enables students to systematically register study tasks, assign time estimates, organize tasks by subject, track completion status, and evaluate productivity through statistical metrics.

---

## 3. Problem Statement
Students frequently struggle with:
1. Disorganized study sessions leading to neglected subjects.
2. Lack of tracking between planned study time and completed revisions.
3. Over-complicated productivity applications requiring cloud accounts, external dependencies, or complex user interfaces.
4. Difficulty in getting an immediate overview of pending versus completed study goals.

There is a need for a lightweight, dependency-free, and straightforward study organizer that runs instantly in any standard terminal.

---

## 4. Objectives
The core objectives of the project are:
1. To develop a functional, interactive command-line application for daily study scheduling.
2. To apply all 22 fundamental Python topics covered in the first-year Python Essentials curriculum.
3. To implement Object-Oriented Programming (OOP) principles using clear, beginner-friendly class models.
4. To organize the code logically across distinct modules (`main.py`, `planner.py`, `utils.py`).
5. To build a robust system resilient to invalid inputs without using unlearned or external libraries.

---

## 5. Proposed Solution
The proposed solution is a modular Python CLI application that maintains tasks as objects in memory. The system is split into three cohesive modules:
- `StudyTask`: Represents individual study sessions with instance attributes (ID, Subject, Topic, Duration, Priority, Status, Flags).
- `StudyPlanner`: Manages the overall collection of tasks using standard Python lists, providing searching, filtering, and summarization methods.
- `utils`: Houses helper functions for input validation, mathematical time conversion, string formatting, and bitwise attribute handling.

The user interacts through an intuitive numbered text menu running in a continuous control loop.

---

## 6. Features
1. **Add Study Task**: Captures subject, topic, study duration, priority level, and optional tags.
2. **View All Tasks**: Formats all tasks into an aligned list with completion status markers (`[✓]` or `[ ]`).
3. **Search Tasks**: Matches search keywords against Task IDs, subject names, or topics.
4. **Mark Task as Completed**: Toggles task status to `Completed`.
5. **Delete Task**: Deletes a task from the planner with an explicit confirmation step.
6. **Filter by Subject**: Lists available subjects using a Python set and filters tasks accordingly.
7. **Filter by Status**:
   - Lists only pending tasks to highlight immediate priorities.
   - Lists only completed tasks to show accomplishments.
8. **Study Progress Summary**:
   - Computes total study minutes, integer hours, remainder minutes, and decimal hours.
   - Calculates task completion percentage with operator precedence.
   - Computes average, minimum, and maximum session durations using Python's `array` module.
   - Displays priority breakdown via a Python dictionary and unique subjects via a Python set.
9. **Graceful Exit**: Clean termination of the loop.

---

## 7. Python Concepts Used

The project was constructed specifically to demonstrate mastery over the 22 topics of the course syllabus:

| Topic Number & Name | Implementation Details in Study Planner |
|---|---|
| **1. Python Fundamentals** | Clean indentation, block structure, meaningful variable naming, and header comments. |
| **2. Input & Output** | `input()` for reading user commands; `print()` for styled banners, tables, and task cards. |
| **3. Variables & Data Types** | `int` (task_id, duration), `float` (percentage, decimal hours), `str` (subject, topic), `bool` (is_exam, status). |
| **4. `type()` Function** | `utils.inspect_task_types()` dynamically queries the type of attributes using `type()`. |
| **5. Type Conversion** | `int()` to parse integers from strings; `float()` for division operations; `str()` for search matching. |
| **6. Arithmetic Operators** | `+` (accumulation), `-` (pending calculation), `*` (border lines `"=" * 44`), `/` (average & percentage), `//` (integer hours), `%` (remainder minutes), `**` (effort score calculation). |
| **7. Assignment Operators** | `=` for variable assignment, `+=` for ID auto-increment and total time summation, `-=` for reductions. |
| **8. Membership Operators** | `in` and `not in`: verifying user menu choices, priority dictionary keys, and substring search matching. |
| **9. Identity Operators** | `is` and `is not`: verifying `if task is None` or `if type(task.task_id) is int`. |
| **10. Bitwise Operators** | Bitwise flags for task characteristics (`1 << 0`, `1 << 1`, `1 << 2`); bitwise OR `\|` to set flags; bitwise AND `&` to test flags. |
| **11. Logical AND Operator** | `and`: used in duration range validation (`if num >= min_val and num <= max_val`). |
| **12. Logical OR Operator** | `or`: used in multi-field search conditions (`if id_match or subject_match or topic_match`). |
| **13. Logical NOT Operator** | `not`: used in string validation (`if not query:`) and boolean checks. |
| **14. Relational Operators** | `==`, `!=`, `<`, `>`, `<=`, `>=`: used in comparisons across loops and menu handlers. |
| **15. Division Operators** | Demonstrates both float division `/` (`decimal_hours = minutes / 60.0`) and integer floor division `//` (`hours = minutes // 60`). |
| **16. Operator Precedence** | Enforcing order of operations with parentheses: `percentage = (float(part) * 100.0) / float(total)`. |
| **17. Core Data Structures** | Lists (tasks collection), Tuples (priority choices), Sets (unique subjects), Dictionaries (task record, priority breakdown), Frozensets (immutable allowed values). |
| **18. Control Flow Statements** | `if`, `if-else`, `if-elif-else`, nested conditionals, `while` loops for continuous operation, `for` loops for iteration, `break` to exit loops, and `continue` to handle input errors. |
| **19. Functions** | Modular, single-purpose functions with parameters, default values, and return statements. |
| **20. Modules & Packages** | Three-file structure (`main.py`, `planner.py`, `utils.py`) using `import` statements. |
| **21. Array Data Structure** | Python's standard `array.array('i')` used in `calculate_summary()` for numerical processing of durations. |
| **22. OOP in Python** | `class StudyTask` and `class StudyPlanner`, `__init__()`, instance attributes, and instance methods. |

---

## 8. Data Structures Used
1. **List (`list`)**:
   - `self.tasks = []`: Serves as the primary container for `StudyTask` instances.
   - Dynamically grows using `.append()` and shrinks using `.remove()`.
2. **Tuple (`tuple`)**:
   - `PRIORITY_TUPLE = ("Low", "Medium", "High")`: Immutable sequence defining valid priorities.
   - `STATUS_TUPLE = ("Pending", "Completed")`: Fixed status options.
3. **Set (`set`)**:
   - `subjects_set = set()`: Gathers distinct subjects from tasks, naturally discarding duplicates for subject filtering.
4. **Dictionary (`dict`)**:
   - `task.to_dict()`: Converts instance attributes to key-value pairs.
   - `priority_counts = {"Low": 0, "Medium": 0, "High": 0}`: Tracks distribution of tasks by priority.
5. **Frozenset (`frozenset`)**:
   - `ALLOWED_PRIORITIES = frozenset(["Low", "Medium", "High"])`: Demonstrates immutable set structures.
6. **Array (`array.array('i')`)**:
   - Used in `StudyPlanner.calculate_summary()` to hold task durations as homogeneous signed integers for min, max, sum, and average calculations.

---

## 9. Functions Used

### In `utils.py`:
- `print_header(title)`: Formats and displays an aesthetic uppercase header.
- `print_divider()`: Prints a uniform separator line.
- `inspect_task_types(task)`: Displays the Python types of each attribute using `type()`.
- `convert_minutes_to_hours(minutes)`: Converts minutes to whole hours, remainder minutes, and float hours.
- `calculate_percentage(part, total)`: Calculates completion percentage with operator precedence.
- `calculate_study_score(priority, duration_minutes)`: Calculates an effort index using `**`.
- `encode_study_flags(is_rev, is_imp, is_prac)`: Generates bitmask using bitwise `|` and `<<`.
- `has_flag(flags, flag_to_check)`: Tests bitmask using bitwise `&`.
- `format_task_row(task)`: Formats task into a single tabular row string.
- `get_non_empty_string(prompt)`: Validates that text inputs are not empty.
- `get_valid_integer(prompt, min_val, max_val)`: Validates integer numbers within limits.
- `get_valid_priority()`: Provides an interactive priority selection submenu.

### In `planner.py`:
- `StudyTask.mark_completed()`: Updates task status to "Completed".
- `StudyTask.to_dict()`: Exports task attributes as a Python dictionary.
- `StudyTask.display_details()`: Displays multi-line card format of a task.
- `StudyPlanner.add_task()`: Instantiates and records a new `StudyTask`.
- `StudyPlanner.get_all_tasks()`: Retrieves all task objects.
- `StudyPlanner.find_task_by_id()`: Looks up a task by numeric ID.
- `StudyPlanner.search_tasks()`: Searches tasks across multiple attributes.
- `StudyPlanner.mark_task_completed()`: Completes a task by ID.
- `StudyPlanner.delete_task()`: Removes a task by ID.
- `StudyPlanner.get_tasks_by_subject()`: Filters tasks for a specific subject.
- `StudyPlanner.get_unique_subjects()`: Returns a `set` of subjects.
- `StudyPlanner.get_pending_tasks()`: Returns all pending tasks.
- `StudyPlanner.get_completed_tasks()`: Returns all completed tasks.
- `StudyPlanner.calculate_summary()`: Compiles statistics using `array` and arithmetic operators.

### In `main.py`:
- `display_menu()`: Renders the 10-option main menu.
- `handle_add_task()`, `handle_view_all()`, `handle_search()`, `handle_mark_completed()`, `handle_delete_task()`, `handle_view_by_subject()`, `handle_view_pending()`, `handle_view_completed()`, `handle_summary()`: Handler functions routing menu actions.
- `main()`: Orchestrates application lifecycle.

---

## 10. Object-Oriented Programming (OOP) Implementation

The system implements basic OOP suitable for a first-year undergraduate:
- **Encapsulation of Data**: The `StudyTask` class encapsulates the attributes of a study session (`task_id`, `subject`, `topic`, `duration`, `priority`, `status`, `flags`) and provides methods (`mark_completed`, `to_dict`, `display_details`) to act on that data.
- **Collection Management**: The `StudyPlanner` class manages the lifecycle of tasks, maintaining internal state (`self.tasks` and `self.next_id`), providing abstraction between the user interface and data operations.

---

## 11. Modules Used
- `main.py`: Interface controller and execution entry point.
- `planner.py`: Domain models and business logic.
- `utils.py`: Reusable utility functions, validators, and operators demonstrations.
- `array` (Standard Library): Numerical typed array implementation.

---

## 12. Program Flow

```
[Start]
   │
   ▼
[Initialize StudyPlanner Instance & Load Default Tasks]
   │
   ▼
┌─► [Display 10-Option Menu]
│      │
│      ▼
│   [Read User Input]
│      │
│      ├─ Choice 1  ──► Add Study Task
│      ├─ Choice 2  ──► View All Tasks
│      ├─ Choice 3  ──► Search Tasks
│      ├─ Choice 4  ──► Mark Task Completed
│      ├─ Choice 5  ──► Delete Task
│      ├─ Choice 6  ──► Filter Tasks by Subject
│      ├─ Choice 7  ──► Filter Pending Tasks
│      ├─ Choice 8  ──► Filter Completed Tasks
│      ├─ Choice 9  ──► Calculate & Display Summary
│      ├─ Choice 10 ──► Exit Application ──► [Terminate]
│      └─ Invalid   ──► Display Error Message
│              │
└──────────────┘
```

---

## 13. Sample Input & Output

### Adding a Task:
```
============================================
    ADD NEW STUDY TASK
============================================
Enter Subject (e.g., Python, Math, Physics): Data Structures
Enter Topic (e.g., Functions, Matrices): Binary Search Trees
Enter Planned Duration in minutes (5 - 720): 90

Select Priority:
1. Low
2. Medium
3. High
Enter choice (1-3) [Default 2 for Medium]: 3

Optional Attributes (Enter 'y' for Yes, or press Enter for No):
Is this an Exam/Important topic? (y/n): y
Does this require revision? (y/n): y
Is this a practical/lab exercise? (y/n): n

Success: Study Task added successfully!
Assigned Task ID: 5
```

---

## 14. Testing & Verification

The application was tested through the 10 manual test cases specified for the project:

### Test Case 1: Add a valid study task
- **Action**: Chose Option 1, entered subject `Chemistry`, topic `Thermodynamics`, duration `75`, priority `High`.
- **Expected Result**: Task added with next sequential ID; confirmation message displayed.
- **Actual Result**: Task ID 5 created, confirmed in task list. **[PASS]**

### Test Case 2: Enter an invalid menu option
- **Action**: Entered `99` and `abc` at the main menu prompt.
- **Expected Result**: Error message shown: `[!] Invalid selection...`; menu re-displayed without crashing.
- **Actual Result**: Handled cleanly, loop repeated. **[PASS]**

### Test Case 3: Search for an existing task
- **Action**: Chose Option 3, searched for `Matrices`.
- **Expected Result**: Returns Task ID 2 (Mathematics - Matrices and Determinants).
- **Actual Result**: Correct task details displayed. **[PASS]**

### Test Case 4: Search for a task that does not exist
- **Action**: Chose Option 3, searched for `Quantum Physics`.
- **Expected Result**: Message: `No tasks found matching 'Quantum Physics'.`
- **Actual Result**: Handled cleanly, zero matches reported. **[PASS]**

### Test Case 5: Mark an existing task as completed
- **Action**: Chose Option 4, entered Task ID `1`.
- **Expected Result**: Status changes from `Pending` to `Completed [✓]`.
- **Actual Result**: Status updated, confirmed in summary and completed list. **[PASS]**

### Test Case 6: Delete an existing task
- **Action**: Chose Option 5, entered Task ID `3`, confirmed deletion with `y`.
- **Expected Result**: Task ID 3 removed from planner.
- **Actual Result**: Task deleted, subsequent lookups report not found. **[PASS]**

### Test Case 7: Display pending tasks
- **Action**: Chose Option 7.
- **Expected Result**: Displays only tasks whose status is `Pending`.
- **Actual Result**: Only pending tasks (IDs 2 and 5) displayed. **[PASS]**

### Test Case 8: Display completed tasks
- **Action**: Chose Option 8.
- **Expected Result**: Displays only tasks whose status is `Completed`.
- **Actual Result**: Only completed tasks (IDs 1 and 4) displayed. **[PASS]**

### Test Case 9: View study summary
- **Action**: Chose Option 9.
- **Expected Result**: Displays task count, completion percentage, total/average duration, array stats, and priority breakdown.
- **Actual Result**: Accurate mathematical statistics printed without errors. **[PASS]**

### Test Case 10: Exit the program
- **Action**: Chose Option 10.
- **Expected Result**: Prints exit greeting and terminates execution cleanly.
- **Actual Result**: Program exited with code 0. **[PASS]**

---

## 15. Limitations
1. **Volatile Memory**: Data is maintained in RAM during execution. Tasks are re-initialized upon restart since external databases and file I/O are beyond the first-year course scope.
2. **Terminal Interface**: Does not have a graphical interface (GUI).
3. **No Automatic Timers**: Durations represent planned estimates rather than real-time countdown clocks.

---

## 16. Future Scope
In subsequent terms, this project can be expanded with:
1. File persistence using JSON or SQLite.
2. Real-time study stopwatch using Python's `time` module.
3. Graphical user interface built with Tkinter.
4. Reminder notifications before planned study sessions.

---

## 17. Conclusion
The **Study Planner** project fulfills all requirements specified for a first-year student completing a Python Essentials course. It applies all 22 syllabus concepts—including control flow, all operator categories, lists, tuples, sets, dictionaries, frozensets, the Python array module, modular architecture, and basic OOP—while serving as a practical, easy-to-use command-line study assistant.
