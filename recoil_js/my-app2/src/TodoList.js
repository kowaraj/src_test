import { atom, useRecoilValue } from 'recoil';
import TodoItem from './TodoItem';
import TodoItemCreator from './TodoItemCreator';

const todoListState = atom(
    {
      key: 'todoListStateID', 
      default: []
    }
);

function MyTodoList() {

    const todoList = useRecoilValue(todoListState);

    return (
    <>
      {/* <TodoListStats /> */}
      {/* <TodoListFilters /> */}
      <TodoItemCreator />

      {todoList.map((todoItem) => (
        <TodoItem key={todoItem.id} item={todoItem} />
      ))}
    </>
    );
};

export { 
    MyTodoList as default, 
    todoListState as todoListState, 
    };
    