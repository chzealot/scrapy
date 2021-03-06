from scrapy.core.downloader.responsetypes import responsetypes
from scrapy.utils.url import file_uri_to_path
from scrapy.utils.decorator import defers

class FileDownloadHandler(object):

    @defers
    def download_request(self, request, spider):
        filepath = file_uri_to_path(request.url)
        body = open(filepath, 'rb').read()
        respcls = responsetypes.from_args(filename=filepath, body=body)
        return respcls(url=request.url, body=body)
