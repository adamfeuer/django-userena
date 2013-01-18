"""
Django accounts management made easy.

"""
VERSION = (1, 1, '2bv-5')

__version__ = '.'.join((str(each) for each in VERSION[:4]))

def get_version():
    """
    Returns string with digit parts only as version.

    """
    return '.'.join((str(each) for each in VERSION[:3]))
