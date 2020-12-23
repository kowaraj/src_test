'use strict';

var React = require("react");
var TodoList$MyRescriptApp = require("./TodoList.bs.js");
var TodoItemCreator2$MyRescriptApp = require("./TodoItemCreator2.bs.js");

function App(Props) {
  return React.createElement("div", undefined, React.createElement(TodoItemCreator2$MyRescriptApp.make, {}), React.createElement(TodoList$MyRescriptApp.make, {}));
}

var make = App;

exports.make = make;
/* react Not a pure module */
