import json


def load_data(file_path):
    """Loads animal data from a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes one animal into an HTML list item."""
    name = animal_obj.get('name')
    char = animal_obj.get('characteristics', {})
    locs = animal_obj.get('locations', [])

    output = '<li class="cards__item">\n'
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <p class="card__text">\n'

    if char.get('diet'):
        output += f"    <strong>Diet:</strong> {char.get('diet')}<br/>\n"
    if locs:
        output += f"    <strong>Location:</strong> {locs[0]}<br/>\n"
    if char.get('type'):
        output += f"    <strong>Type:</strong> {char.get('type')}<br/>\n"

    output += '  </p>\n</li>\n'
    return output


def main():
    """Main controller: Loads data, generates HTML, and writes output file."""
    data = load_data('animals_data.json')

    # Generate HTML content
    animals_html = ""
    for animal in data:
        animals_html += serialize_animal(animal)

    # Replace and write file
    with open('animals_template.html', "r") as f:
        template = f.read()

    final_content = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open("animals.html", "w") as f:
        f.write(final_content)
    print("Successfully generated animals.html")


if __name__ == "__main__":
    main()