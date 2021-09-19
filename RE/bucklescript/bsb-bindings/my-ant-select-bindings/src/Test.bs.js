'use strict';

var Antd = require("Antd");
var List = require("bs-platform/lib/js/list.js");
var $$Array = require("bs-platform/lib/js/array.js");
var React = require("react");

function Test(Props) {
  return React.createElement("div", undefined, "test div tag", React.createElement(Antd.Select, {
                  style: {
                    width: "100%"
                  },
                  mode: "multiple",
                  children: $$Array.of_list(List.map((function (top) {
                              return React.createElement(Antd.Select.Option, {
                                          children: top,
                                          key: top
                                        });
                            }), /* :: */[
                            "testo1",
                            /* :: */[
                              "testo2",
                              /* :: */[
                                "testo3",
                                /* [] */0
                              ]
                            ]
                          ]))
                }));
}

var make = Test;

exports.make = make;
/* Antd Not a pure module */
