"""
Tests for the Student model.
"""

import pytest
from src.student import Student


class TestStudentCreation:
    """Tests for creating Student objects."""

    def test_create_student_basic(self):
        s = Student("Alice Johnson", "STU001")
        assert s.name == "Alice Johnson"
        assert s.student_id == "STU001"
        assert s.email == ""
        assert s.grades == {}

    def test_create_student_with_email(self):
        s = Student("Bob Smith", "STU002", "bob@school.edu")
        assert s.email == "bob@school.edu"

    def test_create_student_strips_whitespace(self):
        s = Student("  Charlie Brown  ", "  STU003  ")
        assert s.name == "Charlie Brown"
        assert s.student_id == "STU003"

    def test_create_student_empty_name_raises(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Student("", "STU004")

    def test_create_student_empty_id_raises(self):
        with pytest.raises(ValueError, match="ID cannot be empty"):
            Student("Diana", "")


class TestStudentGrades:
    """Tests for adding and retrieving grades."""

    def test_add_single_grade(self):
        s = Student("Eve", "STU005")
        s.add_grade("homework", 85.0)
        assert s.grades["homework"] == [85.0]

    def test_add_multiple_grades_same_category(self):
        s = Student("Frank", "STU006")
        s.add_grade("quiz", 90.0)
        s.add_grade("quiz", 80.0)
        s.add_grade("quiz", 70.0)
        assert len(s.grades["quiz"]) == 3

    def test_add_grades_different_categories(self):
        s = Student("Grace", "STU007")
        s.add_grade("homework", 85.0)
        s.add_grade("exam", 92.0)
        assert "homework" in s.grades
        assert "exam" in s.grades

    def test_add_grade_invalid_score_negative(self):
        s = Student("Henry", "STU008")
        with pytest.raises(ValueError, match="between 0 and 100"):
            s.add_grade("homework", -5.0)

    def test_add_grade_invalid_score_over_100(self):
        s = Student("Ivy", "STU009")
        with pytest.raises(ValueError, match="between 0 and 100"):
            s.add_grade("homework", 105.0)

    def test_add_grade_empty_category_raises(self):
        s = Student("Jack", "STU010")
        with pytest.raises(ValueError, match="Category cannot be empty"):
            s.add_grade("", 85.0)

    def test_category_average(self):
        s = Student("Kate", "STU011")
        s.add_grade("homework", 80.0)
        s.add_grade("homework", 90.0)
        s.add_grade("homework", 100.0)
        assert s.get_category_average("homework") == 90.0

    def test_category_average_nonexistent(self):
        s = Student("Leo", "STU012")
        assert s.get_category_average("midterm") == 0.0

    def test_get_all_scores(self):
        s = Student("Mia", "STU013")
        s.add_grade("homework", 80.0)
        s.add_grade("quiz", 90.0)
        s.add_grade("exam", 75.0)
        all_scores = s.get_all_scores()
        assert len(all_scores) == 3
        assert 80.0 in all_scores
        assert 90.0 in all_scores
        assert 75.0 in all_scores


class TestStudentAttendance:
    """Tests for attendance tracking."""

    def test_set_attendance(self):
        s = Student("Noah", "STU014")
        s.set_attendance(95.5)
        assert s.attendance == 95.5

    def test_set_attendance_zero(self):
        s = Student("Olivia", "STU015")
        s.set_attendance(0)
        assert s.attendance == 0

    def test_set_attendance_hundred(self):
        s = Student("Paul", "STU016")
        s.set_attendance(100)
        assert s.attendance == 100

    def test_set_attendance_negative_raises(self):
        s = Student("Quinn", "STU017")
        with pytest.raises(ValueError):
            s.set_attendance(-1)

    def test_set_attendance_over_100_raises(self):
        s = Student("Rachel", "STU018")
        with pytest.raises(ValueError):
            s.set_attendance(101)
