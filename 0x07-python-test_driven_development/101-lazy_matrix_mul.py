#!/usr/bin/python3
"""Matrix multiplication using NumPy
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b using NumPy.

    Args:
        m_a (list): A list of lists representing the first matrix.
        m_b (list): A list of lists representing the second matrix.

    Returns:
        list: A new matrix resulting from the multiplication of m_a and m_b.

    Raises:
        ValueError: If m_a or m_b is empty or if they can't be multiplied.

    """
    try:
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        result = np.matmul(np_a, np_b).tolist()
        return result
    except ValueError as ve:
        raise ValueError("m_a and m_b can't be multiplied") from ve

if __name__ == "__main__":
    # Example usage
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
