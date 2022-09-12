
from core.views import PaymentSummaryCards, PaymentRecentsTable, PaymentTrackerChart
from django.urls import path

payments_summary_cards = PaymentSummaryCards.as_view({ 'get': 'list' })
payments_recents_table = PaymentRecentsTable.as_view({ 'get': 'list' })
payments_tracker_chart = PaymentTrackerChart.as_view({ 'get': 'list' })

urlpatterns = [
    path('payments/summary/', payments_summary_cards, name='payments_summary_cards'),
    path('payments/recents/', payments_recents_table, name='payments_recents_table'),
    path('payments/tracker/', payments_tracker_chart, name='payments_tracker_chart'),
]