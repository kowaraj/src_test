let todoList : ref(array(int)) = ref(Belt.Array.make(-1,0))

let getTodoList = () => {
    todoList
}

let addTodoItem = (item) => {
    let temp : array(int) = todoList.contents
    let new_array  = Belt.Array.make(1, item)
    todoList := Belt.Array.concat(temp, new_array)
}

