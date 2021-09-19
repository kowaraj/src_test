@react.component
let make = () => {

    let (inputValue, setInputValue) = React.useState(_ => "");

    let onChange = (e) => {
        setInputValue(ReactEvent.Form.target(e)["value"])
    };

    let addItem = (e_) => {
        let item_id = Js.Math.random_int(0,1000000000)
        let new_item : MyRecoil.todoItemType = {id: item_id, text: inputValue, isComplete: false}
        MyRecoil.addTodoItem(new_item)
    };

    <div>
        <input type_="text" value={inputValue} onChange={onChange} />
        <button onClick={addItem}>{R.str("Add")}</button>
    </div>
}