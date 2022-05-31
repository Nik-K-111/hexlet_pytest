# Тест стека: заполнение и извлечение.

def test_stack():
    stack = []

    stack.append('One')
    stack.append('Two')

    assert stack.pop() == 'Two'
    assert stack.pop() == 'One'

# Тест стека: начальное состояние, состояние после добавления, состояние после очистки.

def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)

    stack.pop()
    assert not stack

# Тест стека: извлечение из пустого стека.

import pytest


def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()