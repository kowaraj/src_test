let ( let* ) o f =
  match o with
  | None -> None
  | Some x -> f x

let return x = Some x

let find_and_sum tbl k1 k2 =
  let* x1 = Hashtbl.find_opt tbl k1 in
  let* x2 = Hashtbl.find_opt tbl k2 in
    return (x1 + x2)


