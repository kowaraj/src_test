let () = Mylib.Mymath.add 3 2 |> string_of_int |> print_endline 
let () = Mylib.Mymath.sub 3 2 |> string_of_int |> print_endline 

(* no parenthesis!!! *)
let () = print_endline @@ string_of_int @@ Mylib.Mymath.add 1 2 

(* trying ppx *)
(* also: dune exec ./myppx/bin/run_myppx_to_test.exe *)
let () = Myppx.Myderiving.test