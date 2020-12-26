'use strict';

var Curry = require("bs-platform/lib/js/curry.js");
var Belt_Array = require("bs-platform/lib/js/belt_Array.js");

var emptyItem = {
  id: 0,
  text: "",
  isComplete: false
};

var emptyTodoList = {
  contents: Belt_Array.make(-1, emptyItem)
};

var setter = {
  contents: (function (x) {
      return emptyTodoList.contents;
    })
};

var todoList = {
  contents: Belt_Array.make(-1, emptyItem)
};

function subscribeForTodoList(setLocalTodoList) {
  setter.contents = Curry._1(setLocalTodoList, undefined);
  return todoList;
}

function getTodoList(param) {
  return todoList.contents;
}

function addTodoItem(item) {
  var temp = todoList.contents;
  var new_array = Belt_Array.make(1, item);
  todoList.contents = Belt_Array.concat(temp, new_array);
  
}

exports.emptyItem = emptyItem;
exports.emptyTodoList = emptyTodoList;
exports.setter = setter;
exports.todoList = todoList;
exports.subscribeForTodoList = subscribeForTodoList;
exports.getTodoList = getTodoList;
exports.addTodoItem = addTodoItem;
/* emptyTodoList Not a pure module */
