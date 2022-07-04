

```
kowaraj@ams-ap-mbp2 ~/src/kj/src_test  % dune init proj ocaml_freq_counter
Success: initialized project component named ocaml_freq_counter

kowaraj@ams-ap-mbp2 ~/src/kj/src_test  % cd ocaml_freq_counter

kowaraj@ams-ap-mbp2 src/kj/src_test/ocaml_freq_counter  % dune build
Info: Creating file dune-project with this contents:
| (lang dune 2.9)
| (name ocaml_freq_counter)

kowaraj@ams-ap-mbp2 src/kj/src_test/ocaml_freq_counter  % ls -la
total 8
drwxr-xr-x   8 kowaraj  staff  256 Jul  4 14:38 .
drwxr-xr-x  14 kowaraj  staff  448 Jul  4 14:38 ..
drwxr-xr-x   9 kowaraj  staff  288 Jul  4 14:38 _build
drwxr-xr-x   4 kowaraj  staff  128 Jul  4 14:38 bin
-rw-r--r--   1 kowaraj  staff   42 Jul  4 14:38 dune-project
drwxr-xr-x   3 kowaraj  staff   96 Jul  4 14:38 lib
-rw-r--r--   1 kowaraj  staff    0 Jul  4 14:38 ocaml_freq_counter.opam
drwxr-xr-x   4 kowaraj  staff  128 Jul  4 14:38 test

kowaraj@ams-ap-mbp2 src/kj/src_test/ocaml_freq_counter  % dune exec ./bin/main.exe
Hello, World!
```