from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from analysis.models import Company, FinancialDocument, FinancialIndicator
from analysis.serializers import CompanySerializer, FinancialDocumentSerializer, FinancialIndicatorSerializer

class CompanyViewSet(viewsets.ViewSet):
    def list(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        company = Company.objects.get(pk=pk)
        financial_documents = FinancialDocument.objects.filter(company=company)
        serializer = FinancialDocumentSerializer(financial_documents, many=True)
        return Response(serializer.data)

class IndicatorViewSet(viewsets.ViewSet):
    def retrieve(self, request, company_pk, year):
        company = Company.objects.get(pk=company_pk)
        indicator = FinancialIndicator.objects.get(company=company, report_year=year)
        serializer = FinancialIndicatorSerializer(indicator)
        return Response(serializer.data)
