# Create your views here.
from django.core.management import call_command
from rest_framework import viewsets, status
from rest_framework.decorators import action  # Import the action decorator
from rest_framework.response import Response
from analysis.models import Company, FinancialDocument, FinancialIndicator
from analysis.serializers import CompanySerializer, FinancialDocumentSerializer, FinancialIndicatorSerializer
from analysis.management.commands.fetch_financial_data import fetch_financial_data as financial_data
from analysis.configs import ALPHA_VANTAGE_API_KEY

class CompanyViewSet(viewsets.ViewSet):
    def list(self, request):
        """List all companies."""
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Add a new company."""
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='fetch-financial-data')
    def fetch_financial_data(self, request):
        """Fetch and update financial data for a specific company."""
        company_id = request.data.get('company_id')
        num_of_exercise_years = int(request.data.get('num_of_exercise_years'))
        report_type = request.data.get('report_type')

        try:
            company = Company.objects.get(id=company_id)
            # Update global settings if needed
            #from analysis.configs import NUM_OF_EXERCICES_YEARS
            data = financial_data(company.symbol, report_type, num_of_exercise_years);

            # Trigger data fetch
            # call_command('fetch_financial_data')      #Call the fetch_financial_data command file     /analysis/management/fetch_financial_data.py
            # financial_data('IBM', report_type);
            if data is None:
                return Response({'error': 'No data found.'}, status=status.HTTP_404_NOT_FOUND)

             # Retornar os dados juntamente com o tipo de relatório
            return Response({'message': f"Data fetched for {company.name}.", 'data': data,  'report_type': report_type}, status=status.HTTP_200_OK)

            # return Response({'message': f"Data fetch initiated for {company.name}."}, status=status.HTTP_200_OK)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
