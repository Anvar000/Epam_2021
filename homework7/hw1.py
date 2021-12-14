"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    """Take an element and find the number of occureences in tree

    Args:
        tree (dict): can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
        element (Any): searching element

    Returns:
        int: the number of occurences of the element in the given tree
    """
    if tree == element:
        return 1
    if isinstance(tree, list):
        return sum(find_occurrences(subtree, element) for subtree in tree)
    if isinstance(tree, dict):
        return sum(find_occurrences(subtree, element)
                   for subtree in tree.values())
    return 0


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
