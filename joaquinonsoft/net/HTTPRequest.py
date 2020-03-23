import urllib.request
import urllib.parse


class HTTPRequest:
    METHOD_GET = "GET"
    METHOD_POST = "POST"

    def __init__(self, url, method="GET", params=None):
        """
        Read a web page given
        :param url: URL to be read
        :param method: HTTP method. Valid values GET, POST
        """
        self.url = url
        self.method = method
        self.params = params

    def read(self):
        resource = None

        if self.method == self.METHOD_POST:
            body_data = urllib.parse.urlencode(self.params).encode("utf-8")
            resource = urllib.request.urlopen(self.url, data=body_data)

        if self.method == self.METHOD_GET:
            str_params = ""
            if self.params is not None:
                str_params = urllib.parse.urlencode(self.params)
            resource = urllib.request.urlopen(self.url + "?" + str_params)

        response = resource.read()

        if resource.headers.get_content_charset() is not None:
            html = response.decode(resource.headers.get_content_charset())
        else:
            html = response.decode("utf-8")

        resource.close()
        return html

