class ColorTV:
    def _init_(self):
        self.pixels = [[[0, 0, 0] for _ in range(5)] for _ in range(4)]  

    def switch_on(self, pixel_row, pixel_column, rgb_values):
        if 0 <= pixel_row < 4 and 0 <= pixel_column < 5:
            self.pixels[pixel_row][pixel_column] = rgb_values
        else:
            print("Invalid pixel coordinates.")

    def switch_off(self, pixel_row, pixel_column):
        if 0 <= pixel_row < 4 and 0 <= pixel_column < 5:
            self.pixels[pixel_row][pixel_column] = [0, 0, 0]
        else:
            print("Invalid pixel coordinates.")

    def display_pixels(self):
        for row in self.pixels:
            for pixel in row:
                print(pixel, end=" ")
            print()


# Example usage:
tv = ColorTV()

# Turn on some pixels
tv.switch_on(0, 1, [255, 0, 0])  # Red pixel at (0, 1)
tv.switch_on(2, 3, [0, 255, 0])  # Green pixel at (2, 3)

# Display the current state of pixels
tv.display_pixels()

# Turn off a pixel
tv.switch_off(0, 1)

# Display the updated state of pixels
tv.display_pixels()
