import iron_core
import urllib
try:
    import json
except:
    import simplejson as json


class Item:
    cache = None
    key = None
    value = None

    def __str__(self):
        if self.value is not None:
            return self.value
        if self.key is not None:
            return "IronCache Item '%s'" % self.key
        if self.cache is not None:
            return "IronCache Item in Cache '%s'" % self.cache
        return "IronCache item"

    def __repr__(self):
        if self.value is not None:
            if self.cache is not None and self.key is not None:
                return "%s[%s]: %s" % (self.cache, self.key, self.value)
            elif self.cache is None:
                return "%s: %s" % (self.key, self.value)
            else:
                return "%s" % self.value
        else:
            return "IronCache Item"

    def __init__(self, values={}, **kwargs):
        for k in kwargs.keys():
            values[k] = kwargs[k]

        for prop in values.keys():
            if prop == "cache":
                self.cache = values["cache"]
            elif prop == "key":
                self.key = values["key"]
            elif prop == "value":
                self.value = values["value"]


class IronCache:
    NAME = "iron_cache_python"
    VERSION = "0.1.0"
    client = None
    name = None

    def __init__(self, name=None, **kwargs):
        """Prepare a configured instance of the API wrapper and return it.

        Keyword arguments are passed directly to iron_core_python; consult its
        documentation for a full list and possible values."""
        if name is not None:
            self.name = name
        self.client = iron_core.IronClient(name=IronCache.NAME,
                version=IronCache.VERSION, product="iron_cache", **kwargs)

    def caches(self, options={}):
        """Query the server for a list of caches, parse the JSON response, and
        return the result.

        Keyword arguments:
        options -- a dict of arguments to send with the request. See
                   http://dev.iron.io/cache/reference/api/#list_caches for more
                   information on defaults and possible values.
        """
        query = urllib.urlencode(options)
        url = "caches"
        if query != "":
            url = "%s?%s" % (url, query)
        result = self.client.get(url)
        return [cache["name"] for cache in result["body"]]

    def get(self, key, cache=None):
        """Query the server for an item, parse the JSON, and return the result.

        Keyword arguments:
        key -- the key of the item that you'd like to retrieve. Required.
        cache -- the name of the cache that the item resides in. Defaults to
                 None, which uses self.name. If no name is set, raises a
                 ValueError.
        """
        if cache is None:
            cache = self.name
        if cache is None:
            raise ValueError("Cache name must be set")
        cache = urllib.quote_plus(cache)
        key = urllib.quote_plus(key)
        url = "caches/%s/items/%s" % (cache, key)
        result = self.client.get(url)
        return Item(values=result["body"])

    def put(self, key, value, cache=None, options={}):
        """Query the server to set the key specified to the value specified in
        the specified cache.

        Keyword arguments:
        key -- the name of the key to be set. Required.
        value -- the value to set key to. Must be a string or JSON
                 serialisable. Required.
        cache -- the cache to store the item in. Defaults to None, which uses
                 self.name. If no name is set, raises a ValueError.
        options -- a dict of arguments to send with the request. See
                   http://dev.iron.io/cache/reference/api/#put_item for more
                   information on defaults and possible values.
        """
        if cache is None:
            cache = self.name
        if cache is None:
            raise ValueError("Cache name must be set")

        if not isinstance(value, basestring) and not isinstance(value,
                (int, long)):
            value = json.dumps(value)

        options["body"] = value
        body = json.dumps(options)

        cache = urllib.quote_plus(cache)
        key = urllib.quote_plus(key)

        result = self.client.put("caches/%s/items/%s" % (cache, key), body,
                {"Content-Type": "application/json"})
        return Item(cache=cache, key=key, value=value)

    def delete(self, key, cache=None):
        """Query the server to delete the key specified from the cache
        specified.

        Keyword arguments:
        key -- the key the item is stored under. Required.
        cache -- the cache to delete the item from. Defaults to None, which
                 uses self.name. If no name is set, raises a ValueError.
        """
        if cache is None:
            cache = self.name
        if cache is None:
            raise ValueError("Cache name must be set")
        cache = urllib.quote_plus(cache)
        key = urllib.quote_plus(key)

        self.client.delete("caches/%s/items/%s" % (cache, key))

        return True

    def increment(self, key, cache=None, amount=1):
        """Query the server to increment the value of the key by the specified
        amount. Negative amounts can be used to decrement.

        Keyword arguments:
        key -- the key the item is stored under. Required.
        cache -- the cache the item belongs to. Defaults to None, which uses
                 self.name. If no name is set, raises a ValueError.
        amount -- the amount to increment the value by. Can be negative to
                  decrement the value. Defaults to 1.
        """
        if cache is None:
            cache = self.name
        if cache is None:
            raise ValueError("Cache name must be set")
        cache = urllib.quote_plus(cache)
        key = urllib.quote_plus(key)

        body = json.dumps({"amount": amount})

        result = self.client.post("caches/%s/items/%s/increment" % (cache,
            key), body, {"Content-Type": "application/json"})
        result = result["body"]
        return Item(values=result, cache=cache, key=key)

    def decrement(self, key, cache=None, amount=1):
        """A convenience function for passing negative values to increment.

        Keyword arguments:
        key -- the key the item is stored under. Required.
        cache -- the cache the item belongs to. Defaults to None, which uses
                 self.name. If no name is set, raises a ValueError.
        amount -- the amount to increment the value by. Can be negative to
                  decrement the value. Defaults to 1.
        """
        amount = amount * -1

        return self.increment(key=key, cache=cache, amount=amount)
