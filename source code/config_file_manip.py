def modify_skin(directory, x_offset, y_offset, rotation, wear):

    with open(directory, 'r') as file:
        skin = [line.strip('\n').replace('\t', '')
                for line in file.readlines()]
        # bottom = skin[2::]
        skin = [line.split('""') for line in skin]

    file.close()

    for line in skin:
        if line[0] == '"pattern_offset_x_start' or line[0] == '"pattern_offset_x_end':
            line[1] = f'{x_offset}"'

        if line[0] == '"pattern_offset_y_start' or line[0] == '"pattern_offset_y_end':
            line[1] = f'{y_offset}"'

        if line[0] == '"pattern_rotate_start' or line[0] == '"pattern_rotate_end':
            line[1] = f'{rotation}"'

        if line[0] == '"wear_remap_min' or line[0] == '"wear_remap_max':
            line[1] = f'{wear}"'

    skin = [('""').join(line) for line in skin]
    skin = "\n".join(skin)

    with open("C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\__custom_skin\skin_custom.txt", 'w') as file2:
        file2.write(skin)
