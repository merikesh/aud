from .base import *
from .base import __version__

from .generated import __usd_version__

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
__path__.append(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'generated'
))