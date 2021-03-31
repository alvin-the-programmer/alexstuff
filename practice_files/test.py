def foo(bar=[]):
    bar.append('hi')
    print(bar)


foo()  # the state of bar will persist across all of these top level calls, typically not desireable
foo()
foo()


def foo2(bar):
    bar.append('hi')
    print(bar)


foo2([])
foo2([])
foo2([])
