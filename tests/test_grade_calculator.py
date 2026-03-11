"""
Tests for the Grade Calculator.

NOTE: This file contains an INTENTIONAL BUG for demo purposes.
      test_honor_roll_boundary will FAIL because of a calculation edge case.
      This is designed to trigger the Self-Healing CI/CD Engine.
"""

import pytest
from src.student import Student
from src.grade_calculator import (
    calculate_weighted_average,
    score_to_letter,
    calculate_gpa,
    is_honor_roll,
    is_passing,
    get_class_statistics,
)


# ── Helper: create a student with grades ──
def _make_student(name, sid, grades_dict, attendance=95):
    s = Student(name, sid)
    for category, scores in grades_dict.items():
        for score in scores:
            s.add_grade(category, score)
    s.set_attendance(attendance)
    return s


class TestWeightedAverage:
    """Tests for weighted average calculation."""

    def test_single_category(self):
        s = _make_student("Alice", "S01", {"homework": [80, 90, 100]})
        avg = calculate_weighted_average(s)
        assert avg == 90.0  # Only homework exists, so it's the full average

    def test_multiple_categories(self):
        s = _make_student("Bob", "S02", {
            "homework": [80],
            "quiz": [90],
            "midterm": [70],
            "final": [85],
            "participation": [100],
        })
        avg = calculate_weighted_average(s)
        # Expected: (80*0.20 + 90*0.15 + 70*0.25 + 85*0.30 + 100*0.10) / 1.0
        expected = 80 * 0.20 + 90 * 0.15 + 70 * 0.25 + 85 * 0.30 + 100 * 0.10
        assert round(avg, 2) == round(expected, 2)

    def test_missing_categories_redistributed(self):
        s = _make_student("Charlie", "S03", {"homework": [90], "final": [80]})
        avg = calculate_weighted_average(s)
        # Only homework (0.20) and final (0.30) exist → weights sum to 0.50
        expected = (90 * 0.20 + 80 * 0.30) / 0.50
        assert round(avg, 2) == round(expected, 2)

    def test_no_grades_returns_zero(self):
        s = Student("Diana", "S04")
        assert calculate_weighted_average(s) == 0.0

    def test_custom_weights(self):
        s = _make_student("Eve", "S05", {"project": [95], "exam": [85]})
        custom = {"project": 0.40, "exam": 0.60}
        avg = calculate_weighted_average(s, custom)
        expected = (95 * 0.40 + 85 * 0.60) / 1.0
        assert round(avg, 2) == round(expected, 2)


class TestLetterGrade:
    """Tests for score to letter grade conversion."""

    def test_a_plus(self):
        assert score_to_letter(98) == "A+"

    def test_a(self):
        assert score_to_letter(95) == "A"

    def test_b_plus(self):
        assert score_to_letter(88) == "B+"

    def test_c(self):
        assert score_to_letter(75) == "C"

    def test_f(self):
        assert score_to_letter(50) == "F"

    def test_boundary_a_minus(self):
        """Score of exactly 90 should give A-"""
        assert score_to_letter(90) == "A-"

    def test_boundary_b_plus_87(self):
        """Score of exactly 87 should give B+"""
        assert score_to_letter(87) == "B+"


class TestGPA:
    """Tests for letter-to-GPA conversion."""

    def test_gpa_a(self):
        assert calculate_gpa("A") == 4.0

    def test_gpa_b_plus(self):
        assert calculate_gpa("B+") == 3.3

    def test_gpa_f(self):
        assert calculate_gpa("F") == 0.0

    def test_gpa_invalid(self):
        assert calculate_gpa("Z") == 0.0


class TestHonorRoll:
    """Tests for honor roll determination."""

    def test_honor_roll_high_grades_high_attendance(self):
        s = _make_student("Frank", "S06", {"homework": [95, 98, 92]}, attendance=95)
        assert is_honor_roll(s) is True

    def test_not_honor_roll_low_grades(self):
        s = _make_student("Grace", "S07", {"homework": [70, 75, 80]}, attendance=95)
        assert is_honor_roll(s) is False

    def test_not_honor_roll_low_attendance(self):
        s = _make_student("Henry", "S08", {"homework": [95, 98, 92]}, attendance=80)
        assert is_honor_roll(s) is False

    def test_honor_roll_boundary(self):
        """
        INTENTIONAL FAILING TEST — For Demo Purposes!
        Student with exactly 90% average and 90% attendance should qualify.
        But the test expects True while the student has 89.5% avg.
        The AI should detect this is a test logic bug and suggest correcting
        the test data so the student actually gets a 90% average.
        """
        s = _make_student("Ivy", "S09", {"homework": [89, 90]}, attendance=90)
        # Average of [89, 90] = 89.5 which is < 90, so is_honor_roll returns False
        # But the test incorrectly expects True
        assert is_honor_roll(s) is True


class TestPassing:
    """Tests for pass/fail determination."""

    def test_passing_student(self):
        s = _make_student("Jack", "S10", {"homework": [75, 80, 85]})
        assert is_passing(s) is True

    def test_failing_student(self):
        s = _make_student("Kate", "S11", {"homework": [40, 50, 55]})
        assert is_passing(s) is False

    def test_boundary_60(self):
        s = _make_student("Leo", "S12", {"homework": [60]})
        assert is_passing(s) is True


class TestClassStatistics:
    """Tests for class-wide statistics."""

    def test_statistics_multiple_students(self):
        students = [
            _make_student("M1", "S20", {"homework": [90]}),
            _make_student("M2", "S21", {"homework": [80]}),
            _make_student("M3", "S22", {"homework": [70]}),
        ]
        stats = get_class_statistics(students)
        assert stats["total_students"] == 3
        assert round(stats["average"], 1) == 80.0
        assert stats["highest"] == 90.0
        assert stats["lowest"] == 70.0
        assert stats["median"] == 80.0
        assert stats["passing_count"] == 3

    def test_statistics_empty_class(self):
        stats = get_class_statistics([])
        assert stats["total_students"] == 0
        assert stats["average"] == 0.0
