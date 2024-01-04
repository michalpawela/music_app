"""photo_path = os.path.join(artists_imgs_directory, photo.filename)
            photo.save(photo_path)

            photo_path_bytes = photo_path.encode('ascii')
            base64_bytes = base64.b64encode(photo_path_bytes)
            base64_string = base64_bytes.decode('ascii')
            existing_artist.PhotoPath = base64_string"""