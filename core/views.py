from ast import Return
from datetime import date
import json

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.services import MerchandService, PaymentService

import pandas as pd

merchand_service = MerchandService()
payment_service = PaymentService()


class PaymentSummaryCards(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)    
    
    def list(self, request):
        payments_df = pd.DataFrame(payment_service.get_payments_mock())
        result = {}
        result['Total'] = { 
            'total': payments_df['value'].sum(), 
            'count': payments_df['value'].size,
            'percentage': 100.00 }
        statuses = ['Aprovada', 'Pendente', 'Rejeitada']
        for status in statuses:
            query_df = payments_df[payments_df['status'] == status]
            result[status] = { 
                'total': query_df['value'].sum(), 
                'count': query_df['value'].size }
            percentage_part = result[status]['count']/result['Total']['count']
            result[status]['percentage'] = percentage_part*100
        return Response(result)


class PaymentRecentsTable(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)    
    
    def list(self, request):
        merchands_df = pd.DataFrame(merchand_service.get_merchands_mock())
        payments_df = pd.DataFrame(payment_service.get_payments_mock())
        result = pd.merge(merchands_df, payments_df, on='merchand_id', how='inner')
        result = result.sort_values(by='datetime', ascending=True).tail(10).iloc[::-1]
        result = json.loads(result.to_json(orient="records"))
        return Response(result)


class PaymentTrackerChart(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        period = request.GET.get('period', 'month')
        payments_df = pd.DataFrame(payment_service.get_payments_mock())
        payments_df = payments_df.sort_values(by='datetime', ascending=True)
        
        if period == 'day':
            offset = pd.DateOffset(hours=11)
            str_format = '%Y-%m-%d %H'
            output_format = '%Hh'
            range_freq = 'H'
        elif period == 'week':
            offset = pd.DateOffset(days=6)
            str_format = '%Y-%m-%d'
            output_format = '%a'
            range_freq = 'D'
        elif period == 'month':
            offset = pd.DateOffset(months=11)
            str_format = '%Y-%m'
            output_format = '%b'
            range_freq = 'M'

        # Filtering by period
        now = pd.Timestamp.now(tz='America/Fortaleza').tz_localize(None)
        payments_df['datetime'] = pd.to_datetime(payments_df['datetime']).dt.strftime(str_format)
        initial_time = (now - offset).strftime(str_format)
        payments_df = payments_df[payments_df['datetime'] > initial_time]
        
        # Extracting data
        periods = pd.date_range(initial_time, now, freq=range_freq).strftime(str_format)
        datetime_group = payments_df.groupby(by='datetime')
        payments = datetime_group.sum('value')['value']
        stores = datetime_group['merchand_id'].nunique()
        result = pd.merge(payments, stores, left_index=True, right_index=True)
        result = result.reindex(periods.array, fill_value=0)

        # Formatting and response
        result = result.reset_index(level=0).iloc[::-1]
        result['datetime'] = pd.to_datetime(result['datetime']).dt.strftime(output_format)
        result = json.loads(result.to_json(orient="records"))
        return Response(result) 