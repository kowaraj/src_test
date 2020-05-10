'use strict';

var Antd = require("antd");
var React = require("react");

function Test(Props) {
  return React.createElement("div", undefined, "test div tag", React.createElement(Antd.Select, { }));
}

var make = Test;

exports.make = make;
/* antd Not a pure module */
