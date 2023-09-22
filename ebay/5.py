def solution(message):
    global answer
    answer = ''
    postorder_traversal(message, 0)

    return answer

def postorder_traversal(tree, index):
    global answer
    size = len(tree)
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    if left_child < size:
        postorder_traversal(tree, left_child)
    if right_child < size:
        postorder_traversal(tree, right_child)
    answer += tree[index]


