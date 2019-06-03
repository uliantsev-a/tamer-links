from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings
from rest_framework.response import Response
from collections import OrderedDict
import math


class StandardResultsSetPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        next_page = self.page.next_page_number() if self.page.has_next() else None
        prev_page = self.page.previous_page_number() if self.page.has_previous() else None

        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('count_page', math.ceil(self.page.paginator.count / api_settings.PAGE_SIZE)),
            ('next', next_page),
            ('previous', prev_page),
            ('page_size', api_settings.PAGE_SIZE),
            ('results', data),
        ]))
