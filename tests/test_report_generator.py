"""
Tests for the Report Generator.
"""

from src.student import Student
from src.report_generator import (
    generate_student_report,
    generate_summary_line,
    generate_class_roster,
)
from src.grade_calculator import calculate_weighted_average


def _make_student(name, sid, grades_dict, attendance=95, email=""):
    s = Student(name, sid, email)
    for category, scores in grades_dict.items():
        for score in scores:
            s.add_grade(category, score)
    s.set_attendance(attendance)
    return s


class TestStudentReport:
    """Tests for individual student report generation."""

    def test_report_contains_name(self):
        s = _make_student("Alice", "STU001", {"homework": [90]}, email="alice@school.edu")
        report = generate_student_report(s)
        assert "Alice" in report

    def test_report_contains_id(self):
        s = _make_student("Bob", "STU002", {"homework": [85]})
        report = generate_student_report(s)
        assert "STU002" in report

    def test_report_contains_grade_info(self):
        s = _make_student("Charlie", "STU003", {"homework": [80, 90]})
        report = generate_student_report(s)
        assert "Weighted Average" in report
        assert "Letter Grade" in report
        assert "GPA" in report

    def test_report_shows_honor_roll(self):
        s = _make_student("Diana", "STU004", {"homework": [95, 98, 100]}, attendance=98)
        report = generate_student_report(s)
        assert "⭐ Yes" in report

    def test_report_shows_passing(self):
        s = _make_student("Eve", "STU005", {"homework": [75, 80]})
        report = generate_student_report(s)
        assert "Passing" in report


class TestSummaryLine:
    """Tests for one-line student summary."""

    def test_summary_contains_student_info(self):
        s = _make_student("Frank", "STU006", {"homework": [88]})
        line = generate_summary_line(s)
        assert "STU006" in line
        assert "Frank" in line

    def test_summary_shows_pass_status(self):
        s = _make_student("Grace", "STU007", {"homework": [80]})
        line = generate_summary_line(s)
        assert "PASS" in line

    def test_summary_shows_fail_status(self):
        s = _make_student("Henry", "STU008", {"homework": [40]})
        line = generate_summary_line(s)
        assert "FAIL" in line


class TestClassRoster:
    """Tests for class roster generation."""

    def test_roster_with_students(self):
        students = [
            _make_student("S1", "ID1", {"homework": [90]}),
            _make_student("S2", "ID2", {"homework": [80]}),
        ]
        roster = generate_class_roster(students)
        assert "S1" in roster
        assert "S2" in roster

    def test_roster_empty_class(self):
        roster = generate_class_roster([])
        assert "No students enrolled" in roster

    def test_roster_sorted_by_average_descending(self):
        students = [
            _make_student("Low", "ID1", {"homework": [60]}),
            _make_student("High", "ID2", {"homework": [95]}),
            _make_student("Mid", "ID3", {"homework": [80]}),
        ]
        roster = generate_class_roster(students)
        lines = roster.strip().split("\n")
        # Skip header and separator (first 2 lines)
        data_lines = lines[2:]
        assert "High" in data_lines[0]  # Highest average should be first
        assert "Low" in data_lines[2]   # Lowest should be last
