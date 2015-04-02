from django.conf.urls import patterns, url

from apps.charts import views

urlpatterns = patterns(
    '',
    url(
        r'^wallet/balance/(?P<chart_type>[\w-]+)/$',
        views.wallet_balance_chart,
        name='wallet_balance_chart',
    ),
)
