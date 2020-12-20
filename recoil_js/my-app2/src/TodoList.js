import { atom, useRecoilValue } from 'recoil';
import TodoItem from './TodoItem';
import TodoItemCreator from './TodoItemCreator';
import TodoListFilters from './TodoListFilter';
// import { filteredTodoListState } from './TodoListFilter';
import { filteredTodoListState } from './TodoListFilter';

const todoListState = atom(
    {
      key: 'todoListStateID', 
      default: []
    }
);

function MyTodoList() {

    // const todoList = useRecoilValue(todoListState);
    const todoList = useRecoilValue(filteredTodoListState);

    return (
    <>
        {/* <TodoListStats /> */}
        <TodoListFilters />
        <TodoItemCreator />

        {todoList.map((todoItem) => 
            (
            <TodoItem key={todoItem.id} item={todoItem} />
            )
        )}
    </>
    );
};

export { 
    MyTodoList as default, 
    todoListState, 
    };
    