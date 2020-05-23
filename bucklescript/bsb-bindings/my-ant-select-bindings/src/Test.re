[@react.component]
let make = () =>  
  <div> 
    {ReasonReact.string("test div tag")} 
    <Ant.Select 
      style=ReactDOMRe.Style.make(~width="100%", ())
      mode="multiple">
      {
        [ "testo1", "testo2", "testo3" ] 
          |> List.map( top => <Ant.Select.Option key=top> {ReasonReact.string(top)} </Ant.Select.Option> ) 
          |> Array.of_list 
      }
    </Ant.Select>
  </div> ;
