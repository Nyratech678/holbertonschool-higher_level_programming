#!/usr/bin/python3
import jinja2

def generate_invitations(template: str, attendees: list):
    if not isinstance(template, str):
        print("Error: template should be a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: attendees should be a list of dictionaries")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    env = jinja2.Environment(loader=jinja2.BaseLoader())
    jinja_template = env.from_string(template)

    for idx, attendee in enumerate(attendees, 1):
        context = {
            key: attendee.get(key) if attendee.get(key) not in [None, ''] else "N/A"
            for key in ['name', 'event_title', 'event_date', 'event_location']
        }
        rendered = jinja_template.render(context)
        filename = f"output_{idx}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(rendered)
        except Exception as e:
            print(f"Failed to write file {filename}: {e}")
