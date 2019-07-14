# coding: utf-8

# 如何仅用递归函数和栈操作逆序一个栈
def get(stack):
    '''将栈stack的栈底元素返回并移除'''
    result = stack.pop()
    if not stack:
        return result
    else:
        last = get(stack)
        stack.append(result)
        return last


def reverse(stack):
    '''逆序一个栈'''
    if not stack:
        return
    else:
        i = get(stack)
        reverse(stack)
        stack.append(i)
        return stack


if __name__ == '__main__':
    stack = [1, 2, 3, 4, 5]
    print(stack)
    print(reverse(stack))

