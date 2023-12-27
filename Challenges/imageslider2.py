"""
图像平滑器 是大小为 3 x 3 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。
每个单元格的  平均灰度 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9 个单元格的平均值）。
对于位于边缘的像素，则计算平均灰度时不考虑缺失的单元格，只计算有效单元格平均即可。

This is the elegant solution. It uses two for loops to cycle through the 8 squares surrounding a square.
"""

def smooth_image(img):
    rows, cols = len(img), len(img[0])
    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            total = []

            for x in range(max(0, i-1), min(rows, i+2)):
                for y in range(max(0, j-1), min(cols, j+2)):
                    total.append(img[x][y])

            result[i][j] = sum(total) // len(total)
    return result

# Example usage
img = [[1, 1, 1],
       [1, 0, 1],
       [1, 1, 1]]

output = smooth_image(img)
print(output)
