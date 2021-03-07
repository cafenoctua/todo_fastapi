import React, { useState } from 'react';
import { TodoAdd } from '../../types';

interface TodoAddProps {
    todoAdd: TodoAdd;
}

export const TodoAddForm: React.FC<TodoAddProps> = ({ todoAdd }) => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [status, setStatus] = useState('');
    const [userName, setUserName] = useState('');
    
    const resetSets = () => {
        setTitle('');
        setDescription('');
        setStatus('');
        setUserName('');
    }
    return (
        <form>
            <label>Title:</label>
            <ul>
                <input
                    type="text"
                    value={title}
                    onChange={e => {
                        setTitle(e.target.value);
                    }}
                />
            </ul>
            <label>description:</label>
            <ul>
                <input
                    type="text"
                    value={description}
                    onChange={e => {
                        setDescription(e.target.value);
                    }}
                />
            </ul>
            <label>Status:</label>
            <ul>
                <input
                    type="text"
                    value={status}
                    onChange={e => {
                        setStatus(e.target.value);
                    }}
                />
            </ul>
            <label>User name:</label>
            <ul>
                <input
                    type="text"
                    value={userName}
                    onChange={e => {
                        setUserName(e.target.value);
                    }}
                />
            </ul><br/>
            <button
                type="submit"
                onClick={e => {
                    e.preventDefault();
                    todoAdd({...{title:title, description:description, status:status, userName:userName}});
                    resetSets();
                }}
            >Add Todo</button>
        </form>
    )
}