#!/usr/bin/env python3
"""Interactive demonstration of the Pythagorean numerology system.

This script demonstrates the functional API with simple functions that do not
require class instantiation or shared state.

Key features of v2.0:
- Pure functions with no side effects
- English-only output (no language configuration needed)
- Simple parameter passing (strings and basic types)
- Individual calculation functions can be used independently
- Complete readings available through convenience functions
"""

from numerology import pythagorean as numerology


def demonstrate_individual_calculations():
    """Demonstrate individual calculation functions."""
    print("=" * 60)
    print("INDIVIDUAL CALCULATION FUNCTIONS")
    print("=" * 60)

    # Sample data
    first_name = "John"
    last_name = "Smith"
    birthdate = "1985-03-15"

    print(f"Sample person: {first_name} {last_name}, born {birthdate}")
    print()

    # Individual calculations - each function is independent
    print("Individual Calculations:")
    print("-" * 25)

    destiny = numerology.destiny_number(first_name, last_name)
    print(f"Destiny Number: {destiny}")

    personality = numerology.personality_number(first_name, last_name)
    print(f"Personality Number: {personality}")

    heart_desire = numerology.heart_desire_number(first_name, last_name)
    print(f"Heart Desire Number: {heart_desire}")

    life_path = numerology.life_path_number(birthdate)
    print(f"Life Path Number: {life_path}")
    print()


def demonstrate_interpretations():
    """Demonstrate interpretation functions."""
    print("=" * 60)
    print("INTERPRETATION FUNCTIONS")
    print("=" * 60)

    # Sample numbers
    destiny_num = 7
    personality_num = 3
    heart_desire_num = 11  # Master number example

    print("Sample Interpretations:")
    print("-" * 22)

    # Individual interpretation functions
    destiny_interp = numerology.interpret_destiny_number(destiny_num)
    print(f"Destiny Number {destiny_num} - {destiny_interp['title']}")
    print(f"Description: {destiny_interp['description'][:100]}...")
    print(f"Strengths: {destiny_interp['strengths'][:80]}...")
    print(f"Weaknesses: {destiny_interp['weaknesses'][:80]}...")
    print()

    personality_interp = numerology.interpret_personality_number(personality_num)
    print(f"Personality Number {personality_num} - {personality_interp['title']}")
    print(f"Description: {personality_interp['description'][:100]}...")
    print()

    # Master number interpretation example
    heart_interp = numerology.interpret_heart_desire_number(heart_desire_num)
    print(
        f"Heart Desire Number {heart_desire_num} (Master Number) - "
        f"{heart_interp['title']}"
    )
    print(f"Description: {heart_interp['description'][:100]}...")
    print()


def demonstrate_full_reading():
    """Demonstrate the full_reading convenience function."""
    print("=" * 60)
    print("COMPLETE READING FUNCTION")
    print("=" * 60)

    # Sample data
    first_name = "Sarah"
    last_name = "Johnson"
    birthdate = "1992-07-22"

    print(f"Complete reading for: {first_name} {last_name}, born {birthdate}")
    print()

    # Get complete reading with one function call
    reading = numerology.full_reading(first_name, last_name, birthdate)

    print("Complete Numerology Reading:")
    print("-" * 30)

    # Display all numbers and their interpretations
    print(f"Destiny Number: {reading['destiny']}")
    print(f"  {reading['destiny_interpretation']['title']}")
    print(f"  {reading['destiny_interpretation']['description'][:120]}...")
    print()

    print(f"Personality Number: {reading['personality']}")
    print(f"  {reading['personality_interpretation']['title']}")
    print(f"  {reading['personality_interpretation']['description'][:120]}...")
    print()

    print(f"Heart Desire Number: {reading['heart_desire']}")
    print(f"  {reading['heart_desire_interpretation']['title']}")
    print(f"  {reading['heart_desire_interpretation']['description'][:120]}...")
    print()

    print(f"Life Path Number: {reading['life_path']}")
    print(f"  {reading['life_path_interpretation']['title']}")
    print(f"  {reading['life_path_interpretation']['description'][:120]}...")
    print()


def demonstrate_functional_benefits():
    """Demonstrate the benefits of the functional approach."""
    print("=" * 60)
    print("FUNCTIONAL API BENEFITS")
    print("=" * 60)

    print("1. No class instantiation required:")
    print("   # v1.x: persona = Persona(...); numerology = Numerology(persona)")
    print("   # v2.0: result = numerology.destiny_number('John', 'Smith')")
    print()

    print("2. Functions are pure (no side effects):")
    result1 = numerology.destiny_number("Alice", "Brown")
    result2 = numerology.destiny_number("Alice", "Brown")
    print(f"   Same input always gives same output: {result1} == {result2}")
    print()

    print("3. Functions work independently:")
    print("   # Can call any function without calling others first")
    just_personality = numerology.personality_number("Bob", "Wilson")
    print(f"   personality_number('Bob', 'Wilson') = {just_personality}")
    print()

    print("4. English-only output (no language configuration):")
    interp = numerology.interpret_destiny_number(5)
    print(f"   All text is in English: '{interp['title']}'")
    print()

    print("5. Simple data types (strings, integers, dictionaries):")
    print("   # No complex objects - easy to integrate with other systems")
    print("   # JSON-serializable results")
    print()


def interactive_demo():
    """Interactive demonstration allowing user input."""
    print("=" * 60)
    print("INTERACTIVE DEMO")
    print("=" * 60)

    try:
        print("Enter your information for a personalized reading:")
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        birthdate = input("Birthdate (YYYY-MM-DD): ").strip()

        if not first_name or not last_name or not birthdate:
            print("Please provide all required information.")
            return

        print(f"\nGenerating reading for {first_name} {last_name}...")
        print()

        # Use the full_reading function for complete results
        reading = numerology.full_reading(first_name, last_name, birthdate)

        print("YOUR NUMEROLOGY READING:")
        print("=" * 25)

        for number_type in ["destiny", "personality", "heart_desire", "life_path"]:
            number = reading[number_type]
            if f"{number_type}_interpretation" in reading:
                interp = reading[f"{number_type}_interpretation"]
                print(f"{number_type.replace('_', ' ').title()} Number: {number}")
                print(f"  {interp['title']}")
                print(f"  {interp['description']}")
                print(f"  Strengths: {interp['strengths']}")
                print(f"  Challenges: {interp['weaknesses']}")
                print()
            else:
                print(f"{number_type.replace('_', ' ').title()} Number: {number}")
                print("  (Interpretation not available)")
                print()

    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nDemo cancelled.")


def main():
    """Main demonstration function."""
    print("NUMEROLOGY v2.0 FUNCTIONAL API DEMONSTRATION")
    print("=" * 60)
    print()
    print("This script demonstrates the new v2.0 functional API.")
    print(
        "The v2.0 API provides simple, pure functions for numerological calculations."
    )
    print()

    # Run all demonstrations
    demonstrate_individual_calculations()
    print()

    demonstrate_interpretations()
    print()

    demonstrate_full_reading()
    print()

    demonstrate_functional_benefits()
    print()

    # Ask if user wants interactive demo
    try:
        response = (
            input("Would you like to try the interactive demo? (y/n): ").strip().lower()
        )
        if response in ["y", "yes"]:
            print()
            interactive_demo()
    except KeyboardInterrupt:
        print("\nDemo completed.")

    print()
    print("=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)
    print("For more information, see the numerology package documentation.")
    print("Import with: import numerology")


if __name__ == "__main__":
    main()
