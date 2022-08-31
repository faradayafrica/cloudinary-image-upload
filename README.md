# About
This library allows you to upload a signed image to cloudinary effectively. 

## Installation
    pip install cloudinary-upload

In the file (.py) that you wish to use it, import the library. <br>

    from cloudinary_upload import upload_image_cloudinary

    upload_true = upload_image_cloudinary(image_file="/path/to/image.png")
    

The `upload_true` variable is going to give you a bunch of meaningful information from cloudinary, you can get the image_url by printing: <br>

    print("Image URL: ", upload_true['url'])

<br>

## Contribute

All contributions are welcome:

- Read the issues, Fork the project and do a Pull Request.
- Request a new topic creating a `New issue` with the `enhancement` tag.
- Find any kind of errors in the `README` and create a `New issue` with the details or fork the project and do a Pull Request.
- Suggest a better or more pythonic way for existing examples.