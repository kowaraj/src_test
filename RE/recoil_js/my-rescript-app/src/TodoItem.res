
@react.component
let make = (~item) => {

    let editItemText = (_) => {
        ();
    }

    let toggleItemCompletion = (_) => { (); }
    let deleteItem = (_) => { (); }

    <div>
        <input type_="text" value={item} onChange={editItemText} />
        <input type_="checkbox" checked={true}  onChange={toggleItemCompletion} />
        <button onClick={deleteItem}>{R.str("X")}</button>
    </div>

}