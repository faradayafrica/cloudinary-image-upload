# Navtive import
import os, datetime, json, time

# cloudinary import
from cloudinary.uploader import upload
from cloudinary.utils import api_sign_request


CLOUDINARY_NAME = os.getenv("CLOUDINARY_NAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_SECRET_KEY = os.getenv("CLOUDINARY_API_SECRET")



def sign_cloudinary_request(request, time_parmas):
    """
    It takes a request and a time parameter, and returns a signature
    
    :param request: The request object
    :param time parameter: The current time in Unix epoch format
    :return: A dictionary with the timestamp and the signature.
    """
    data = api_sign_request(params_to_sign=time_parmas, api_secret=CLOUDINARY_SECRET_KEY)
    return data


async def upload_image_cloudinary(request, profile_picture, signature):
    
    # convert datetime to unix timestamp
    datetime_now = datetime.datetime.now()
    timestamp = time.mktime(datetime_now.timetuple())
    
    # Sign request going to cloudinary
    signed_request = sign_cloudinary_request(
        request=request, params={"timestamp": timestamp}
    )
    
    print("Signed Request: ", signed_request)
    

    
    # async with httpx.AsyncClient() as client:
        
    #     data = {
    #         "file": profile_picture,
    #         "public_id": profile_picture,
    #         "signature": signature,
    #         "api_key": CLOUDINARY_API_KEY,
    #         "timestamp": timestamp
    #     }
        
    #     url = f"https://api.cloudinary.com/v1_1/{CLOUDINARY_NAME}/image/upload"
    #     response = await client.post(url, data=json.dumps(data))
        
    #     if response.status_code == 200:
    #             response_data = response.json()
    #             return response_data["status"], response_data["data"]

        
    
    # Responsible for uploading image to cloudinary
    # data = upload(
    #     file=profile_picture,
    #     timestamp=timestamp,
    #     signature=signature,
    #     crop='limit',
    #     width='2000',
    #     height='2000',
    #     eager=[
    #         {'width': 200, 'height': 200,
    #          'crop': 'thumb', 'gravity ': 'auto',
    #          'radius': 20, 'effect': 'sepia'},
    #         {'width': 100, 'height': 150,
    #          'crop': 'fit', 'format ': 'png'}
    #     ],
    #     tags=['image_ad', 'NAPI']
    # )
    # return data
