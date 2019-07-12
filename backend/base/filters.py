from rest_framework.filters import SearchFilter

from backend.base.utils import lang_switcher


class LangSwitcherSearchFilter(SearchFilter):
    """
    Класс фильтрации для поиска. Если не найдено по искомой строке ни одного результата, то изменяет раскладку и ищет
    на другом языке и возвращает результат. Переводит только с английской раскладки на русскую.
    """

    def filter_queryset(self, request, queryset, view):
        qs = super().filter_queryset(request, queryset, view)
        if not qs.exists() and request.query_params.get('search'):
            request.query_params._mutable = True
            request.query_params['search'] = lang_switcher(request.query_params['search'])
            request.query_params._mutable = False
            qs = super().filter_queryset(request, queryset, view)
        return qs
