#!/usr/bin/python
import io
import PIL.Image as Image

class BlobData:
    
    @staticmethod
    def image_to_bytesarray( 
            path_file: str
        ):
        """
        A method which converts an image to bytes array.

        Args:
            path_file (str): The path of image file.

        Returns:
            b (bytes): The image as bytes array. 
        """
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
        """
        A method which converts bytes array to image.

        Args:
            b (bytes): The bytes array which corresponds to an image.

        Returns:
            image (Image): The image as PIL.Image type.
        """
        try:
            image = Image.open(io.BytesIO(b))

            return image
        
        except Exception as e:
            print(e)