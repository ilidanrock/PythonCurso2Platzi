from typing import Callable

def increment2(x): return x + 1


print(increment2(2))

# transform the bellow lambda function with types
FullNameFunction = Callable[[str, str], str]

full_name: FullNameFunction = lambda fn , ln: f"{fn.strip().title()} {ln.strip().title()}"


print(full_name("  leonhard", "EULER"))

