class TimezoneMiddleWare(object):

    def process_request(self, request):
        from django.utils import timezone
        import pytz
        from settings import TIME_ZONE
        if request.user.is_authenticated():
            timezone_selected = request.user.timezone
            if not timezone_selected:
                timezone_selected = TIME_ZONE
            timezone.activate(pytz.timezone(timezone_selected))
        else:
            timezone.deactivate()