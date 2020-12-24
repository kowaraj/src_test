@react.component
let make = () => {

    let (inputValue, setInputValue) = React.useState(_ => "");

    let items = Belt.Array.map( 
        MyRecoil.getTodoList(),
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