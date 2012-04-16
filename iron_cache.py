from iron_rest import *
import ConfigParser

class IronCache:
    def __init__(self, project_id=None, token=None, protocol='https',
            host='cache-aws-us-east-1.iron.io', port=443, version=1,
            config=None):
        """Prepare a configured instance of the API wrapper and return it.

        Keyword arguments:
        project_id -- The ID for the project, found on http://hud.iron.io.
                      Defaults to None. project_id or config must be set 
                      (with a project_id value in the config file) or a
                      ValueError will be raised.
        token -- The OAuth2 token that grants access to the project specified
                 by project_id or in the config file. Found on
                 http://hud.iron.io. Defaults to None. token or config must
                 be set (with a token value in the config file) or a ValueError
                 will be raised.
        protocol -- The protocol to use for requests. Defaults to 'https'.
                    Overrides the protocol specified in the config file, if
                    config is set.
        host -- The hostname of the API server. Defaults to
                'cache-aws-us-east-1.iron.io'. Overrides the host specified in
                the config file, if config is set.
        port -- The port to connect to the API server on. Defaults to 443.
                Overrides the port specified in the config file, if config is
                set.
        version -- The version of the API to use. Defaults to 1. Overrides the
                   version specified in the config file, if config is set.
        config -- The path to the config file to use when configuring the
                  client. Should be a valid .ini file. Defaults to None. If
                  None, both token and project_id must be set, or a ValueError
                  will be thrown.
        """
        self.token = None
        self.version = None
        self.project_id = None
        self.protocol = None
        self.host = None
        self.port = None
        self.config = None
        self.client = None

        if config is not None:
            config_file = ConfigParser.RawConfigParser()
            config_file.read(config)
            try:
                self.token = config_file.get("iron_cache", "token")
            except ConfigParser.NoOptionError:
                pass
            try:
                self.project_id = config_file.get("iron_cache", "project_id")
            except ConfigParser.NoOptionError:
                pass
            try:
                self.version = config_file.get("iron_cache", "version")
            except ConfigParser.NoOptionError:
                pass
            try:
                self.protocol = config_file.get("iron_cache", "protocol")
            except ConfigParser.NoOptionError:
                pass
            try:
                self.host = config_file.get("iron_cache", "host")
            except ConfigParser.NoOptionError:
                pass
            try:
                self.port = config_file.get("iron_cache", "port")
            except ConfigParser.NoOptionError:
                pass

        if token is not None:
            self.token = token
        if project_id is not None:
            self.project_id = project_id
        if protocol is not None:
            self.protocol = protocol
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if version is not None:
            self.version = version

        if self.token is None:
            raise ValueError("No token provided.")
        if self.project_id is None:
            raise ValueError("No project_id provided.")
        if self.protocol is None:
            raise ValueError("No protocol specified.")
        if self.host is None:
            raise ValueError("No host specified.")
        if self.port is None:
            raise ValueError("No port specified.")
        if self.version is None:
            raise ValueError("No API version specified.")

        self.client = IronClient(name="iron_cache_python", version="0.1.0",
                host=self.host, project_id=self.project_id, token=self.token,
                protocol=self.protocol, port=self.port,
                api_version=self.version)

    def listCaches(self, options={}):
        """Query the server for a list of caches, parse the JSON response, and
        return the result.

        Keyword arguments:
        options -- a dict of arguments to send with the request. See
                   http://dev.iron.io/cache/reference/api/#list_caches for more
                   information on defaults and possible values.
        """

        return self.client.get("caches")

    def getCache(self, cache, options={}):
        """Query the server for info on a specific cache, parse the JSON, and
        return the result.

        Keyword arguments:
        cache -- the name of the cache to be retrieved. Required.
        options -- a dict of arguments to send with the request. See
                   http://dev.iron.io/cache/reference/api/#get_cache for more
                   information on defaults and possible values.
        """

        return self.client.get("caches/%s" % cache)
