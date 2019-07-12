from backend.base.utils import convert_base64


class CoverMixin(object):

    image_field = None

    def create(self, request, *args, **kwargs):
        if self.image_field is not None:
            cover = request.data.get(self.image_field)
            request.data[self.image_field] = convert_base64(cover) if cover else None
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if self.image_field is not None:
            cover = request.data.get(self.image_field)
            if cover:
                request.data[self.image_field] = convert_base64(cover)
            elif cover == '':
                request.data[self.image_field] = None
        return super().update(request, *args, **kwargs)
