'use strict';

var React = require("react");

function ReasonReactApp(Props) {
  return React.createElement("h1", undefined, "The App in ReasonReact");
}

var make = ReasonReactApp;

exports.make = make;
/* react Not a pure module */
