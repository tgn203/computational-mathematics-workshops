"""
main.py
Thomas Noakes
2025
"""


def matrix_addition(mat_a: list, mat_b: list):
    """Add two matrices of the same dimensions"""

    # Ensure matrices are of the same dimensions
    dim_a = (len(mat_a), len(mat_a[0]))
    dim_b = (len(mat_b), len(mat_b[0]))
    if dim_a != dim_b:
        raise ValueError("Matrices must be of the same dimensions")

    # Create and fill the output matrix
    mat_ans: list = []
    for i, row in enumerate(mat_a):
        mat_ans.append([])
        for j in range(len(row)):
            mat_ans[i].append(mat_a[i][j] + mat_b[i][j])

    return mat_ans


def matrix_subtraction(mat_a: list, mat_b: list):
    """Subtract two matrices of the same dimensions"""

    # Ensure matrices are of the same dimensions
    dim_a = (len(mat_a), len(mat_a[0]))
    dim_b = (len(mat_b), len(mat_b[0]))
    if dim_a != dim_b:
        raise ValueError("Matrices must be of the same dimensions")

    # Create and fill the output matrix
    mat_ans: list = []
    for i, row in enumerate(mat_a):
        mat_ans.append([])
        for j in range(len(row)):
            mat_ans[i].append(mat_a[i][j] - mat_b[i][j])

    return mat_ans


def main():
    """
    Matrix Manipulation
    """

    a = [[6, -2], [-3, 5]]
    b = [[7, 1], [0, -3]]

    print(f"A = {a}")
    print(f"B = {b}")
    print("-" * 50)

    print(f"A + B = {matrix_addition(a, b)}")
    print(f"A - B = {matrix_subtraction(a, b)}\n")


if __name__ == "__main__":
    main()
