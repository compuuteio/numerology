from numerology import Pythagorean
from numerology import Chaldean
from numerology import Vedic

def start_app():
    """Interactive version of the package."""
    print("Starting...\n")

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    birthdate = input("Enter your birthdate (yyyy-MM-dd, example 1994-11-30): ")

    Pythagorean(first_name, last_name, birthdate)
    Chaldean(first_name, last_name, birthdate)
    Vedic(first_name, last_name, birthdate)

if __name__ == "__main__":
    start_app()
