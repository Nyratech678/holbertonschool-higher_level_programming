#!/usr/bin/python3
"""Module for generating personalized invitation files from a template."""


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template.

    Args:
        template (str): A string template with placeholders.
        attendees (list): A list of dictionaries containing attendee data.

    Error Handling:
        - Validates that template is a string and attendees is a list of dicts.
        - Checks for empty template or empty attendees list.
        - Replaces missing values with "N/A" in the output.
    """
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: template should be a string")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list):
        print("Error: attendees should be a list of dictionaries")
        return

    # Verify all items in attendees are dictionaries
    if attendees and not all(isinstance(item, dict) for item in attendees):
        print("Error: attendees should be a list of dictionaries")
        return

    # Check if template is empty
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for this attendee
        output_content = template

        # Replace placeholders with values or "N/A" if missing
        # Handle name
        name = attendee.get('name')
        if name is None or name == '':
            name = "N/A"
        output_content = output_content.replace('{name}', str(name))

        # Handle event_title
        event_title = attendee.get('event_title')
        if event_title is None or event_title == '':
            event_title = "N/A"
        output_content = output_content.replace('{event_title}',
                                                str(event_title))

        # Handle event_date
        event_date = attendee.get('event_date')
        if event_date is None or event_date == '':
            event_date = "N/A"
        output_content = output_content.replace('{event_date}',
                                                str(event_date))

        # Handle event_location
        event_location = attendee.get('event_location')
        if event_location is None or event_location == '':
            event_location = "N/A"
        output_content = output_content.replace('{event_location}',
                                                str(event_location))

        # Generate output filename
        filename = f"output_{index}.txt"

        # Write to file
        try:
            with open(filename, 'w') as file:
                file.write(output_content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
