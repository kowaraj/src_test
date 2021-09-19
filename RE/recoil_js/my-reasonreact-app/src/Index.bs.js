'use strict';

var React = require("react");
var ReactDom = require("react-dom");
var ReScriptApp_re$MyReasonreactApp = require("./ReScriptApp_re.bs.js");
var ReasonReactApp$MyReasonreactApp = require("./ReasonReactApp.bs.js");
var ReScriptApp_res$MyReasonreactApp = require("./ReScriptApp_res.bs.js");

var root = document.querySelector("#app1");

if (!(root == null)) {
  ReactDom.render(React.createElement(ReasonReactApp$MyReasonreactApp.make, {}), root);
}

var root$1 = document.querySelector("#app2");

if (!(root$1 == null)) {
  ReactDom.render(React.createElement(ReScriptApp_re$MyReasonreactApp.make, {}), root$1);
}

var root$2 = document.querySelector("#app3");

if (!(root$2 == null)) {
  ReactDom.render(React.createElement(ReScriptApp_res$MyReasonreactApp.make, {}), root$2);
}

/* root Not a pure module */
