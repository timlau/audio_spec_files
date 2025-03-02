#!/usr/bin/python

from pathlib import Path
import jinja2
import argparse
import re
from datetime import datetime

# Set up argument parser
parser = argparse.ArgumentParser(description='Tool to create the needed files for a new plugin')
parser.add_argument('name',  help='Name of the plugin')
parser.add_argument('version',  help='Version of the plugin')
parser.add_argument('github_url',  help='GitHub url of the project')
args = parser.parse_args()

URL_MATCH = re.compile(r"https\:\/\/github\.com/(.*)/(.*)")
# https://github.com/giorgio-natale/FirComp
 
found = URL_MATCH.match(args.github_url)
if len(found.groups()) != 2:
    print(f"Can't parse url : {args.github_url}")

# Define the data to populate the template
template_data = {
    "name": args.name,
    "version": args.version,
    "github_url": args.github_url,
    "github_owner": found.groups()[0],
    "github_project": found.groups()[1],
    "changelog_date": datetime.now().strftime('%a %b %d %Y')
}

# List of template files to process
template_files = [
    Path('./docs/plugin_template/new-plugin.spec'),
    Path('./docs/plugin_template/Makefile')
]

output_path = Path(f"./plugins/{args.name}")
output_path.mkdir()


# Process each template file
for template_file_path in template_files:
    # Load the template from a file
    with open(template_file_path, 'r') as file:
        template_content = file.read()

    # Create a Jinja2 template object
    template = jinja2.Template(template_content)

    # Render the template with the provided data
    rendered_content = template.render(template_data)

    # Define the output file path
    file_name = template_file_path.name
    match file_name:
        case "new-plugin.spec":
            output_file_path = output_path / f"{args.name}.spec"
        case _:
            output_file_path = output_path / template_file_path.name


    # Write the rendered content to the output file
    with open(output_file_path, 'w') as file:
        file.write(rendered_content)

    print(f"new project file saved to {output_file_path}")