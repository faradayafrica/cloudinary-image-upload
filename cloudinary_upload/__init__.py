# Navtive import
import os, datetime, json, time

# cloudinary import
from cloudinary import config as cloudinary_config
from cloudinary.uploader import upload
from cloudinary.utils import api_sign_request


# cloudinary config
CLOUDINARY_NAME="faraday-africa"
CLOUDINARY_API_KEY="372228664337547"
CLOUDINARY_API_SECRET="711Qcxf2zOLp35l-ALMmZVoDUW0"

cloudinary_config(
    cloud_name=CLOUDINARY_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)


# convert datetime to unix timestamp
datetime_now = datetime.datetime.now()
timestamp = time.mktime(datetime_now.timetuple())


def sign_cloudinary_request(time_parmas):
    """
    It takes a request and a time parameter, and returns a signature
    
    :param request: The request object
    :param time parameter: The current time in Unix epoch format
    :return: A dictionary with the timestamp and the signature.
    """
    data = api_sign_request(params_to_sign=time_parmas, api_secret=CLOUDINARY_API_KEY)
    return data


def upload_image_cloudinary(image_file="", time_stamp=timestamp):
    """
    It takes in a timestamp and returns a signed request to cloudinary
    
    :param image_file: The image to be uploaded
    :param time_stamp: This is the time stamp that is used to sign the request
    :return: A dictionary with the following keys:
        - public_id
        - version
        - signature
        - width
        - height
        - format
        - resource_type
        - created_at
        - tags
        - bytes
        - type
        - etag
        - url
        - secure_url
        - original_filename
    """
    
    # Sign request going to cloudinary
    signed_request = sign_cloudinary_request({"timestamp": timestamp})

    # Responsible for uploading image to cloudinary
    data = upload(
        file=image_file,
        timestamp=timestamp,
        signature=signed_request,
        tags=['image_ad', 'NAPI']
    )
    return data
