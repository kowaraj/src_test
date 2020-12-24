'use strict';

var Curry = require("bs-platform/lib/js/curry.js");
var React = require("react");
var Js_math = require("bs-platform/lib/js/js_math.js");
var R$MyRescriptApp = require("./R.bs.js");
var MyRecoil$MyRescriptApp = require("./MyRecoil.bs.js");

function TodoItemCreator(Props) {
  var match = React.useState(function () {
        return "";
      });
  var setInputValue = match[1];
  var inputValue = match[0];
  var onChange = function (e) {
    return Curry._1(setInputValue, e.target.value);
  };
  var addItem = function (e_) {
    var item_id = Js_math.random_int(0, 1000000000);
    return MyRecoil$MyRescriptApp.addTodoItem({
                id: item_id,
                text: inputValue,
                isComplete: false
              });
  };
  return React.createElement("div", undefined, React.createElement("input", {
                  type: "text",
                  value: inputValue,
                  onChange: onChange
                }), React.createElement("button", {
                  onClick: addItem
                }, R$MyRescriptApp.str("Add")));
}

var make = TodoItemCreator;

exports.make = make;
/* react Not a pure module */
