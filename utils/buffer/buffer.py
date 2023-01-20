from collections import deque

class ContextBuffer(object):
    """
    """
    def __init__(self, maxlen):
        """
        """
        self._inner_buffer = []
        self._maxlen = maxlen
    
    def _extend(self, content):
        """
        """
        content_list = content.split(' ')
        if len(self._inner_buffer) + len(content_list) > self._maxlen:
            self._inner_buffer = content_list
        else:
            self._inner_buffer = self._inner_buffer + content_list
    
    def __str__(self) -> str:
        return ' '.join(self._inner_buffer)

    def __add__(self, content: str):
        self._extend(content)
        return self
     