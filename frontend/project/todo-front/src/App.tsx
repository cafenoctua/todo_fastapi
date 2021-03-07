import React, { useState } from 'react';
import { TodoAddForm } from './components/todoAddForm/TodoAddForm';
import { TodoList } from './components/todoList/TodoList';
import { Todo, TodoAdd } from './types';

const initialTodos: Todo[] = [
  {
    title: "test",
    description: "test",
    status: "not yet",
    userName: "test"
  },
  {
    title: "test1",
    description: "test",
    status: "not yet",
    userName: "test"
  },
  {
    title: "test2",
    description: "test",
    status: "not yet",
    userName: "test"
  }
]

function App() {
  const [todos, setTodos] = useState(initialTodos)

  const todoAdd: TodoAdd = (todo: Todo) => {
    const newTodo = {...todo};
    setTodos([...todos, newTodo])
  }
  return (
    <>
      <TodoAddForm todoAdd={todoAdd} />
      <TodoList todos={todos} />
    </>
  );
}

export default App;
