"""
planner.py - Core data models and planner operations for Study Planner.

This module demonstrates:
- Object-Oriented Programming (OOP) in Python:
  - class StudyTask
  - class StudyPlanner
  - __init__() constructor
  - instance attributes and instance methods
  - object instantiation
- Core data structures:
  - list (collection of tasks)
  - dictionary (task details dictionary and priority statistics)
  - set (gathering unique subjects without duplicates)
  - tuple (order of priorities)
  - frozenset (validation against immutable allowed states)
- Array data structure:
  - import array
  - array.array('i') used for numerical calculations on study durations
- Control flow:
  - if, if-else, if-elif-else, nested conditions
  - for loops, while loops, break, continue
- Operators:
  - Arithmetic operators (+, -, *, /, //, %)
  - Assignment operators (=, +=, -=)
  - Membership operators (in, not in)
  - Identity operators (is, is not)
  - Logical operators (and, or, not)
"""

import array
import utils


class StudyTask:
    """
    Represents an individual study task.
    Demonstrates:
    - OOP class definition
    - __init__ constructor
    - Instance attributes
    - Instance methods
    - Dictionary creation
    """

    def __init__(self, task_id, subject, topic, duration, priority="Medium", status="Pending", flags=0):
        # Instance attributes
        self.task_id = task_id          # int: unique identifier
        self.subject = subject          # str: name of the subject
        self.topic = topic              # str: specific chapter or topic
        self.duration = duration        # int: duration in minutes
        self.priority = priority        # str: Low, Medium, High
        self.status = status            # str: Pending, Completed
        self.flags = flags              # int: bitwise flags for attributes

    def mark_completed(self):
        """
        Marks this task as Completed.
        Demonstrates assignment operator (=).
        """
        self.status = "Completed"

    def to_dict(self):
        """
        Converts the task object into a standard Python dictionary.
        Demonstrates dictionary data structure.
        """
        task_dictionary = {
            "task_id": self.task_id,
            "subject": self.subject,
            "topic": self.topic,
            "duration": self.duration,
            "priority": self.priority,
            "status": self.status,
            "flags": self.flags
        }
        return task_dictionary

    def display_details(self):
        """
        Prints detailed information of this task.
        Demonstrates I/O operations and string formatting.
        """
        utils.print_divider()
        print(f"Task ID   : {self.task_id}")
        print(f"Subject   : {self.subject}")
        print(f"Topic     : {self.topic}")
        print(f"Duration  : {self.duration} minutes")
        print(f"Priority  : {self.priority}")
        print(f"Status    : {self.status}")

        # Check bitwise flags using helper functions
        attributes = []
        if utils.has_flag(self.flags, utils.FLAG_REVISION):
            attributes.append("Revision Required")
        if utils.has_flag(self.flags, utils.FLAG_IMPORTANT):
            attributes.append("Exam/High Importance")
        if utils.has_flag(self.flags, utils.FLAG_PRACTICAL):
            attributes.append("Practical/Lab")

        if len(attributes) > 0:
            print("Attributes: " + ", ".join(attributes))
        else:
            print("Attributes: Standard Study")
        utils.print_divider()


