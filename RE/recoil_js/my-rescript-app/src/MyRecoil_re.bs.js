'use strict';

var Belt_Array = require("bs-platform/lib/js/belt_Array.js");

var todoList = {
  contents: Belt_Array.make(-1, 0)
};

function getTodoList(param) {
  return todoList;
}

function addTodoItem(item) {
  var temp = todoList.contents;
  var new_array = Belt_Array.make(1, item);
  todoList.contents = Belt_Array.concat(temp, new_array);
  
}

exports.todoList = todoList;
exports.getTodoList = getTodoList;
exports.addTodoItem = addTodoItem;
/* todoList Not a pure module */
