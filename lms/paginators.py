from rest_framework.pagination import PageNumberPagination


class LessonPaginator(PageNumberPagination):
    """Пагинатор для вывода списка уроков."""

    page_size = 8
    page_size_query_param = "page_size"
    max_page_size = 20


class CoursePaginator(PageNumberPagination):
    """Пагинатор для вывода списка курсов."""

    page_size = 4
    page_size_query_param = "page_size"
    max_page_size = 10
