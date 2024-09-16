import urllib.parse
import re
from response import run_query

def validate_query_string(query_string):
    """Validates a query string for special characters.

    Args:
        query_string (str): The query string to validate.

    Returns:
        bool: True if the query string is valid, False otherwise.
    """

    # Decode the query string to handle potential encoding issues
    decoded_query = urllib.parse.unquote(query_string)

    # Use a regular expression to match allowed characters.
    # Adjust the pattern to include or exclude specific characters as needed.
    allowed_pattern = r'^[a-zA-Z0-9_\-\.\/:\s\?]+$'

    # Check if the decoded query matches the allowed pattern
    if re.match(allowed_pattern, decoded_query):
        return True
    else:
        return False
    
query_string = "My name is mohit?"

if validate_query_string(query_string):
    # Process the query string if it's valid
    print("Query string is valid.")
else:
    print("Query string contains invalid characters.")