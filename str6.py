import re

def match_string(pattern, text):
    return bool(re.fullmatch(pattern, text))  # Returns True if the entire string matches

# Example usage
pattern = r"\d{3}-\d{2}-\d{4}"  # Pattern for a format like "123-45-6789"
text1 = "123-45-6789"
text2 = "123456789"

print(match_string(pattern, text1))  # Output: True (matches the pattern)
print(match_string(pattern, text2))  # Output: False (does not match)