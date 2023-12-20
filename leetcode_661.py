import copy
from math import floor
from typing import List


def imageSmoother(img: List[List[int]]) -> List[List[int]]:
    m = len(img)
    n = len(img[0])
    new_img = copy.deepcopy(img)

    for row in range(m):
        for col in range(n):
            # curr position on img is img[row][col]
            # must find all positions that surround (row, col), and get
            # the avg of the numbers within them
            num_surrounding_positions = 1
            surrounding_sum = img[row][col]

            if col - 1 >= 0:
                surrounding_sum += img[row][col - 1]
                num_surrounding_positions += 1

            if col + 1 < n:
                surrounding_sum += img[row][col + 1]
                num_surrounding_positions += 1

            if row + 1 < m:
                surrounding_sum += img[row + 1][col]
                num_surrounding_positions += 1

                if col - 1 >= 0:
                    surrounding_sum += img[row + 1][col - 1]
                    num_surrounding_positions += 1

                if col + 1 < n:
                    surrounding_sum += img[row + 1][col + 1]
                    num_surrounding_positions += 1

            if row - 1 >= 0:
                surrounding_sum += img[row - 1][col]
                num_surrounding_positions += 1

                if col - 1 >= 0:
                    surrounding_sum += img[row - 1][col - 1]
                    num_surrounding_positions += 1

                if col + 1 < n:
                    surrounding_sum += img[row - 1][col + 1]
                    num_surrounding_positions += 1

            new_value = floor(surrounding_sum / num_surrounding_positions)
            new_img[row][col] = new_value

    return new_img


if __name__ == "__main__":
    img1 = [[100,200,100],[200,50,200],[100,200,100]]
    imageSmoother(img1)
