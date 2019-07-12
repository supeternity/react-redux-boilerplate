from django.conf import settings
from django.db.models import Count

from rest_framework import pagination
from rest_framework.response import Response


class Paginator(pagination.PageNumberPagination):
    page_size_query_param = settings.REST_FRAMEWORK.get('PAGINATE_BY_PARAM') if hasattr(settings, 'REST_FRAMEWORK') else None
    __qs = None

    def get_paginated_response(self, data):
        groupes = []
        aggregate_sqs = {}
        period = self.request.query_params.get('grouped_period')
        # fields_sqs = self.request.query_params.getlist('grouped_sqs')
        if hasattr(self.__qs, '_group_periods'):
            if period and self.__qs.exists() and period in self.__qs._group_periods:
                groupes = self.__qs.annotate_group_with_dt().values(f'dt_{period}').annotate(c=Count(f'dt_{period}')).values_list(f'dt_{period}', flat=True).order_by(f'dt_{period}')

                # if hasattr(self.__qs, 'aggregate_with_periods'):
                #     aggregate_sqs = self.__qs.aggregate_with_periods(*fields_sqs, period=period)
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'page_size': self.get_page_size(self.request),
            'results': data,
            'groupes': groupes,
            'aggregate_sqs': aggregate_sqs,
        })

    def paginate_queryset(self, queryset, request, view=None):
        self.__qs = queryset
        return super().paginate_queryset(queryset, request, view)
