from flask_admin.contrib.sqla import ModelView


class UsersAdminView(ModelView):
    column_searchable_list = ('username', 'email',)
    column_editable_list = ('username', 'email', 'created_date',)
    column_filters = ('username', 'email',)
    column_sortable_list = ('username', 'email', 'active', 'created_date',)
    column_default_sort = ('created_date', True)
#created a new class called users admin that
#inherits from Model View