from django.core.files.uploadhandler import FileUploadHandler, StopUpload

class QuotaUploadHandler(FileUploadHandler):
    """ """
    QUOTA = 524288 #500k
    
    def __init__(self, request=None):
        super(QuotaUploadHandler, self).__init__(request)
        self.total_upload = 0
        
    def receive_data_chunk(self, raw_data, start):
        self.total_upload += len(raw_data)
        if self.total_upload >= self.QUOTA:
            raise StopUpload(connection_reset=True)
        return raw_data
            
    def file_complete(self, file_size):
        pass

class CustomUploadError(Exception):
    pass

class ErroringUploadHandler(FileUploadHandler):
    """A handler that raises an exception."""
    def receive_data_chunk(self, raw_data, start):
        raise CustomUploadError("Oops!")
