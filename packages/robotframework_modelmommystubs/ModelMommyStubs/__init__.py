from model_mommy import mommy
from django.apps import apps


class ModelMommyStubs(object):
    def create_stub(self, app_name):
        appconfs = apps.get_app_config(app_name)
        for model in appconfs.get_models():
            mommy.make(model)
