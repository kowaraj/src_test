let () = Mylib.Mymath.add 3 2 |> string_of_int |> print_endline 
let () = Mylib.Mymath.sub 3 2 |> string_of_int |> print_endline 

(* no parenthesis!!! *)
let () = print_endline @@ string_of_int @@ Mylib.Mymath.add 1 2 
