def modify_skin(directory, wear):

    with open(directory, 'r') as file:
        skin = [line.strip('\n').replace('\t', '')
                for line in file.readlines()]
        skin = [line.split('""') for line in skin]

    file.close()

    x_offset_start = None
    y_offset_start = None
    pattern_rotate_start = None
    is_wear = False

    for line in skin:
        if line[0] == '"pattern_offset_x_start':
            x_offset_start = line[1]
        if line[0] == '"pattern_offset_x_end':
            line[1] = x_offset_start

        if line[0] == '"pattern_offset_y_start':
            y_offset_start = line[1]
        if line[0] == '"pattern_offset_y_end':
            line[1] = y_offset_start

        if line[0] == '"pattern_rotate_start':
            pattern_rotate_start = line[1]
        if line[0] == '"pattern_rotate_end':
            line[1] = pattern_rotate_start

        if line[0] == '"wear_remap_min' or line[0] == '"wear_remap_max':
            is_wear = True
            line[1] = f'{wear}"'

        if line[0] == '"dialog_config':
            skin.remove(line)

    if not is_wear:
        last_line = skin.pop()
        skin.append(['"wear_remap_min', f'{wear}"'])
        skin.append(['"wear_remap_max', f'{wear}"'])
        skin.append(last_line)

    skin = ['""'.join(line) for line in skin]
    skin = "\n".join(skin)

    with open("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive"
              "\\__custom_skin\\skin_custom.txt", 'w') as file2:
        file2.write(skin)


if __name__ == "__main__":
    modify_skin(
        r"C:\Users\Anon\Downloads\screenshots\tmp\screenshots\configs\ssg-08-abyss.txt", 1)