class StudyPlanner:
    """
    Manages a collection of StudyTask objects.
    Demonstrates:
    - List operations
    - Set operations
    - Dictionary operations
    - Array operations (array.array('i'))
    - Searching, filtering, and summary calculations
    """

    def __init__(self):
        # List of StudyTask objects
        self.tasks = []
        # Next sequential ID
        self.next_id = 1

        # Seed realistic initial tasks for first-year demonstration
        self._load_sample_tasks()

    def _load_sample_tasks(self):
        """
        Populates initial sample tasks so the application is ready to explore.
        Demonstrates list appending and object creation.
        """
        sample_data = [
            ("Python", "Functions and Scope", 60, "High", "Pending", utils.FLAG_IMPORTANT),
            ("Mathematics", "Matrices and Determinants", 90, "Medium", "Pending", 0),
            ("Physics", "Wave Optics and Interference", 45, "Low", "Completed", utils.FLAG_REVISION),
            ("Python", "Lists and Dictionaries", 50, "High", "Completed", utils.FLAG_PRACTICAL)
        ]

        for subject, topic, duration, priority, status, flags in sample_data:
            task = StudyTask(
                task_id=self.next_id,
                subject=subject,
                topic=topic,
                duration=duration,
                priority=priority,
                status=status,
                flags=flags
            )
            self.tasks.append(task)
            # Assignment operator with addition (+=)
            self.next_id += 1

    def add_task(self, subject, topic, duration, priority="Medium", flags=0):
        """
        Creates and adds a new StudyTask to the planner.
        Demonstrates:
        - Class instantiation
        - List append method
        - Incrementing with +=
        """
        new_task = StudyTask(
            task_id=self.next_id,
            subject=subject,
            topic=topic,
            duration=duration,
            priority=priority,
            status="Pending",
            flags=flags
        )
        self.tasks.append(new_task)
        self.next_id += 1
        return new_task

    def get_all_tasks(self):
        """Returns the list of all tasks."""
        return self.tasks

    def find_task_by_id(self, task_id):
        """
        Finds and returns a task by its task_id.
        Demonstrates:
        - for loop
        - Comparison operator (==)
        - Identity operator (is not None)
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        # If not found, return None
        return None

    def search_tasks(self, query):
        """
        Searches tasks matching task_id, subject, or topic.
        Demonstrates:
        - Membership operator (in)
        - Logical OR operator (or)
        - Type conversion (str)
        - List accumulation
        """
        query_clean = query.strip().lower()
        results = []

        for task in self.tasks:
            # Check if query matches ID, subject, or topic
            id_match = query_clean in str(task.task_id)
            subject_match = query_clean in task.subject.lower()
            topic_match = query_clean in task.topic.lower()

            # Logical OR evaluation
            if id_match or subject_match or topic_match:
                results.append(task)

        return results

    def mark_task_completed(self, task_id):
        """
        Marks a specific task as completed.
        Demonstrates:
        - Identity operator check (is not None)
        - Boolean return values (True/False)
        """
        task = self.find_task_by_id(task_id)

        # Identity operator: if task is not None
        if task is not None:
            task.mark_completed()
            return True
        else:
            return False

    def delete_task(self, task_id):
        """
        Deletes a task by ID.
        Demonstrates:
        - for loop with index tracking
        - list.pop() or list.remove()
        - break statement
        """
        target_task = None
        for task in self.tasks:
            if task.task_id == task_id:
                target_task = task
                break  # Exit search loop once found

        if target_task is not None:
            self.tasks.remove(target_task)
            return True
        return False

    def get_tasks_by_subject(self, subject_name):
        """
        Filters tasks for a given subject.
        Demonstrates:
        - String methods and case-insensitivity
        - Relational operator (==)
        - List accumulation
        """
        filtered = []
        target = subject_name.strip().lower()

        for task in self.tasks:
            if task.subject.strip().lower() == target:
                filtered.append(task)

        return filtered

    def get_unique_subjects(self):
        """
        Extracts all unique subjects using a Python set.
        Demonstrates:
        - Core data structure: set()
        - set.add() method
        - Eliminating duplicates naturally
        """
        subjects_set = set()
        for task in self.tasks:
            subjects_set.add(task.subject)
        return subjects_set

    def get_pending_tasks(self):
        """
        Returns list of tasks with status 'Pending'.
        Demonstrates for loop and conditional checking.
        """
        pending = []
        for task in self.tasks:
            if task.status == "Pending":
                pending.append(task)
        return pending

    def get_completed_tasks(self):
        """
        Returns list of tasks with status 'Completed'.
        Demonstrates for loop and conditional checking.
        """
        completed = []
        for task in self.tasks:
            if task.status == "Completed":
                completed.append(task)
        return completed

    def calculate_summary(self):
        """
        Calculates study statistics using arithmetic operators, mixed division,
        dictionaries, sets, and the Python array data structure.
        Demonstrates:
        - import array and array.array('i')
        - Arithmetic operators (+, -, *, /, //, %)
        - Assignment operators (+=)
        - Relational comparisons (<, >)
        - Dictionary data structure for distribution
        - Set data structure for unique subject count
        """
        total_tasks = len(self.tasks)

        # If there are no tasks, return an empty summary dictionary
        if total_tasks == 0:
            return {
                "total_tasks": 0,
                "completed_tasks": 0,
                "pending_tasks": 0,
                "completion_percentage": 0.0,
                "total_minutes": 0,
                "hours": 0,
                "remaining_minutes": 0,
                "decimal_hours": 0.0,
                "average_minutes": 0.0,
                "min_duration": 0,
                "max_duration": 0,
                "unique_subjects_count": 0,
                "priority_breakdown": {"Low": 0, "Medium": 0, "High": 0}
            }

        # ---------------------------------------------------------
        # Array Data Structure: store durations in a typed array
        # 'i' represents signed integer in Python's array module
        # ---------------------------------------------------------
        duration_array = array.array('i')

        completed_count = 0
        priority_counts = {"Low": 0, "Medium": 0, "High": 0}

        # Populate duration array and compute counts
        for task in self.tasks:
            # Append integer to array
            duration_array.append(task.duration)

            # Count completed
            if task.status == "Completed":
                completed_count += 1

            # Count priority distribution using dictionary
            if task.priority in priority_counts:
                priority_counts[task.priority] += 1

        # Arithmetic operator: subtraction (-)
        pending_count = total_tasks - completed_count

        # Operator precedence & mixed division for completion percentage
        completion_percentage = utils.calculate_percentage(completed_count, total_tasks)

        # Sum of durations using array iteration and assignment addition (+=)
        total_study_minutes = 0
        min_duration = duration_array[0]
        max_duration = duration_array[0]

        for dur in duration_array:
            total_study_minutes += dur
            if dur < min_duration:
                min_duration = dur
            if dur > max_duration:
                max_duration = dur

        # Mixed data type division (/) and floor division (//, %)
        hours, remaining_mins, decimal_hrs = utils.convert_minutes_to_hours(total_study_minutes)
        average_minutes = float(total_study_minutes) / float(total_tasks)

        # Unique subjects using set
        unique_subjects = self.get_unique_subjects()

        summary_dict = {
            "total_tasks": total_tasks,
            "completed_tasks": completed_count,
            "pending_tasks": pending_count,
            "completion_percentage": completion_percentage,
            "total_minutes": total_study_minutes,
            "hours": hours,
            "remaining_minutes": remaining_mins,
            "decimal_hours": round(decimal_hrs, 2),
            "average_minutes": round(average_minutes, 1),
            "min_duration": min_duration,
            "max_duration": max_duration,
            "unique_subjects_count": len(unique_subjects),
            "priority_breakdown": priority_counts
        }

        return summary_dict
