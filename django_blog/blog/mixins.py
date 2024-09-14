from django.contrib.auth.mixins import UserPassesTestMixin


class UserPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user