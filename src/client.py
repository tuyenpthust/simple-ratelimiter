import json


class Client(object):
  """Simple fake request sending client with built-in rate limiting."""
  def __init__(self, limiter):
    self.send = limiter.wrap(self._send_impl)

  def _send_impl(self, req):
    print "Sending request (%s)" % json.dumps(req)
