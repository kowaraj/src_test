'use strict';


var todoList = {
  contents: []
};

function getTodoList(param) {
  return todoList;
}

function addTodoItem(item) {
  var upd = todoList.contents;
  return upd.push(item);
}

exports.todoList = todoList;
exports.getTodoList = getTodoList;
exports.addTodoItem = addTodoItem;
/* No side effect */
