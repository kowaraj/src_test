
def g():
    def f():
        print("var_global = ", var_global)
        print("var_g = ", var_g)
        return

    var_g = 777
    f()
    return

var_global = 666
g()


