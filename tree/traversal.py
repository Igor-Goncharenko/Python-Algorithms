from typing import Generator
from tree_structure import BinNode as Node


def inorder_trav(tree: Node | None) -> Generator:
    """Algorithm Inorder(tree).
    1. Traverse the left subtree, i.e., call Inorder(left->subtree)
    2. Visit the root.
    3. Traverse the right subtree, i.e., call Inorder(right->subtree)
    """
    if tree is not None:
        yield from inorder_trav(tree.left)
        yield tree.value
        yield from inorder_trav(tree.right)


def preorder_trav(tree: Node | None) -> Generator:
    """Algorithm Preorder(tree).
    1. Visit the root.
    2. Traverse the left subtree, i.e., call Preorder(left->subtree)
    3. Traverse the right subtree, i.e., call Preorder(right->subtree).
    """
    if tree is not None:
        yield tree.value
        yield from inorder_trav(tree.left)
        yield from inorder_trav(tree.right)


def postorder_trav(tree: Node | None) -> Generator:
    """Algorithm Postorder(tree)
    1. Traverse the left subtree, i.e., call Postorder(left->subtree)
    2. Traverse the right subtree, i.e., call Postorder(right->subtree)
    3. Visit the root
    """
    if tree is not None:
        yield from postorder_trav(tree.left)
        yield from postorder_trav(tree.right)
        yield tree.value


def breadth_first_search(tree: Node | None) -> Generator:
    """Breadth first search.
    Breadth first search is a graph traversal algorithm that starts at the root
    node and explores all of the neighbor nodes at the present depth prior to
    moving on to the nodes at the next depth level.
    Uses Queue data structure.
    """
    queue = [tree.left, tree.right]
    yield tree.value
    while queue:
        el = queue.pop(0)
        if el is not None:
            yield el.value
            queue.append(el.left)
            queue.append(el.right)


def depth_first_search(tree: Node) -> Generator:
    """Depth first search.
    Depth first search is a graph traversal algorithm that starts at a root node
    and explores as far as possible along each branch before backtracking.
    Uses stack data structure.
    """
    stack = [tree.right, tree.left]
    yield tree.value
    while stack:
        el = stack.pop(-1)
        if el is not None:
            yield el.value
            stack.append(el.right)
            stack.append(el.left)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    print(f"Inorder trav: {list(inorder_trav(root))}")
    print(f"Preorder trav: {list(preorder_trav(root))}")
    print(f"Postorder trav: {list(postorder_trav(root))}")
    print(f"Breadth first search: {list(breadth_first_search(root))}")
    print(f"Depth first search: {list(depth_first_search(root))}")
