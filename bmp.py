import math 

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
                row.append([red, green, blue])
            # add row to matrix
            pixels.append(row)
            # adjust pointer
            f.seek(row_bytes - (width * 3), 1)

    return pixels

def arr_to_ascii(pixels):
    bias_colors = int(765/4)
    chars = list('!@$%&*+_=`xXo,.?/<~|QaAEK:abvcfgh')
    clusters =  list(range(0, 766, bias_colors))
    ascii = []
    for i in range(len(pixels)):
        ascii_row=[]
        arr= (pixels[i])
        for j in range(len(arr)):
            
            val = int(arr[j][0] + arr[j][1] + arr[j][2])
            for k in range(len(clusters)):
                #bias k-mean algorithm
                distance = int(math.sqrt((val-clusters[k])**2))
                if (distance<bias_colors-10):
                    val = clusters[k]
                    break
            
            brightness_val = int(val/25)
            
            ascii_row.append(chars[brightness_val-1])
        ascii.append(ascii_row)
    ascii.reverse()
    with open('ascii.txt', 'w') as f:
            
            for i in range(len(ascii)):
                f.write('\n')
                arr = ascii[i]
                for j in range(len(arr)):
                    f.write(arr[j])
                 
          
    #

pixels = read_bmp('')#filename

pixels2 =arr_to_ascii(pixels)

