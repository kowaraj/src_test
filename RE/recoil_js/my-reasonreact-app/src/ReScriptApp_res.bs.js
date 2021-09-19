'use strict';

var React = require("react");

function ReScriptApp_res(Props) {
  return React.createElement("h1", undefined, "The App in ReScript.res");
}

var make = ReScriptApp_res;

exports.make = make;
/* react Not a pure module */
