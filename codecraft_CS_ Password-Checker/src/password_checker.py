import re
from typing import Dict, Literal

class PasswordChecker:
    def __init__(self, min_length: int = 8):
        self.min_length = min_length

    def check_requirements(self, password: str) -> Dict[str, bool]:
        """
        Check individual password requirements.
        Returns a dictionary with the results of each check.
        """
        return {
            'length': len(password) >= self.min_length,
            'lowercase': bool(re.search(r'[a-z]', password)),
            'uppercase': bool(re.search(r'[A-Z]', password)),
            'digit': bool(re.search(r'\d', password)),
            'special': bool(re.search(r'[!@#$%^&*]', password))
        }

    def check_strength(self, password: str) -> Literal['Weak', 'Moderate', 'Strong']:
        """
        Evaluate the overall strength of a password.
        Returns one of: 'Weak', 'Moderate', 'Strong'.
        """
        checks = self.check_requirements(password)
        score = sum(checks.values())
        if score < 3:
            return "Weak"
        elif score < 5:
            return "Moderate"
        return "Strong"

    def get_improvement_suggestions(self, password: str) -> list[str]:
        """
        Provide specific suggestions for improving password strength.
        Returns a list of actionable recommendations.
        """
        checks = self.check_requirements(password)
        suggestions = []
        if not checks['length']:
            suggestions.append(f"Make password at least {self.min_length} characters long")
        if not checks['lowercase']:
            suggestions.append("Add lowercase letters")
        if not checks['uppercase']:
            suggestions.append("Add uppercase letters")
        if not checks['digit']:
            suggestions.append("Add numbers")
        if not checks['special']:
            suggestions.append("Add special characters (!@#$%^&*)")
        return suggestions
