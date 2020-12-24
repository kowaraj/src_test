'use strict';

var Curry = require("bs-platform/lib/js/curry.js");
var React = require("react");
var Belt_Array = require("bs-platform/lib/js/belt_Array.js");
var R$MyRescriptApp = require("./R.bs.js");
var MyRecoil$MyRescriptApp = require("./MyRecoil.bs.js");
var TodoItem$MyRescriptApp = require("./TodoItem.bs.js");

function TodoList(Props) {
  var match = React.useState(function () {
        return "";
      });
  var setInputValue = match[1];
  var items = Belt_Array.map(MyRecoil$MyRescriptApp.getTodoList(undefined), (function (item) {
          return React.createElement(TodoItem$MyRescriptApp.make, {
                      item: "asdf"
                    });
        }));
  console.log(items);
  return React.createElement("div", undefined, React.createElement("button", {
                  onClick: (function (e) {
                      return Curry._1(setInputValue, (function (param) {
                                    return "6";
                                  }));
                    })
                }, R$MyRescriptApp.str("MOD")), items);
}

var make = TodoList;

exports.make = make;
/* react Not a pure module */
