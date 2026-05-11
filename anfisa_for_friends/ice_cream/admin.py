from django.contrib import admin
from .models import Category, IceCream, Topping, Wrapper

# admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(Wrapper)


# Этот вариант сработает для всех моделей приложения.
# Вместо пустого значения в админке будет отображена строка "Не задано".
admin.site.empty_value_display = 'Не задано'


# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.StackedInline[IceCream]):
    model = IceCream
    extra = 0
    filter_horizontal = ('toppings',)


class CategoryAdmin(admin.ModelAdmin[Category]):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


# Создаём класс, в котором будем описывать настройки админки:
class IceCreamAdmin(admin.ModelAdmin[IceCream]):
    # В этом классе опишем все настройки, какие захотим.
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)

    # Это свойство сработает для всех полей этой модели.
    # Вместо пустого значения будет выводиться строка "Не задано".
    empty_value_display = 'Не задано'

    # Указываем, для каких связанных моделей нужно включить такой интерфейс:
    filter_horizontal = ('toppings',)


# Регистрируем новый класс:
# указываем, что для отображения админки модели IceCream
# вместо стандартного класса нужно использовать класс IceCreamAdmin
admin.site.register(IceCream, IceCreamAdmin)


admin.site.register(Category, CategoryAdmin)
