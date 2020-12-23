'use strict';

var React = require("react");
var R$MyRescriptApp = require("./R.bs.js");

function TodoItemCreator2(Props) {
  var onChange = function (e) {
    console.log("onChange");
    
  };
  var addItem = function (e) {
    console.log("addItem");
    
  };
  return React.createElement("div", undefined, React.createElement("input", {
                  type: "text",
                  value: "init value",
                  onChange: onChange
                }), React.createElement("button", {
                  onClick: addItem
                }, R$MyRescriptApp.str("Add")));
}

var make = TodoItemCreator2;

exports.make = make;
/* react Not a pure module */
