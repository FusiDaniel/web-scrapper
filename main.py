from bs4 import BeautifulSoup
import os


def html_to_dictionary(file_path, output_directory):
    with open(file_path, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    span_elements = soup.find_all('span', class_='css-jhjqlk')

    result = {}

    os.makedirs(output_directory, exist_ok=True)

    for span in span_elements:
        div = span.find('div')
        icon_name = div.text.strip()

        svg = span.find('svg').prettify()
        svg_lines = str(svg).split('\n')
        svg_lines[0] = f'<svg title="{icon_name}" viewBox="0 0 24 24">'
        svg = '\n'.join(svg_lines)
        # Generate the output file path
        file_name = f'{icon_name}.svg'
        file_path = os.path.join(output_directory, file_name)

        # Write the SVG content to the output file
        with open(file_path, 'w') as file:
            file.write(str(svg))

        print(f'SVG file created: {file_path}')

    return result


# Example usage
file_path = 'sharp.html'
output_directory = 'sharp'
html_to_dictionary(file_path, output_directory)
