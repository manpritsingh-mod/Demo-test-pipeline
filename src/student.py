"""
Student Model — Represents a student with grades.
"""


class Student:
    """A student with a name, ID, and grades across categories."""

    def __init__(self, name: str, student_id: str, email: str = ""):
        if not name or not name.strip():
            raise ValueError("Student name cannot be empty")
        if not student_id or not student_id.strip():
            raise ValueError("Student ID cannot be empty")

        self.name = name.strip()
        self.student_id = student_id.strip()
        self.email = email.strip()
        self.grades = {}       # category -> list of scores
        self.attendance = 0    # percentage 0-100

    def add_grade(self, category: str, score: float):
        """Add a grade score to a category (e.g., 'homework', 'exam')."""
        if not category:
            raise ValueError("Category cannot be empty")
        if score < 0 or score > 100:
            raise ValueError(f"Score must be between 0 and 100, got {score}")

        if category not in self.grades:
            self.grades[category] = []
        self.grades[category].append(score)

    def get_category_average(self, category: str) -> float:
        """Get the average score for a specific category."""
        if category not in self.grades or not self.grades[category]:
            return 0.0
        return sum(self.grades[category]) / len(self.grades[category])

    def get_all_scores(self) -> list:
        """Get all scores across all categories as a flat list."""
        all_scores = []
        for scores in self.grades.values():
            all_scores.extend(scores)
        return all_scores

    def set_attendance(self, percentage: float):
        """Set attendance percentage (0-100)."""
        if percentage < 0 or percentage > 100:
            raise ValueError(f"Attendance must be between 0 and 100, got {percentage}")
        self.attendance = percentage

    def __repr__(self):
        return f"Student(name='{self.name}', id='{self.student_id}')"
