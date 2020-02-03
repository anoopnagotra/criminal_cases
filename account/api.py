# -*- coding: utf-8 -*-

# # Third Party Stuff
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from . import models, serializers
from rest_framework.decorators import list_route, detail_route
from django.contrib.auth.models import User
from account.serializers import UserSerializer
from base import response



# class UserAuthViewSet(mixins.ListModelMixin,
#                   mixins.RetrieveModelMixin,
#                   viewsets.GenericViewSet):
#
# 	permission_classes = (AllowAny,)
# 	queryset = models.Profile.objects.all()
# 	serializer_class = serializers.ProfileSerializer
#
#
#
# 	# @list_route(methods=['post'])
# 	# def register(self, request):
# 	# 	print("hello in side register")
# 	# 	serialized = UserSerializer()
# 	# 	print("ethe")
# 	# 	return response.Created({"success": "Account successfully created."})
#
# #     permission_classes = (AllowAny,)
# #     queryset = models.City.objects.filter(is_published=True)
# #     serializer_class = serializers.CitySerializer
#
# #     def list(self, request, *args, **kwargs):
# #         queryset = self.get_queryset()
# #         for index, item in enumerate(queryset):
# #             if item.for_festival == True:
# #                 queryset[index].country = "All Fetivals"
# #                 queryset[index].state = "/"
# #         return paginated_response(request, queryset, serializers.CitySerializer)
#
# 	def login(self, request):
# 		print( "I am here in login ")


class UserAuthViewSet(viewsets.ModelViewSet):
    model = models.Profile
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

