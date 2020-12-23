'use strict';

var React = require("react");
var ReactDom = require("react-dom");
var App$MyRescriptApp = require("./App.bs.js");

var root = document.querySelector("#root");

if (!(root == null)) {
  ReactDom.render(React.createElement(App$MyRescriptApp.make, {}), root);
}

/* root Not a pure module */
