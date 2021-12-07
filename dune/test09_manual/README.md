[this page](https://ocamlverse.github.io/content/quickstart_ocaml_project_dune.html)

# Quickstart: Step4 - .mli interface file

```
[kapashnin@Andreys-MacBook-Pro: ~/src/test/dune/test09_manual ] dune exec bin/main.exe
File "mylib/mymath.ml", line 2, characters 4-7:
2 | let sub x y = x - y
        ^^^
Error (warning 32 [unused-value-declaration]): unused value sub.
```
# Quickstart: Step 3 - mylib

# Quickstart: Step 2 - keep it tidy

You might notice that currently, our created files reside at the root of the project directory. In most cases, this is not desirable since the project root is reserved for project metadata such as a readme, change log, license, and other project configurations. To keep things tidy, let’s move the program to a subdirectory. We will name the directory bin, a convention I use as a place to put entry point modules for executables

Run again:
```
[kapashnin@Andreys-MacBook-Pro: ~/src/test/dune/test09_manual ] dune build bin/main.exe
[kapashnin@Andreys-MacBook-Pro: ~/src/test/dune/test09_manual ] dune exec bin/main.exe
Hello, World!
```

Run from bin:
```
[kapashnin@Andreys-MacBook-Pro: ~/src/test/dune/test09_manual/bin ] dune exec ./main.exe
Entering directory '/Users/kapashnin/src/test/dune/test09_manual'
Entering directory '/Users/kapashnin/src/test/dune/test09_manual'
Hello, World!
[kapashnin@Andreys-MacBook-Pro: ~/src/test/dune/test09_manual/bin ] dune build main.exe
Entering directory '/Users/kapashnin/src/test/dune/test09_manual'
```

Still working as expected. Next up, we’re going to look at putting reusable code as library modules to be used from the executable.


# Quickstart: Step 1 - all files reside at the root!


Notice the `./main.exe` instead of `main.exe` for `exec`:
```
[kapashnin@Andreys-MacBook-Pro: ~/src/test/dune/test09_manual ] dune build main.exe
[kapashnin@Andreys-MacBook-Pro: ~/src/test/dune/test09_manual ] dune exec ./main.exe
Hello, World!
```

File tree:
```
[kapashnin@Andreys-MacBook-Pro: ~/src/test/dune/test09_manual ] find .
.
./dune
./main.ml
./README.md
./dune-project
./_build
./_build/default
./_build/default/.merlin-conf
./_build/default/.merlin-conf/exe-main
./_build/default/.main.eobjs
./_build/default/.main.eobjs/native
./_build/default/.main.eobjs/native/dune__exe__Main.o
./_build/default/.main.eobjs/native/dune__exe__Main.cmx
./_build/default/.main.eobjs/byte
./_build/default/.main.eobjs/byte/dune__exe__Main.cmt
./_build/default/.main.eobjs/byte/dune__exe__Main.cmo
./_build/default/.main.eobjs/byte/dune__exe__Main.cmi
./_build/default/.dune
./_build/default/.dune/configurator.v2
./_build/default/.dune/.dune-keep
./_build/default/.dune/configurator
./_build/default/main.ml
./_build/default/.merlin-exist-exe-main
./_build/default/main.exe
./_build/.digest-db
./_build/log
./_build/.db
./_build/.filesystem-clock
```