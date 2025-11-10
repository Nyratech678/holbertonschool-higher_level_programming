#!/usr/bin/python3
import jinja2

def render_template(template_name: str, context: dict) -> str:
    """
    Renders a Jinja2 template with the given context.

    Args:
        template_name (str): The name of the template file.
        context (dict): A dictionary containing variables to be used in the template.

    Returns:
        str: The rendered template as a string.
    """
    # Create a Jinja2 environment with the file system loader
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

    # Load the specified template
    template = env.get_template(template_name)

    # Render the template with the provided context
    rendered_content = template.render(context)

    return rendered_content

def generate_invitations(template, attendees):
    import os
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
    
    for idx, attendee in enumerate(attendees, 1):
        context = {key: attendee.get(key, 'N/A') if attendee.get(key) is not None else "N/A" for key in ['name', 'event_title', 'event_date', 'event_location']}
        jinja_template = env.from_string(template)
        rendered = jinja_template.render(context)
        filename = f"output_{idx}.txt"
        with open(filename, 'w') as f:
            f.write(rendered)
