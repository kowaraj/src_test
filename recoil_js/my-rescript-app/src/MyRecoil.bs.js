'use strict';

var Belt_Array = require("bs-platform/lib/js/belt_Array.js");

var emptyItem = {
  id: 0,
  text: "",
  isComplete: false
};

var todoList = {
  contents: Belt_Array.make(-1, emptyItem)
};

function getTodoList(param) {
  return todoList.contents;
}

function addTodoItem(item) {
  var temp = todoList.contents;
  var new_array = Belt_Array.make(1, item);
  todoList.contents = Belt_Array.concat(temp, new_array);
  
}

exports.emptyItem = emptyItem;
exports.todoList = todoList;
exports.getTodoList = getTodoList;
exports.addTodoItem = addTodoItem;
/* todoList Not a pure module */
