'use strict';

var React = require("react");
var TodoItem$MyRescriptApp = require("./TodoItem.bs.js");

function TodoList2(Props) {
  return React.createElement("div", undefined, React.createElement(TodoItem$MyRescriptApp.make, {
                  item: "asdf"
                }));
}

var make = TodoList2;

exports.make = make;
/* react Not a pure module */
