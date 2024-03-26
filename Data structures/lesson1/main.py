from stack import Stack

"""
Task 1. Дана скобочная последовательность. Нужно определить, правильная она или нет. 

Каждой открывающей скобке в последовательности соответствует закрывающая, образуя пары.

Будем считать строку «правильной» если все скобки закрываются в нужном порядке, т.е:

1. для каждой открывающей есть закрывающая из той же пары;
2. скобки закрываются в правильном порядке.
3. Пустая строка считается правильной.

Программе на вход подаётся последовательность из скобок трёх видов: [], (), {}.

Напишите функцию is_correct_brackets, которая принимает на вход скобочную последовательность и возвращает True, 
если последовательность правильная, а иначе возвращает False.
"""


def is_correct_brackets(sequence: str) -> bool:

    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    stack = Stack()
    for symbol in sequence:
        if symbol in brackets.keys():
            stack.push(symbol)
        elif not stack.is_empty() and symbol == brackets[stack.peek()]:
            stack.pop()
        else:
            return False

    if stack.is_empty():
        return True
    else:
        return False


print(is_correct_brackets('((()))'))  # True
print(is_correct_brackets('((()()'))  # False
print(is_correct_brackets('(()'))  # False
print(is_correct_brackets(''))  # True

