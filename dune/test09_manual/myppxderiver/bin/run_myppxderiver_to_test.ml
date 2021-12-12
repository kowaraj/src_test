module My_module_name = struct
  type t = char
  [@@deriving my_deriver_name {with_path=false}, eq]
end

let to_be_derived: My_module_name.t = "Y"

print_endline to_be_derived