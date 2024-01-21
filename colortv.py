# Define the dimensions of the TV and initialize a 3D array for pixels
tv_width = 4  # Assuming a 4x5 grid for simplicity
tv_height = 5
tv_pixels = [[[0, 0, 0] for _ in range(tv_width)] for _ in range(tv_height)]

# Function to turn on a pixel with RGB values
def switch_on(pixel_x, pixel_y, red, green, blue):
    tv_pixels[pixel_y][pixel_x] = [red, green, blue]

# Function to turn off a pixel
def switch_off(pixel_x, pixel_y):
    tv_pixels[pixel_y][pixel_x] = [0, 0, 0]

# Example: Turn on pixel at position (2, 3) with RGB values (255, 0, 0)
switch_on(2, 3, 255, 0, 0)

# Example: Turn off pixel at position (1, 1)
switch_off(1, 1)

# Print the 3D array representing the TV pixels
for row in tv_pixels:
    print(row)
