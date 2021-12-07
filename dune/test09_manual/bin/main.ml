(* let () = print_endline string_of_int Mylib.Mymath.add 1 2 *)

let () = 
  let result = Mylib.Mymath.add 1 2 in
  print_endline (string_of_int result)

let () = print_endline (string_of_int (Mylib.Mymath.add 1 2))

let () = Mylib.Mymath.add 1 2 |> Printf.printf "%i\n" 
