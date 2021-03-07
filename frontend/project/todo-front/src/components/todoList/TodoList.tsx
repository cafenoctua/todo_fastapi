import React from 'react';
import { Todo } from '../../types';
import { TodoItem } from '../todoItem/TodoItem';

interface TodoListProps {
    todos: Todo[];
}

export const TodoList: React.FC<TodoListProps> = ({ todos }) => {
    return (
        <div>
            {todos.map(todo => (
                <TodoItem key={todo.title} todo={todo} />
            ))}
        </div>
    )
}