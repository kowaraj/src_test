/* Note that `myDep.re` becomes the module `MyDep`. In OCaml and Reason syntax, a module is upper-cased. */
print_endline(MyDep.secret);   /* <-- prints "hello" */
print_endline("hello");        /* <-- prints "hello" */
/*print_endline MyDep.secret;  <----- prints !! nothing !! */
/*print_endline "hello";       <----- compile ERROR        */

