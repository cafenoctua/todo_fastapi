import React from 'react';
import { Todo } from '../../types';
import './TodoItem.css';

interface TodoProps {
    todo: Todo
}

export const TodoItem: React.FC<TodoProps> = ({ todo }) => {
    return (
        <div className="card">
            <h1>{todo.title}</h1>
            <ul>
                <li>
                    <label >
                        Description: {todo.description}
                    </label>
                </li>
                <li>
                    <label>
                        Status: {todo.status}
                    </label>
                </li>
                <li>
                    <label>
                        User name: {todo.userName}
                    </label>
                </li>
            </ul>
        </div>
    )
}