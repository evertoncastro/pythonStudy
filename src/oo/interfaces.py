import abc


class HttpRequest:

    def request(self):
        raise NotImplementedError


class HttpGet(HttpRequest):
    # This class will try to execute the method request to receive a NotImplementedError
    ...


class File(abc.ABC):

    @abc.abstractmethod
    def parse_content(self):
        return 'parsed content'


class PDFFile(File):
    # In runtime the interpreter will notice that this class hasn't implemented the interface abstract error
    # and raise a TypeError
    ...


if __name__ == '__main__':

    # req_get = HttpGet()
    # req_get.request()
    pdf_file = PDFFile()
    print(pdf_file.parse_content())