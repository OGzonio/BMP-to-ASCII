def read_bmp(filename):
    with open(filename, 'rb') as f:
        # read bmp file
        header = f.read(54)
        # extract width,height and off
        width = int.from_bytes(header[18:22], byteorder='little')
        height = int.from_bytes(header[22:26], byteorder='little')
        offset = int.from_bytes(header[10:14], byteorder='little')

        # bytes in each row
        row_bytes = ((width * 24 + 31) // 32) * 4

        # read pixel data
        f.seek(offset)
        pixels = []
        for y in range(height):
            row = []
            for x in range(width):
                # read rgb for current pixel
                blue = int.from_bytes(f.read(1), byteorder='little')
                green = int.from_bytes(f.read(1), byteorder='little')
                red = int.from_bytes(f.read(1), byteorder='little')
                # add pixel to row
                row.append((red, green, blue))
            # add row to matrix
            pixels.append(row)
            # adjust pointer
            f.seek(row_bytes - (width * 3), 1)

    return pixels


pixels = read_bmp('rgb.bmp')
for i in range(len(pixels)):
    print (type(pixels[i]))