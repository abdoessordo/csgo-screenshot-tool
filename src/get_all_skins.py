import sys

def get_all_skins():
    try:
        base_directory, output_directory = sys.argv[1::]
    except:
        print("2 Arguments Needed")

    

    with open(base_directory, "r") as all_skins_file:
        all_skins = [line.strip('\n') for line in all_skins_file.readlines()]

    all_skins_file.close()

    base_directory = base_directory.split('\\')
    file_name = base_directory.pop()
    base_directory = "\\".join(base_directory)

    if file_name == "base_guns.txt":
        run_type = "basic"
    elif file_name == "base_knives.txt":
        run_type = "mod"

    return all_skins, base_directory, output_directory, run_type
