open Ppxlib

let some_context = Extension.Context.expression

let some_pattern = Ast_pattern.(single_expr_payload (estring __))
(* let some_pattern = Ast_pattern.(single_expr_payload (pexp_tuple ((eint __)^::(estring __)^::nil))) *)

let expand_function ~loc ~path s = 
  let () = print_endline path in (* don't know how to use path yet *)
  Ast_builder.Default.estring ~loc (s^"_extendedstring")



(* to be used as [%my_extension_name ...] *)
let my_magic_extension_var =
  Extension.declare
    "my_extension_name"
    some_context
    some_pattern
    expand_function

let rule = Context_free.Rule.extension my_magic_extension_var

let () =
  Driver.register_transformation ~rules:[rule] "my_transformation"