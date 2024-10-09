from flask import Flask, request, render_template, redirect, url_for, flash
import boto3
import os
from config import S3_BUCKET, S3_REGION
from cryptography.fernet import Fernet  # Import Fernet for encryption
from io import BytesIO  # Import BytesIO to create in-memory file-like objects

# Initialize the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'supersecretkey')

# Initialize the S3 client
s3 = boto3.client('s3', region_name=S3_REGION)

# Generate a key for encryption and decryption (store this securely)
encryption_key = Fernet.generate_key()
cipher = Fernet(encryption_key)


### Page 1: Upload Images ###
@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if an image is provided in the form
    if 'image' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))

    image = request.files['image']
    encrypt = request.form.get('encrypt')  # Get encryption checkbox value

    # Check if the user actually selected a file
    if image.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))

    try:
        # Read the image file
        image_data = image.read()

        # Encrypt the image data if the checkbox is checked
        if encrypt:
            encrypted_data = cipher.encrypt(image_data)

            # Create an in-memory file-like object for the encrypted data
            encrypted_fileobj = BytesIO(encrypted_data)

            # Upload the encrypted image to S3
            s3.upload_fileobj(
                encrypted_fileobj,
                S3_BUCKET,
                f'encrypted/{image.filename}',  # Store encrypted images in a separate folder
                ExtraArgs={"ContentType": image.content_type}
            )
            flash(f"Image '{image.filename}' encrypted and uploaded successfully!", 'success')
        else:
            # Upload the original image to S3
            s3.upload_fileobj(
                image,
                S3_BUCKET,
                image.filename,
                ExtraArgs={"ContentType": image.content_type}
            )
            flash(f"Image '{image.filename}' uploaded successfully!", 'success')
    except Exception as e:
        flash(f"Error uploading image: {e}", 'danger')

    return redirect(url_for('index'))


### Page 2: List and Download Images ###
@app.route('/list', methods=['GET', 'POST'])
def list_images():
    show_encrypted = request.form.get('show_encrypted')  # Check if the checkbox is checked
    images = []

    try:
        # List all objects in the S3 bucket
        response = s3.list_objects_v2(Bucket=S3_BUCKET)
        for obj in response.get('Contents', []):
            images.append(obj['Key'])  # Append all images to the list
    except Exception as e:
        flash(f"Error fetching image list: {e}", 'danger')

    # Filter images based on encryption if checkbox is checked
    if show_encrypted:
        images = [img for img in images if 'encrypted/' in img]

    return render_template('list.html', images=images)


@app.route('/download/<filename>')
def download_image(filename):
    try:
        # Generate a presigned URL for downloading the file
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': S3_BUCKET, 'Key': filename},
            ExpiresIn=604800  # Presigned URL expires in 1 week
        )
        return redirect(url)
    except Exception as e:
        flash(f"Error downloading image: {e}", 'danger')
        return redirect(url_for('list_images'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  # Expose Flask to all network interfaces