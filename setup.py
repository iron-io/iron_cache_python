from setuptools import setup

setup(
        name = "iron-cache",
        py_modules = ["iron_cache"],
        install_requires = ["iron_core"],
        version = "0.2.0",
        description = "Client library for IronCache, the cache-in-the-cloud provided by Iron.io.",
        author = "Iron.io",
        author_email = "thirdparty@iron.io",
        url = "https://www.github.com/iron-io/iron_cache_python",
        keywords = ["Iron.io", "cache", "iron_cache"],
        classifiers = [
                "Programming Language :: Python",
                "Programming Language :: Python :: 3",
                "Intended Audience :: Developers",
                "Operating System :: OS Independent",
                "Development Status :: 2 - Pre-Alpha",
                "License :: OSI Approved :: BSD License",
                "Natural Language :: English",
                "Topic :: Internet",
                "Topic :: Internet :: WWW/HTTP",
                "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        long_description = """\
IronCache client library
------------------------

This package wraps the IronCache API. It provides a simple and intuitive 
way to interact with the IronCache service.

IronCache is a service provided by Iron.io. It is a temporary key/value 
storage mechanism built on cloud providers. It provides a cache that 
is reliable and scales based on demand, without requiring developers to 
provision servers themselves."""
)
