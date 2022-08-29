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
            result[status]['percentage'] = result[status]['count']/result['Total']['count']*100
        return Response(result)


class PaymentRecentsTable(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)    
    
    def list(self, request):
        merchands_df = pd.DataFrame(merchand_service.get_merchands_mock())
        payments_df = pd.DataFrame(payment_service.get_payments_mock())
        result = pd.merge(merchands_df, payments_df, on='merchand_id', how='inner')
        result = result.sort_values(by='datetime', ascending=False).tail(10)
        return Response(json.loads(result.to_json(orient="records")))