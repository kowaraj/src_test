type todoItemType = {
    id: int,
    text: string, 
    isComplete: bool
};

let emptyItem = {id: 0, text: "", isComplete: false};
let todoList : ref<array<todoItemType>> = ref(Belt.Array.make(-1, emptyItem))

let getTodoList = () => {
    todoList.contents
}

let addTodoItem = (item) => {
    let temp = todoList.contents
    let new_array  = Belt.Array.make(1, item)
    todoList := Belt.Array.concat(temp, new_array)
}