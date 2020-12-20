import { useRecoilState } from 'recoil';
import { todoListState } from './TodoList';

function TodoItem({item}) {
    const [todoList, setTodoList] = useRecoilState(todoListState);

    return(
        <div>
            <p> TODOITEM </p>
            <input type="text" value={item.value}>
            </input>
        </div>
    )
};

export default TodoItem;