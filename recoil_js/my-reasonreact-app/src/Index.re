switch (ReactDOM.querySelector("#app1")) {
| Some(root) => ReactDOM.render(<ReasonReactApp />, root)
| None => ()
}

switch (ReactDOM.querySelector("#app2")) {
| Some(root) => ReactDOM.render(<ReScriptApp_re />, root)
| None => ()
}

switch (ReactDOM.querySelector("#app3")) {
| Some(root) => ReactDOM.render(<ReScriptApp_res />, root)
| None => ()
}

