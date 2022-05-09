import sys
import json


def get_all_skins():
    try:
        base_directory, output_directory = sys.argv[1::]
    except:
        print("2 arguments required")
        sys.exit()

    with open(base_directory, "r") as all_skins_file:
        all_skins = json.load(all_skins_file)

    all_skins_file.close()

    base_directory = base_directory.split('\\')
    base_directory.pop()
    base_directory = "\\".join(base_directory)

    return all_skins, base_directory, output_directory
