@react.component
let make = () => {

    let (inputValue, setInputValue) = React.useState(_ => "");
    let (localTodoList, setLocalTodoList) = React.useState(_ => MyRecoil.emptyTodoList.contents)

    let pass_setter = () => () => setLocalTodoList
    let items = Belt.Array.map( 
        MyRecoil.subscribeForTodoList(pass_setter()),
        item => <TodoItem item="asdf"/>)

    Js.log(items)
    <div> 
        <button onClick={e=> setInputValue(_=>"6")}>{R.str("MOD")}</button>

    (
        items
        |> React.array
    )
    


    </div>
}