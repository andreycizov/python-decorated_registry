decorated_registry
==================

Implementation of generalised registries for Python.

Allows you to seamlessly create registries of tests, modules, DSLs and RPCs.

Supports arguments and fully typed.

Example
-------

```python
from typing import List, Type
from dataclasses import dataclass
from decorated_registry import Registry, ConstructorPayloadFactory

# framework/abstract.py

@dataclass
class ModuleConfig:
    init_priority: int = -1


class Module:
    pass

# framework/registry.py

application_module: Registry[ModuleConfig, Type[Module]] = Registry(
    payload_factory=ConstructorPayloadFactory(dict)
)

# authentication_mod/impl.py

@application_module
class AuthenticationModule(Module):
    pass


# database_mod/impl.pu

@application_module(init_priority=2)
class DatabaseSessionModule(Module):
    pass

# framework/app.py

def load_modules() -> List[Module]:
    rtn = []
    # ensure modules are loaded in the order given by `ModuleConfig.priority`
    modules_priority = sorted(application_module.items, key=lambda x: x.payload.init_priority)
    for x in modules_priority:
        module_cls: Type[Module] = x.value
        module = module_cls()
        rtn.append(module)
    return rtn


# framework/main.py

def main():
    modules = load_modules()


if __name__ == '__main__':
    main()
```
