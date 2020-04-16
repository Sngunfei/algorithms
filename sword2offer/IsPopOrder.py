
"""
给定两个序列，第一个是压栈顺序，判断第二个序列是否是可能的弹出顺序。
1 2 3 4 5
3 4 2 1 5

1 3 2
"""

def isPopOrder(push, pop) -> bool:
    pop_pos = 0
    push_pos = 0
    stack = []

    while push_pos < len(push):
        stack.append(push[push_pos])
        push_pos += 1
        while stack and stack[-1] == pop[pop_pos]:
            stack.pop()
            pop_pos += 1
    return False if stack else True


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [4, 3, 5, 2, 1]
    print(isPopOrder(a, b))