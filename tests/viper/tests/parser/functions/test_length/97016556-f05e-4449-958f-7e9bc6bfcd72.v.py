
y: bytes <= 10

@public
def foo(inp: bytes <= 10) -> num:
    x = slice(inp, start=1, len=5)
    self.y = slice(inp, start=2, len=4)
    return len(inp) * 100 + len(x) * 10 + len(self.y)
    