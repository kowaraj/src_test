type todoItemType = {
    id: int,
    text: string, 
    isComplete: bool
};

let emptyItem = {id: 0, text: "", isComplete: false};
let emptyTodoList : ref<array<todoItemType>> = ref(Belt.Array.make(-1, emptyItem))

let setter = ref( (x : array<todoItemType> ) => { emptyTodoList.contents  } )

let todoList : ref<array<todoItemType>> = ref(Belt.Array.make(-1, emptyItem))

let subscribeForTodoList = setLocalTodoList => {
    setter := setLocalTodoList()
    todoList
}

let getTodoList = () => {
    todoList.contents
}

let addTodoItem = (item) => {
    let temp = todoList.contents
    let new_array  = Belt.Array.make(1, item)
    todoList := Belt.Array.concat(temp, new_array)
}