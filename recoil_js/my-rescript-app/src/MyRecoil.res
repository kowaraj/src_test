type todoItemType = {
    id: int,
    text: string, 
    isComplete: bool
};

let todoList : ref<array<todoItemType>> = ref([]);

let getTodoList = () => {
    todoList
}

let addTodoItem = (item) => {
    let upd : array<todoItemType> = todoList.contents
    Js.Array2.push(upd, item)
}

