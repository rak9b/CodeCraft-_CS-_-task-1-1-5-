from src.password_checker import PasswordChecker

def main():
    """Interactive demo for the Password Strength Checker."""
    checker = PasswordChecker()

    print("Welcome to the Password Strength Checker!")
    print("Enter a password to analyze its strength.")
    print("Type 'q' to quit.\n")

    while True:
        password = input("Enter password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            print("\nGoodbye!")
            break

        # Check the password strength
        strength = checker.check_strength(password)
        print(f"\nPassword Strength: {strength}")

        # Provide improvement suggestions if not strong
        if strength != "Strong":
            suggestions = checker.get_improvement_suggestions(password)
            print("\nSuggestions for improvement:")
            for suggestion in suggestions:
                print(f"- {suggestion}")

        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    main()
