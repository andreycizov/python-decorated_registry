decorated_registry
==================

Implementation of generalised registries for Python.

```python
from decorated_registry import Registry

my_app_register = Registry()

@my_app_register
class MyFirstModule:
    pass


@my_app_register
class MySecondModule:
    pass


def load_app():
    rtn = []
    for x in my_app_register.items:
       initialized_module = x.value() 
       rtn.append(initialized_module)
    return rtn

if __name__ == '__main__':
    modules = load_app()
```
