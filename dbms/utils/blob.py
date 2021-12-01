#!/usr/bin/python
import io
import PIL.Image as Image

class BlobData:
    
    @staticmethod
    def image_to_bytesarray( 
            path_file: str
        ):
        try:
            with open(path_file, 'rb') as image:
                i = image.read()
                b = bytearray(i)

            return b
        
        except Exception as e:
            print(e)
    
    
    @staticmethod
    def bytesarray_to_image(
            b: bytes
        ):
        try:
            image = Image.open(io.BytesIO(b))

            return image
        
        except Exception as e:
            print(e)