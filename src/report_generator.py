"""
Report Generator — Creates formatted grade reports for students.
"""

from src.student import Student
from src.grade_calculator import (
    calculate_weighted_average,
    score_to_letter,
    calculate_gpa,
    is_honor_roll,
    is_passing,
)


def generate_student_report(student: Student) -> str:
    """Generate a formatted text report for a single student."""
    avg = calculate_weighted_average(student)
    letter = score_to_letter(avg)
    gpa = calculate_gpa(letter)
    honor = is_honor_roll(student)
    passing = is_passing(student)

    lines = [
        "=" * 50,
        f"  STUDENT GRADE REPORT",
        "=" * 50,
        f"  Name:       {student.name}",
        f"  ID:         {student.student_id}",
        f"  Email:      {student.email or 'N/A'}",
        f"  Attendance: {student.attendance}%",
        "-" * 50,
        "  GRADES BY CATEGORY:",
    ]

    for category, scores in student.grades.items():
        avg_cat = student.get_category_average(category)
        lines.append(f"    {category.title():15s} → Avg: {avg_cat:.1f}  ({len(scores)} scores)")

    lines.extend([
        "-" * 50,
        f"  Weighted Average:  {avg:.1f}%",
        f"  Letter Grade:      {letter}",
        f"  GPA:               {gpa:.1f}",
        f"  Passing:           {'Yes' if passing else 'No'}",
        f"  Honor Roll:        {'⭐ Yes' if honor else 'No'}",
        "=" * 50,
    ])

    return "\n".join(lines)


def generate_summary_line(student: Student) -> str:
    """Generate a one-line summary for a student."""
    avg = calculate_weighted_average(student)
    letter = score_to_letter(avg)
    status = "PASS" if is_passing(student) else "FAIL"
    honor = " ⭐" if is_honor_roll(student) else ""
    return f"{student.student_id} | {student.name:20s} | {avg:5.1f}% | {letter:2s} | {status}{honor}"


def generate_class_roster(students: list) -> str:
    """Generate a formatted roster showing all students."""
    if not students:
        return "No students enrolled."

    header = f"{'ID':8s} | {'Name':20s} | {'Avg':>6s} | {'Grade':2s} | Status"
    separator = "-" * len(header)

    lines = [header, separator]
    for student in sorted(students, key=lambda s: calculate_weighted_average(s), reverse=True):
        lines.append(generate_summary_line(student))

    return "\n".join(lines)
