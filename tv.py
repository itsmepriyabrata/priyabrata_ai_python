# Define the TV dimensions
rows = 4
columns = 5

# Create a 2D array to represent the TV pixels
tv_pixels = [[0] * columns for _ in range(rows)]

# Function to display the TV pixels
def display_tv():
    for row in tv_pixels:
        print(row)

# Turn on some pixels (set them to 1)
tv_pixels[1][2] = 1
tv_pixels[3][4] = 1
tv_pixels[0][1] = 1

# Display the TV pixels before turning off any
print("TV pixels before turning off:")
display_tv()

# Turn off a pixel (set it to 0)
tv_pixels[1][2] = 0

# Display the TV pixels after turning off one
print("\nTV pixels after turning off one pixel:")
display_tv()
