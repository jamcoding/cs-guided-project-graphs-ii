"""
An `image` is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).

Given a coordinate `(sr, sc)` representing the starting pixel (row and column)
of the flood fill, and a pixel value `newColor`, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

```plaintext
Input:
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]

sr = 1, sc = 1, newColor = 2

Output: [
    [2,2,2],
    [2,2,0],
    [2,0,1]
]

Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels
connected by a path of the same color as the starting pixel are colored with
the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.
```

Notes:

- The length of `image` and `image[0]` will be in the range `[1, 50]`.
- The given starting pixel will satisfy `0 <= sr < image.length` and
`0 <= sc < image[0].length`.
- The value of each color in `image[i][j]` and `newColor` will be an integer in
`[0, 65535]`.
"""
def flood_fill(image, sr, sc, new_color):
    """
    Inputs:
    image -> List[List[int]]
    sr -> int
    sc -> int
    new_color -> int

    Output:
    List[List[int]]
    """
    current_color = image[sr][sc]
    # Traverse
    queue = []
    visited = set()
    queue.append((sr, sc))

    while len(queue) > 0:
        # pop the item off the queue
        current_vertex = queue.pop(0)
        # check if vertex is visited
        if current_vertex in visited:
            continue

        visited.add(current_vertex)
        # Update the pixel to the new color
        image[current_vertex[0]][current_vertex[1]] = new_color

        # Queue up the neighbors
        row = current_vertex[0]
        col = current_vertex[1]
        neighbors = []
        if row - 1 >= 0 and image[row-1][col] == current_color:
            # look up
            neighbors.append((row - 1, col))
        if row + 1 < len(image) and image[row+1][col] == current_color:
            # look down
            neighbors.append((row + 1, col))
        if col - 1 >= 0 and image[row][col-1] == current_color:
            # look left
            neighbors.append((row, col - 1))
        if col + 1 < len(image[row]) and image[row][col+1] == current_color:
            # look right
            neighbors.append((row, col + 1))

        for neighbor in neighbors:
            queue.append(neighbor)

image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]

flood_fill(image, 1, 1, 2)

# print(image)

for i in image:
    print(i)