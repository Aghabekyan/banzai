from rest_framework.renderers import BrowsableAPIRenderer

from .settings import api_settings
from .util import camelize


class CamelCaseJSONRenderer(api_settings.RENDERER_CLASS):
    def render(self, data, *args, **kwargs):
        return super().render(camelize(data), *args, **kwargs)


class CamelCaseBrowsableAPIRenderer(BrowsableAPIRenderer):
    def render(self, data, *args, **kwargs):
        return super(CamelCaseBrowsableAPIRenderer, self).render(
            camelize(data), *args, **kwargs
        )
