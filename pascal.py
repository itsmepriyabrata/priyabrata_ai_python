class PascalTriangle:
    def _init_(self, rows):
        self.rows = rows
        self.triangle = self.generate_triangle()

    def generate_triangle(self):
        triangle = []
        for i in range(self.rows):
            row = [1]  # First element in each row is always 1
            if i > 0:
                prev_row = triangle[i - 1]
                for j in range(1, i):
                    row.append(prev_row[j - 1] + prev_row[j])
                row.append(1)  # Last element in each row is always 1
            triangle.append(row)
        return triangle

    def display_triangle(self):
        for row in self.triangle:
            print(" ".join(map(str, row)).center(self.rows * 3))


rows = int(input("Enter the number of rows for Pascal's Triangle: "))
pascal_triangle = PascalTriangle(rows)
pascal_triangle.display_triangle()
