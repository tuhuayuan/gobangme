# -*- coding: utf8 -*-
"""
"""
import threading
from tornado.ioloop import IOLoop
from tornado.options import define, options
from sqlalchemy import create_engine, MetaData

define("db_type", default="mysql", help="mysql default")
define("db_user", default="dev", help="dev default")
define("db_password", default="dev", help="dev default")
define("db_host", default="localhost", help="localhost default")
define("db_name", default="dev", help="dev default")
define("db_port", default=3306, help="3306 default", type=int)


class Backend(object):
    """Sqlalchemy backend
    """
    #singleton lock
    _instance_lock = threading.Lock()

    def __init__(self):
        """singleton object, use instance()
        """
        self._engine = create_engine('%s://%s:%s@%s:%d/%s',
            (options.db_type),
            (options.db_user),
            (options.db_password),
            (options.db_host),
            (options.db_port),
            (options.db_name),
        )
        self._metadata = MetaData(bind=self._engine)

    @staticmethod
    def instance():
        """Return a global Backend instance
        """
        if not hasattr(Backend, "_instance"):
            with Backend._instance_lock:
                if not hasattr(Backend, "_instance"):
                    Backend._instance = Backend()
        return Backend._instance

    @property
    def connect(self):
        return self._engine.connect()

    @property
    def metadata(self):
        """all model use same metadata
        """
        return self._metadata

