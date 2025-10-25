# String Methods for Checking Numeric and Alphanumeric Content
# ================================================================

def demonstrate_string_methods():
    """Comprehensive demonstration of string checking methods"""
    
    test_strings = [
        "123",      # Basic digits
        "-123",     # Negative number
        "12.3",     # Decimal point
        "½",        # Unicode fraction
        "²",        # Superscript
        "Ⅴ",        # Roman numeral
        "abc123",   # Mixed alphanumeric
        "hello",    # Letters only
        "",         # Empty string
        " ",        # Whitespace
        "٠١٢",      # Arabic-Indic digits
        "௧௨௩",      # Tamil digits
    ]
    
    print("=" * 80)
    print("STRING METHODS COMPARISON")
    print("=" * 80)
    print(f"{'String':<12} {'isdigit()':<10} {'isdecimal()':<12} {'isnumeric()':<12} {'isalnum()':<10} {'isalpha()':<10}")
    print("-" * 80)
    
    for s in test_strings:
        display_s = s if s else "''(empty)"
        display_s = "' '(space)" if s == " " else display_s
        print(f"{display_s:<12} {str(s.isdigit()):<10} {str(s.isdecimal()):<12} {str(s.isnumeric()):<12} {str(s.isalnum()):<10} {str(s.isalpha()):<10}")

def explain_methods():
    """Detailed explanation of each method"""
    
    print("\n" + "=" * 80)
    print("DETAILED EXPLANATIONS")
    print("=" * 80)
    
    print("\n1. str.isdigit():")
    print("   • Returns True if ALL characters are digits (0-9)")
    print("   • Includes Unicode digit characters (like superscripts)")
    print("   • Does NOT accept: negative signs, decimal points, fractions")
    print("   • Use case: Validating simple positive integers")
    print("   Examples:")
    print(f"     '123'.isdigit() = {'123'.isdigit()}")
    print(f"     '-123'.isdigit() = {'-123'.isdigit()}")
    print(f"     '12.3'.isdigit() = {'12.3'.isdigit()}")
    print(f"     '²'.isdigit() = {'²'.isdigit()}  # Unicode superscript")
    
    print("\n2. str.isdecimal():")
    print("   • Returns True if ALL characters are decimal characters (0-9)")
    print("   • Most restrictive - only accepts base-10 digits")
    print("   • Does NOT accept: Unicode digits, fractions, superscripts")
    print("   • Use case: Validating strict decimal numbers")
    print("   Examples:")
    print(f"     '123'.isdecimal() = {'123'.isdecimal()}")
    print(f"     '²'.isdecimal() = {'²'.isdecimal()}  # Superscript not accepted")
    print(f"     '½'.isdecimal() = {'½'.isdecimal()}  # Fraction not accepted")
    
    print("\n3. str.isnumeric():")
    print("   • Returns True if ALL characters have numeric value")
    print("   • Most permissive - accepts digits, fractions, superscripts, etc.")
    print("   • Includes Unicode numeric characters")
    print("   • Use case: Broad numeric validation including Unicode")
    print("   Examples:")
    print(f"     '123'.isnumeric() = {'123'.isnumeric()}")
    print(f"     '½'.isnumeric() = {'½'.isnumeric()}  # Fraction accepted")
    print(f"     '²'.isnumeric() = {'²'.isnumeric()}  # Superscript accepted")
    print(f"     'Ⅴ'.isnumeric() = {'Ⅴ'.isnumeric()}  # Roman numeral accepted")
    
    print("\n4. str.isalnum():")
    print("   • Returns True if ALL characters are alphanumeric (letters or digits)")
    print("   • Combines isalpha() and isdigit() functionality")
    print("   • Use case: Validating usernames, IDs, codes")
    print("   Examples:")
    print(f"     'abc123'.isalnum() = {'abc123'.isalnum()}")
    print(f"     'hello'.isalnum() = {'hello'.isalnum()}")
    print(f"     '123'.isalnum() = {'123'.isalnum()}")
    print(f"     'hello!'.isalnum() = {'hello!'.isalnum()}  # Special char rejected")
    
    print("\n5. str.isalpha():")
    print("   • Returns True if ALL characters are letters")
    print("   • Use case: Validating names, pure text")
    print("   Examples:")
    print(f"     'hello'.isalpha() = {'hello'.isalpha()}")
    print(f"     'hello123'.isalpha() = {'hello123'.isalpha()}")

def practical_use_cases():
    """Show practical use cases for each method"""
    
    print("\n" + "=" * 80)
    print("PRACTICAL USE CASES")
    print("=" * 80)
    
    def validate_age(age_str):
        """Use isdecimal() for age validation - strict decimal only"""
        if age_str.isdecimal() and 0 <= int(age_str) <= 150:
            return True
        return False
    
    def validate_username(username):
        """Use isalnum() for username - letters and numbers only"""
        return username.isalnum() and len(username) >= 3
    
    def extract_digits_from_text(text):
        """Use isdigit() to extract digit characters"""
        digits = ''.join(char for char in text if char.isdigit())
        return digits
    
    def validate_unicode_number(num_str):
        """Use isnumeric() for international number formats"""
        return num_str.isnumeric()
    
    print("\n1. Age Validation (using isdecimal()):")
    test_ages = ["25", "abc", "12.5", "-5", "200"]
    for age in test_ages:
        result = validate_age(age)
        print(f"   Age '{age}': {'Valid' if result else 'Invalid'}")
    
    print("\n2. Username Validation (using isalnum()):")
    test_usernames = ["user123", "user_123", "user", "ab", "hello!"]
    for username in test_usernames:
        result = validate_username(username)
        print(f"   Username '{username}': {'Valid' if result else 'Invalid'}")
    
    print("\n3. Extract Digits from Text (using isdigit()):")
    test_texts = ["Phone: +1-555-123-4567", "Price: $12.99", "Code: ABC123XYZ"]
    for text in test_texts:
        digits = extract_digits_from_text(text)
        print(f"   Text: '{text}' → Digits: '{digits}'")
    
    print("\n4. Unicode Number Validation (using isnumeric()):")
    unicode_numbers = ["123", "½", "²", "Ⅴ", "abc"]
    for num in unicode_numbers:
        result = validate_unicode_number(num)
        print(f"   '{num}': {'Valid numeric' if result else 'Not numeric'}")

def method_hierarchy():
    """Show the relationship between methods"""
    
    print("\n" + "=" * 80)
    print("METHOD HIERARCHY (from most restrictive to most permissive)")
    print("=" * 80)
    
    print("\nisdecimal() ⊆ isdigit() ⊆ isnumeric()")
    print("     ↓           ↓           ↓")
    print("  [0-9] only   Unicode     All numeric")
    print("              digits      characters")
    
    print("\nWhen to use which:")
    print("• isdecimal(): Parsing user input for integers, ages, counts")
    print("• isdigit():   General digit validation, phone numbers")
    print("• isnumeric(): International applications, Unicode support")
    print("• isalnum():   Usernames, product codes, alphanumeric IDs")
    print("• isalpha():   Names, pure text validation")

if __name__ == "__main__":
    demonstrate_string_methods()
    explain_methods()
    practical_use_cases()
    method_hierarchy()

