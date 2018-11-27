from tastypie.resources import ModelResource
from api.models import User, Score
from tastypie.authorization import Authorization

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()


class ScoreResource(ModelResource):
    class Meta:
        queryset = Score.objects.all()
        resource_name = 'score'
        authorization = Authorization()
