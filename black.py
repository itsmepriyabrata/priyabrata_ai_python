class BlackAndWhiteTV:
    def _init_(self):
        # Initialize a 2D array with 20 pixels, all initially turned off (0)
        self.pixels = [[0] * 4 for _ in range(5)]  # Assuming a 4x5 grid for simplicity

    def switch_on_pixel(self, row, col):
        # Switch on the pixel at the specified row and column
        if 0 <= row < len(self.pixels) and 0 <= col < len(self.pixels[0]):
            self.pixels[row][col] = 1
        else:
            print("Invalid pixel coordinates.")

    def switch_off_pixel(self, row, col):
        # Switch off the pixel at the specified row and column
        if 0 <= row < len(self.pixels) and 0 <= col < len(self.pixels[0]):
            self.pixels[row][col] = 0
        else:
            print("Invalid pixel coordinates.")

    def display_tv_pixels(self):
        # Display the current state of the TV pixels
        for row in self.pixels:
            print(row)

# Example usage:
tv = BlackAndWhiteTV()

# Switch on some pixels
tv.switch_on_pixel(1, 2)
tv.switch_on_pixel(3, 0)
tv.switch_on_pixel(4, 3)

# Switch
