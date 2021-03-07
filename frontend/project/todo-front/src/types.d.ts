import { type } from "os";

interface Todo {
    title: string;
    description: string;
    status: string;
    userName: string;
}

type TodoAdd = (todo: Todo) => void;
