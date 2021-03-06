from numerology import PythagoreanNumerology


def start_app():
    """Interactive version of the package."""
    print("Starting...\n")
    
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    birthdate = input("Enter your birthdate (yyyy-MM-dd, example 1994-11-30): ")
    
    my_pythagorean_numerology = PythagoreanNumerology(first_name, last_name, birthdate)

if __name__ == "__main__":
    start_app()