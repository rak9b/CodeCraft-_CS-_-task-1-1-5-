import pytest
from src.password_checker import PasswordChecker

@pytest.fixture
def checker():
    """Fixture to provide a PasswordChecker instance."""
    return PasswordChecker()

def test_weak_password(checker):
    """Test a password classified as weak."""
    assert checker.check_strength("weak") == "Weak"

def test_moderate_password(checker):
    """Test a password classified as moderate."""
    assert checker.check_strength("Moderate1") == "Moderate"

def test_strong_password(checker):
    """Test a password classified as strong."""
    assert checker.check_strength("Str0ng@Pass") == "Strong"

def test_requirements(checker):
    """Test the individual requirements of a password."""
    checks = checker.check_requirements("Test1@")
    assert checks['uppercase']
    assert checks['lowercase']
    assert checks['digit']
    assert checks['special']
    assert not checks['length']

def test_suggestions(checker):
    """Test the suggestions provided for improving password strength."""
    suggestions = checker.get_improvement_suggestions("weak")
    assert len(suggestions) > 0
    assert "Add uppercase letters" in suggestions
    assert "Add numbers" in suggestions
