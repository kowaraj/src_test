'use strict';

var React = require("react");
var R$MyRescriptApp = require("./R.bs.js");

function TodoItem(Props) {
  var item = Props.item;
  var editItemText = function (param) {
    
  };
  var toggleItemCompletion = function (param) {
    
  };
  var deleteItem = function (param) {
    
  };
  return React.createElement("div", undefined, React.createElement("input", {
                  type: "text",
                  value: item,
                  onChange: editItemText
                }), React.createElement("input", {
                  checked: true,
                  type: "checkbox",
                  onChange: toggleItemCompletion
                }), React.createElement("button", {
                  onClick: deleteItem
                }, R$MyRescriptApp.str("X")));
}

var make = TodoItem;

exports.make = make;
/* react Not a pure module */
