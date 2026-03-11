"""
Grade Calculator — Computes weighted grades, GPA, and letter grades.
"""

from src.student import Student


# ── Grade Scale ──
GRADE_SCALE = {
    "A+": (97, 100),
    "A":  (93, 96),
    "A-": (90, 92),
    "B+": (87, 89),
    "B":  (83, 86),
    "B-": (80, 82),
    "C+": (77, 79),
    "C":  (73, 76),
    "C-": (70, 72),
    "D":  (60, 69),
    "F":  (0, 59),
}

# ── Default Category Weights ──
DEFAULT_WEIGHTS = {
    "homework": 0.20,
    "quiz": 0.15,
    "midterm": 0.25,
    "final": 0.30,
    "participation": 0.10,
}


def calculate_weighted_average(student: Student, weights: dict = None) -> float:
    """
    Calculate the weighted average grade for a student.
    If a category has no grades, it is excluded and weights are redistributed.
    """
    if weights is None:
        weights = DEFAULT_WEIGHTS

    total_weight = 0.0
    weighted_sum = 0.0

    for category, weight in weights.items():
        avg = student.get_category_average(category)
        if avg > 0:
            weighted_sum += avg * weight
            total_weight += weight

    if total_weight == 0:
        return 0.0

    return weighted_sum / total_weight


def score_to_letter(score: float) -> str:
    """Convert a numeric score (0-100) to a letter grade."""
    # BUG: This comparison uses > instead of >= for the lower bound,
    # causing scores exactly at a boundary (e.g., 90.0) to get the wrong grade.
    for letter, (low, high) in GRADE_SCALE.items():
        if low <= score <= high:
            return letter
    return "F"


def calculate_gpa(letter_grade: str) -> float:
    """Convert a letter grade to GPA points (4.0 scale)."""
    gpa_map = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D": 1.0, "F": 0.0,
    }
    return gpa_map.get(letter_grade, 0.0)


def is_honor_roll(student: Student, weights: dict = None) -> bool:
    """Check if a student qualifies for the honor roll (avg >= 90 and attendance >= 90%)."""
    avg = calculate_weighted_average(student, weights)
    return avg >= 90 and student.attendance >= 90


def is_passing(student: Student, weights: dict = None) -> bool:
    """Check if a student is passing (avg >= 60)."""
    avg = calculate_weighted_average(student, weights)
    return avg >= 60


def get_class_statistics(students: list) -> dict:
    """
    Calculate statistics for a list of students.
    Returns: {average, highest, lowest, median, passing_count, honor_count}
    """
    if not students:
        return {
            "average": 0.0,
            "highest": 0.0,
            "lowest": 0.0,
            "median": 0.0,
            "passing_count": 0,
            "honor_count": 0,
            "total_students": 0,
        }

    averages = [calculate_weighted_average(s) for s in students]
    averages.sort()

    n = len(averages)
    if n % 2 == 0:
        median = (averages[n // 2 - 1] + averages[n // 2]) / 2
    else:
        median = averages[n // 2]

    return {
        "average": sum(averages) / len(averages),
        "highest": max(averages),
        "lowest": min(averages),
        "median": median,
        "passing_count": sum(1 for s in students if is_passing(s)),
        "honor_count": sum(1 for s in students if is_honor_roll(s)),
        "total_students": n,
    }
