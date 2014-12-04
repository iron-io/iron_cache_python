# IronCache Python Client

[IronCache](http://www.iron.io/products/cache) is a scalable, managed cache 
from [Iron.io](http://www.iron.io).

## Getting Started

### Get Credentials

To use IronCache, you need to [sign up](https://hud.iron.io/users/new) and 
get your [OAuth token](https://hud.iron.io/tokens).

### Install iron_cache_python

You can install iron_cache_python in two ways:

#### pip/easy_install

iron_cache_python is available in the Python Package Index as "iron_cache". 
This means you can run `pip install iron_cache` or `easy_install iron_cache` 
from your command line to download iron_cache_python and all its dependencies.

#### From Source

You can also [download the source](https://github.com/iron-io/iron_cache_python) 
from Github. Once you have the source, you can run `python setup.py install` 
from the directory containing the source code to install iron_cache_python.

**Note**: You will need the [iron_core_python](https://github.com/iron-io/iron_core_python) 
module for iron_cache_python to function.

### Configure Your Client

iron_cache_python conforms to the [standard Iron.io configuration scheme](http://dev.iron.io/cache/reference/configuration/) 
that all official libraries use. This means your config files will work across 
languages and products.

### Put Items In the Cache

```python
from iron_cache import *

cache = IronCache()
item = cache.put(cache="test_cache", key="mykey", value="Hello IronCache!")
print item.value
```

### Get an Item In the Cache

```python
from iron_cache import *

cache = IronCache()
try:
    item = cache.get(cache="test_cache", key="mykey")
except:
    item = None    
print item.value if item else print None
```

### Increment an Item's Value

```python
from iron_cache import *

cache = IronCache()
cache.increment(cache="test_cache", key="mykey", amount=10)
```

### Delete an Item From the Cache

```python
from iron_cache import *

cache = IronCache()
try:
    cache.delete(cache="test_cache", key="mykey")
except:
   pass
```

## License

This software is released under the BSD 2-Clause License. You can find the full 
text of this license under LICENSE.txt in the module's root directory.

## More Documentation & Support

More documentation can be found in the [Iron.io Dev Center](http://dev.iron.io).

Iron.io offers a [public support chatroom](http://get.iron.io/chat) that is 
staffed by employees around the clock. We would be more than happy to assist you.
