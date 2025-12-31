def count_bright_spots(pixels):
    count = 0
    for i in range(len(pixels)):
        if i == 0 or i == len(pixels) - 1 or len(pixels) == 2 or len(pixels) == 1:
            continue
            
        if pixels[i] > (pixels[i - 1]) and pixels[i]  > (pixels[i + 1]):
            count += 1
    return count

