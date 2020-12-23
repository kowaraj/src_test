@react.component
let make = () => {

    let onChange = (e) => {
        Js.log("onChange")
    };

    let addItem = (e) => {
        Js.log("addItem")
    };

    <div>
        <input type_="text" value={"init value"} onChange={onChange} />
        <button onClick={addItem}>{R.str("Add")}</button>
    </div>
}