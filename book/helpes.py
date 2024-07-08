import uuid


class SaveMedia(object):
    def save_booook_image_path(instance, filename):
        image_path = filename.split('.')[-1]