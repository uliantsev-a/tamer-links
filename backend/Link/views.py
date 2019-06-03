from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from django.http import QueryDict
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from .models import Resource
from .serializers import ResourceSerializer
from .utils import StandardResultsSetPagination


class LinkViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    """
    retrieve:
    Return the original link by short_record or nothing with code 404.
    Example http://<host>/api/link/<short_record>/.
    It use cache from Redis when repeat request.
    Cache limit time from DEFAULT_CACHE_PAGE

    list:
    Return a list of all links on this session.
    Result split of paginate and getting query options for this.
    Example http://<host>/api/link/?page=2
    Pagination response can see in ./utils.py/StandardResultsSetPagination

    create:
    Create a new link between original and short URL.
    Response the dict with base fields the Resource.
    Receive original URL and custom short record (not required).
    """

    serializer_class = ResourceSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'short_link'

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, QueryDict):
            data = request.data.dict()
        else:
            data = request.data

        if not request.session.session_key:
            request.session.save()

        data.update({'session': request.session.session_key})

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @method_decorator(cache_page(settings.DEFAULT_CACHE_PAGE))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Resource.objects
        if self.action == 'list':
            return queryset.filter(session=self.request.session.session_key).order_by('-created')
        return queryset.all()
