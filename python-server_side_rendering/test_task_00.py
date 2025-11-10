#!/usr/bin/python3
"""Test file for task_00_intro.py"""

from task_00_intro import generate_invitations

# Read the template from a file
with open('template.txt', 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)

print("\n--- Testing edge cases ---")

# Test with empty template
print("\nTest 1: Empty template")
generate_invitations("", attendees)

# Test with empty attendees
print("\nTest 2: Empty attendees")
generate_invitations(template_content, [])

# Test with invalid template type
print("\nTest 3: Invalid template type")
generate_invitations(123, attendees)

# Test with invalid attendees type
print("\nTest 4: Invalid attendees type (not a list)")
generate_invitations(template_content, "not a list")

# Test with invalid attendees type (list but not of dicts)
print("\nTest 5: Invalid attendees type (list but not of dicts)")
generate_invitations(template_content, [1, 2, 3])

# Test with missing fields
print("\nTest 6: Missing fields")
attendees_missing = [
    {"name": "David"},  # Missing other fields
    {"event_title": "Tech Meetup", "event_location": "Seattle"}  # Missing name and date
]
generate_invitations(template_content, attendees_missing)
