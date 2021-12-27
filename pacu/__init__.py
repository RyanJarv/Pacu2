from pkg_resources import DistributionNotFound, get_distribution
from pacu.config import Config


try:
    __version__ = get_distribution('pacu').version
except DistributionNotFound:
    __version__ = '(local)'
