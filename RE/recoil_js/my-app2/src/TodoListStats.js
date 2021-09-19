import { useRecoilValue } from 'recoil';
import { todoListState } from './TodoList';

const calcTotal = (acc, cur) => {
    acc = acc + 1
    return acc
}

const calcCompleted = (acc, cur) => {
    if (cur.isComplete) {
        return acc + 1
    }
    return acc
}

const get_stats = (todoList) => {
    const t = todoList.reduce(calcTotal, 0);
    const c = todoList.reduce(calcCompleted, 0);
    return {
        total: t,
        completed: c,
        incomplete: t - c,
        percent: c/t
    }
}

function TodoListStats() {
    const todoList = useRecoilValue(todoListState);
    const s = get_stats(todoList);

    return (
        <ul>
            <li> Total: {s.total} </li>
            <li> Completed: {s.completed} </li>
            <li> Incomplete: {s.incomplete} </li>
            <li> Percent Completed: {s.percent} </li>
        </ul>
    )
}

export { TodoListStats as default };
