# Intro

Figuring out the difference between ReasonML and ReScript on 2021.09.19

There was ReasonML with bucklescript. Then it turned into ReScript (with bucklescript). 

- What happened to ReasonML now?
- What is `esy`?

# Summary

## ReasonML
- devs:...? Jordan Walke? React.. ?
- run for native: `esy` + `dune`
- run for browser: `ReScript` or `Js_of_ocaml`
- compiles into native or JS

## ReScript 
- developer: Hongbo Zhang +(Hongbo, Cheng, Cristiano, Maxim, Patrick, Ricky).
- development: The compiler will also continue to acquire upstream OCaml features when relevant.
- runs `rescript` === new name for `bucklescript`
- compiles into `Demo.bs.js`

# Setup

##  ReasonML

- [from reasonml.github.io](herehttps://reasonml.github.io/docs/en/installation)

Reason comes with its own "npm like" package manager called esy:
- npm install -g esy

```
git clone https://github.com/esy-ocaml/hello-reason.git
cd hello-reason
# Install all dependencies (might take a while in the first run)
esy 
# Compile and run Hello.exe
esy x Hello
```

### Building

package.json:
```
  "esy": {
    "build": "dune build -p #{self.name}",
```



## ReScript

- [from rescript-lang.org](https://rescript-lang.org/docs/manual/latest/installation)

Prerequisites:
- Node.js version >= 10
- npm (which comes with Node.js) or Yarn


```
git clone https://github.com/rescript-lang/rescript-project-template
cd rescript-project-template
npm install
npm run build
node src/Demo.bs.js
```

### Building

package.json:
```
  "scripts": {
    "build": "rescript",
    "clean": "rescript clean -with-deps",
    "start": "rescript build -w"
  },
```