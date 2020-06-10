[from here](https://stackoverflow.com/questions/30600978/cpp-usr-bin-ld-cannot-find-lnameofthelibrary)

# Source code

main.c: 

```.cpp
#include "func.h"
int main() {
  func_f();
  return 0;
}
```

func.c:

```cpp
#include "func.h"
void func_f() { }
```

func.h: 
```cpp
void func_f();
```

# Compilation into an executable

Files:
```sh 
15:26:11-apash@ams-vobox100:~/src/test$ ls -la
-rw-r--r--  1 apash apash 37 Jun  8 14:51 func.c
-rw-r--r--  1 apash apash 15 Jun  8 15:26 func.h
-rw-r--r--  1 apash apash 60 Jun  8 15:24 main.c
```

Compile:
```sh
15:26:13-apash@ams-vobox100:~/src/test$ g++ -c func.c -c main.c

15:26:17-apash@ams-vobox100:~/src/test$ ls -la
-rw-r--r--  1 apash apash 1232 Jun  8 15:26 func.o
-rw-r--r--  1 apash apash 1360 Jun  8 15:26 main.o
```

Link:
```sh
15:26:19-apash@ams-vobox100:~/src/test$ ld func.o main.o  -o test

15:26:28-apash@ams-vobox100:~/src/test$ ls -la
-rwxr-xr-x  1 apash apash 1160 Jun  8 15:26 test
```

Object files: 
```
15:32:26-apash@ams-vobox100:~/src/test$ nm func.o
0000000000000000 T _Z6func_fv

15:32:30-apash@ams-vobox100:~/src/test$ nm main.o
0000000000000000 T main
                 U _Z6func_fv
```

```
15:32:34-apash@ams-vobox100:~/src/test$ nm test
0000000000601000 R __bss_start
0000000000601000 R _edata
0000000000601000 R _end
00000000004000b6 T main
00000000004000b0 T _Z6func_fv
```

file:
```
15:32:38-apash@ams-vobox100:~/src/test$ file main.o
main.o: ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped
15:33:54-apash@ams-vobox100:~/src/test$ file test
test: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, not stripped
```

# Shared library

Create: 
```
15:35:38-apash@ams-vobox100:~/src/test$ gcc -shared -fPIC -Wl,-soname,libfunc.so.1 -o libfunc.so.1.5.0 func.o

15:37:23-apash@ams-vobox100:~/src/test$ file ./libfunc.so.1.5.0
./libfunc.so.1.5.0: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, BuildID[sha1]=2614c0dc9bb56eae17ff56d4611f2480dd882594, not stripped
```

Move:
```
15:41:38-apash@ams-vobox100:~/src/test$ ls -la
-rw-r--r--  1 apash apash   37 Jun  8 14:51 func.c
-rw-r--r--  1 apash apash   15 Jun  8 15:26 func.h
-rw-r--r--  1 apash apash   60 Jun  8 15:24 main.c
drwxr-xr-x  3 apash apash   17 Jun  8 15:39 usr

15:41:41-apash@ams-vobox100:~/src/test$ ls -la ./usr/lib/
lrwxrwxrwx 1 apash apash   18 Jun  8 15:39 libfunc.so -> ./libfunc.so.1.5.0
lrwxrwxrwx 1 apash apash   18 Jun  8 15:49 libfunc.so.1 -> ./libfunc.so.1.5.0
-rwxr-xr-x 1 apash apash 7888 Jun  8 15:37 libfunc.so.1.5.0
```

Compile without .so => Error:
```
15:41:02-apash@ams-vobox100:~/src/test$ g++ main.c -o test_with_so
/tmp/apash/ccBB4gaK.o: In function `main':
main.c:(.text+0x5): undefined reference to `func_f()'
collect2: error: ld returned 1 exit status
```

Compile:
```
15:43:59-apash@ams-vobox100:~/src/test$ g++ main.c -L./usr/lib -lfunc -o test_with_so
```

Result:
```
15:44:59-apash@ams-vobox100:~/src/test$ file ./test_with_so
./test_with_so: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.32, BuildID[sha1]=83da4909e0e7fee5d95d7c08ee51fa2ef375d351, not stripped

15:44:38-apash@ams-vobox100:~/src/test$ nm test_with_so
0000000000601034 B __bss_start
0000000000601034 b completed.6355
0000000000601030 D __data_start
0000000000601030 W data_start
0000000000400570 t deregister_tm_clones
00000000004005e0 t __do_global_dtors_aux
0000000000600dd8 t __do_global_dtors_aux_fini_array_entry
00000000004006c8 R __dso_handle
0000000000600de8 d _DYNAMIC
0000000000601034 D _edata
0000000000601038 B _end
00000000004006b4 T _fini
0000000000400600 t frame_dummy
0000000000600dd0 t __frame_dummy_init_array_entry
00000000004007f8 r __FRAME_END__
0000000000601000 d _GLOBAL_OFFSET_TABLE_
                 w __gmon_start__
00000000004006d0 r __GNU_EH_FRAME_HDR
00000000004004d8 T _init
0000000000600dd8 t __init_array_end
0000000000600dd0 t __init_array_start
00000000004006c0 R _IO_stdin_used
0000000000600de0 d __JCR_END__
0000000000600de0 d __JCR_LIST__
00000000004006b0 T __libc_csu_fini
0000000000400640 T __libc_csu_init
                 U __libc_start_main@@GLIBC_2.2.5
000000000040062d T main
00000000004005a0 t register_tm_clones
0000000000400540 T _start
0000000000601038 D __TMC_END__
                 U _Z6func_fv <------------------------ it is OK this time!
                 
```

Run without library => Error:
```
15:50:38-apash@ams-vobox100:~/src/test$ ./test_with_so
./test_with_so: error while loading shared libraries: libfunc.so.1: cannot open shared object file: No such file or directory
```

Run:
```
15:50:44-apash@ams-vobox100:~/src/test$ LD_LIBRARY_PATH=./usr/lib/ ./test_with_so
```

# Theory

[from here](https://stackoverflow.com/questions/30600978/cpp-usr-bin-ld-cannot-find-lnameofthelibrary)

Libraries, in fact, are just the object files which are placed into a single archive 
- by using `ar` tool with a single symbols table which is created by `ranlib` tool.

Compiler, when compiling object files, does not resolve symbols. These symbols will be replaced to addresses by a linker. 

So resolving symbols can be done by two things: 
- the linker and 
- dynamic loader:

#### The linker

`ld`, does 2 jobs:
1. For static libs or simple object files, this linker changes external symbols in the object files to the addresses of the real entities. For example, if we use C++ name mangling linker will change _ZNK3MapI10StringName3RefI8GDScriptE10ComparatorIS0_E16DefaultAllocatorE3hasERKS0_ to 0x07f4123f0.

2. For dynamic libs it only checks if the symbols can be resolved (you try to link with correct library) at all but does not replace the symbols by address. If symbols can't be resolved (for example they are not implemented in the shared library you are linking to) - it throws undefined reference to error and breaks up the building process because you try to use these symbols but linker can't find such symbol in it's object files which it is processing at this time. Otherwise, this linker adds some information to the ELF executable which is:

2.1 `.interp` section - request for an interpreter 
  - dynamic loader to be called before executing, so this section just contains a path to the dynamic loader. 
  
If you look at your executable which depends on shared library (libfunc) for example 
you will see the interp section `readelf -l a.out`:
```
INTERP         0x0000000000000238 0x0000000000400238 0x0000000000400238
               0x000000000000001c 0x000000000000001c  R      1
[Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
```

2.2 `.dynamic` section - a list of shared libraries which interpreter will be looking for before executing. 
You may see them by `ldd` or `readelf`.

`ldd a.out`:
```
     linux-vdso.so.1 =>  (0x00007ffd577dc000)
     libfunc.so.1 => /usr/lib/libfunc.so.1 (0x00007fc629eca000)
     libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fefe148a000)
     /lib64/ld-linux-x86-64.so.2 (0x000055747925e000)
```
`readelf -d a.out`:
```
  Dynamic section at offset 0xe18 contains 25 entries:
  Tag        Type                         Name/Value
  0x0000000000000001 (NEEDED)             Shared library: [libfunc.so.1]
  0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
```

Note that `ldd` also finds all the libraries in your filesystem while `readelf` only shows what libraries does your program need. 
So, all of these libraries will be searched by dynamic loader (next paragraph). The linker works at build time.


#### Dynamic loader

`ld.so` or `ld-linux`

It finds and loads all the shared libraries needed by a program (if they were not loaded before), resolves the symbols by replacing them to real addresses right before the start of the program, prepares the program to run, and then runs it. It works after the build and before running the program. Less speaking, dynamic linking means resolving symbols in your executable before each program start.

Actually, when you run an ELF executable with .interp section (it needs to load some shared libraries) the OS (Linux) runs an interpreter at first but not your program. Otherwise you have an undefined behavior - you have symbols in your program but they are not defined by addresses which usually means that the program will be unable to work properly.

You may also run dynamic loader by yourself but it is unnecessary (binary is /lib/ld-linux.so.2 for 32-bit architecture elf and /lib64/ld-linux-x86-64.so.2 for 64-bit architecture elf).

Why does the linker claim that /usr/bin/ld: cannot find -lblpapi3_64 in your case? Because it tries to find all the libraries in it's known paths. Why does it search the library if it will be loaded during runtime? Because it needs to check if all the needed symbols can be resolved by this library and to put it's name into the .dynamic section for dynamic loader. Actually, the .interp section exists in almost every c/c++ elf because the libc and libstdc++ libraries are both shared, and compiler by default links any project dynamically to them. You may link them statically as well but this will enlarge the total executable size. So, if the shared library can't be found your symbols will remain unresolved and you will be UNABLE to run your application, thus it can't produce an executable. You may get the list of directories where libraries are usually searched by:

Passing a command to the linker in compiler arguments.
By parsing ld --verbose's output.
By parsing ldconfig's output.
Some of these methods are explained here.

Dynamic loader tries to find all the libraries by using:

DT_RPATH dynamic section of an ELF file.
DT_RUNPATH section of the executable.
LD_LIBRARY_PATH environment variable.
/etc/ld.so.cache - own cache file which contains a compiled list of candidate libraries previously found in the augmented library path.
Default paths: In the default path /lib, and then /usr/lib. If the binary was linked with -z nodeflib linker option, this step is skipped.
ld-linux search algorithm

Also, note please, that if we are talking about shared libraries, they are not named .so but in .so.version format instead. When you build your application the linker will look for .so file (which is usually a symlink to .so.version) but when you run your application the dynamic loader looks for .so.version file instead. For example, let's say we have a library test which version is 1.1.1 according to semver. In the filesystem it will look like:

/usr/lib/libtest.so -> /usr/lib/libtest.so.1.1.1
/usr/lib/libtest.so.1 -> /usr/lib/libtest.so.1.1.1
/usr/lib/libtest.so.1.1 -> /usr/lib/libtest.so.1.1.1
/usr/lib/libtest.so.1.1.1
So, to be able to compile you must have all of versioned files (libtest.so.1, libtest.so.1.1 and libtest.so.1.1.1) and a libtest.so file but for running your app you must have only 3 versioned library files listed first. This also explains why do Debian or rpm packages have devel-packages separately: normal one (which consists only of the files needed by already compiled applications for running them) which has 3 versioned library files and a devel package which has only symlink file for making it possible to compile the project.

Resume

After all of that:

You, your colleague and EACH user of your application code must have all the libraries in their system linker paths to be able to compile (build your application). Otherwise, they have to change Makefile (or compile command) to add the shared library location directory by adding -L<somePathToTheSharedLibrary> as argument.
After successful build you also need your library again to be able to run the program. Your library will be searched by dynamic loader (ld-linux) so it needs to be in it's paths (see above) or in system linker paths. In most of linux program distributions, for example, games from steam, there is a shell-script which sets the LD_LIBRARY_PATH variable which points to all shared libraries needed by the game.