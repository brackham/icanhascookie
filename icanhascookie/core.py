__all__ = ['Cookie', 'ask']

class Cookie():
    """A Cookie."""

    def __init__(self, arg):
        super(Cookie, self).__init__()
        self.arg = arg

def ask(n):
    """
    Can I have n cookies?

    Parameters
    ----------
    n: int
        The number of cookies.

    Returns
    -------
    result: list
        The list of cookies.
    """

    result = [Cookie]*n

    return result
