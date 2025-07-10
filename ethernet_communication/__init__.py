try:
    from .accelerator import Accelerator
    from .host import Host
    __all__ = ['Accelerator', 'Host']
except ImportError:
    from .host import Host
    __all__ = ['Host']
