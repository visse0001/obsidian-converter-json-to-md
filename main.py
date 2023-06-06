import json


class Converter:
    def __init__(self, file):
        self.file = file

    def convert_json_to_md(self):

        result = []

        with open(self.file) as file:
            file = json.load(file)
            print(file)

            # loop over file
            for book in file['documents']:

                # Create a new md file
                with open(f'{book["title"]}.md', 'a') as markdown_file:
                    markdown_file.write(f'# {book["title"]} \n')

                    # Loop entries
                    for entry in book['entries']:
                        markdown_file.write(f'## {entry["chapter"]} \n')
                        markdown_file.write('>[!quote] (Enter) >\n')
                        markdown_file.write(f'> {entry["text"]} \n')


converter = Converter('wyciag.json')
converter.convert_json_to_md()
