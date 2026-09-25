"""
utils.py - Utility functions and helpers for the Study Planner application.

This module demonstrates core Python concepts:
- Python fundamentals, I/O operations (print, input)
- Data type inspection with type()
- Type conversion (int, float, str)
- Arithmetic operators (+, -, *, /, //, %, **)
- Comparison and relational operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Membership operators (in, not in)
- Identity operators (is, is not)
- Bitwise operators (&, |, ^, ~, <<, >>)
- Core data structures: tuple, set, frozenset, dictionary
"""

# -------------------------------------------------------------
# Constant Tuples and Frozensets (Core Data Structures)
# -------------------------------------------------------------
# Tuple: fixed, immutable sequence of priorities and statuses
PRIORITY_TUPLE = ("Low", "Medium", "High")
STATUS_TUPLE = ("Pending", "Completed")

# Frozenset: immutable set of allowed priority strings
ALLOWED_PRIORITIES = frozenset(["Low", "Medium", "High"])

# Dictionary: priority numeric weight mapping
PRIORITY_WEIGHTS = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

# Bitwise flags for optional study attributes
# Demonstrates bitwise flags and bitwise operators (&, |, ^, <<)
FLAG_REVISION = 1 << 0   # 1  (0b001) - Needs Revision
FLAG_IMPORTANT = 1 << 1  # 2  (0b010) - High Importance / Exam
FLAG_PRACTICAL = 1 << 2  # 4  (0b100) - Practical / Coding Task


def print_header(title):
    """
    Displays a formatted header block with borders.
    Demonstrates:
    - String multiplication operator (*)
    - String concatenation (+)
    - Built-in print() function
    """
    border = "=" * 44
    print("\n" + border)
    print(" " * 4 + title.upper())
    print(border)


def print_divider():
    """Prints a standard divider line."""
    print("-" * 44)


def inspect_task_types(task):
    """
    Inspects and displays data types of task attributes.
    Demonstrates:
    - type() built-in function
    - Identity operator (is, is not)
    """
    print("\n[DEBUG / LEARNING MODE: Data Type Inspection]")
    print("Attribute 'task_id':  Value =", task.task_id, "| Type =", type(task.task_id))
    print("Attribute 'subject':  Value =", task.subject, "| Type =", type(task.subject))
    print("Attribute 'topic':    Value =", task.topic, "| Type =", type(task.topic))
    print("Attribute 'duration': Value =", task.duration, "| Type =", type(task.duration))
    print("Attribute 'priority': Value =", task.priority, "| Type =", type(task.priority))
    print("Attribute 'status':   Value =", task.status, "| Type =", type(task.status))

    # Identity operator check
    if type(task.task_id) is int:
        print("Verification: task_id is of type int -> True")
    if type(task.subject) is not int:
        print("Verification: subject is not of type int -> True")
    print_divider()


def convert_minutes_to_hours(minutes):
    """
    Converts minutes to hours and minutes using division operators.
    Demonstrates:
    - Integer floor division (//)
    - Modulo operator (%)
    - Float division (/) with mixed data types
    - Type conversion (float, int, str)
    """
    # Floor division gives whole hours
    hours = minutes // 60

    # Modulo gives remaining minutes
    remaining_minutes = minutes % 60

    # Float division gives exact decimal hours
    decimal_hours = float(minutes) / 60.0

    return hours, remaining_minutes, decimal_hours


def calculate_percentage(part, total):
    """
    Calculates percentage with operator precedence and associativity.
    Demonstrates:
    - Operator precedence: parentheses (part * 100.0) evaluated before division (/)
    - Mixed data type arithmetic (int and float)
    - Relational comparison (<=, ==)
    """
    if total <= 0:
        return 0.0

    # Formula: (part * 100.0) / total
    # Associativity and precedence ensured with parentheses
    percentage = (float(part) * 100.0) / float(total)
    return round(percentage, 2)


def calculate_study_score(priority, duration_minutes):
    """
    Calculates an estimated study effort score.
    Demonstrates:
    - Exponentiation operator (**)
    - Arithmetic multiplication (*) and addition (+)
    - Dictionary lookup
    """
    weight = PRIORITY_WEIGHTS.get(priority, 1)
    # Exponentiation formula: (weight ** 2) * duration_minutes
    score = (weight ** 2) * duration_minutes
    return score


def encode_study_flags(is_revision, is_important, is_practical):
    """
    Encodes task attributes into an integer bitmask.
    Demonstrates:
    - Bitwise OR (|)
    - Bitwise left shift (<<)
    """
    flags = 0
    if is_revision:
        flags = flags | FLAG_REVISION
    if is_important:
        flags = flags | FLAG_IMPORTANT
    if is_practical:
        flags = flags | FLAG_PRACTICAL
    return flags


def has_flag(flags, flag_to_check):
    """
    Checks if a bitwise flag is set.
    Demonstrates:
    - Bitwise AND (&)
    - Comparison operator (!=)
    """
    return (flags & flag_to_check) != 0


def format_task_row(task):
    """
    Formats a single task into a clean tabular display string.
    Demonstrates string concatenation, formatting, and str() conversion.
    """
    status_symbol = "[✓]" if task.status == "Completed" else "[ ]"
    return (
        f"ID: {task.task_id:<3} | {status_symbol} {task.status:<9} | "
        f"{task.priority:<6} | {task.duration:>3} mins | "
        f"{task.subject} - {task.topic}"
    )


def get_non_empty_string(prompt):
    """
    Validates that user input is not empty.
    Demonstrates:
    - while loop
    - strip() method
    - Logical NOT operator (not)
    - if condition
    """
    while True:
        value = input(prompt).strip()
        if not value:
            print("Error: Input cannot be blank. Please try again.")
            continue
        return value


def get_valid_integer(prompt, min_val=1, max_val=1440):
    """
    Validates positive integer inputs within an allowed range.
    Demonstrates:
    - while loop
    - isdigit() string check (avoids exceptions outside basic syllabus)
    - Type conversion: int()
    - Relational operators (<, >)
    - Logical OR operator (or)
    """
    while True:
        raw_val = input(prompt).strip()
        if not raw_val:
            print("Error: Please enter a value.")
            continue

        if not raw_val.isdigit():
            print("Error: Invalid number. Please enter digits only.")
            continue

        num = int(raw_val)

        # Relational and logical check
        if num < min_val or num > max_val:
            print(f"Error: Value must be between {min_val} and {max_val}.")
            continue

        return num


def get_valid_priority():
    """
    Prompts user to select task priority.
    Demonstrates:
    - Displaying a menu of options
    - Tuple iteration with for loop
    - Membership operator (in)
    - Dictionary mapping
    """
    print("\nSelect Priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    choice_map = {
        "1": "Low",
        "2": "Medium",
        "3": "High"
    }

    while True:
        choice = input("Enter choice (1-3) [Default 2 for Medium]: ").strip()
        if choice == "":
            return "Medium"

        # Membership operator check
        if choice in choice_map:
            return choice_map[choice]
        else:
            print("Error: Invalid choice. Please enter 1, 2, or 3.")
