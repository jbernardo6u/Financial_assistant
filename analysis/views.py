# Create your views here.
from django.core.management import call_command
from rest_framework import viewsets, status
from rest_framework.decorators import action  # Import the action decorator
from rest_framework.response import Response
from analysis.models import Company, FinancialDocument, FinancialIndicator
from analysis.serializers import CompanySerializer, FinancialDocumentSerializer, FinancialIndicatorSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from analysis.models import Company, FinancialIndicator
from analysis.management.commands.calculate_indicators import Command

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
        num_of_exercise_years = request.data.get('num_of_exercise_years')

        try:
            company = Company.objects.get(id=company_id)
            # Update global settings if needed
            #from analysis.configs import NUM_OF_EXERCICES_YEARS
            NUM_OF_EXERCICES_YEARS = int(num_of_exercise_years)

            # Trigger data fetch
            call_command('fetch_financial_data')      #Call the fetch_financial_data command file     /analysis/management/fetch_financial_data.py

            return Response({'message': f"Data fetch initiated for {company.name}."}, status=status.HTTP_200_OK)
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
    @api_view(['POST'])
    def calculate_indicators(request):
        company_id = request.data.get('company_id')
        if not company_id:
            return Response({'error': 'ID de l\'entreprise requis.'}, status=400)

        try:
            company = Company.objects.get(id=company_id)
            calculate_command = Command()
            calculate_command.handle(company=company)
            return Response({'message': f'Indicateurs calculés pour {company.name}.'})
        except Company.DoesNotExist:
            return Response({'error': 'Entreprise introuvable.'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def retrieve(self, request, company_pk, year):
        company = Company.objects.get(pk=company_pk)
        indicator = FinancialIndicator.objects.get(company=company, report_year=year)
        serializer = FinancialIndicatorSerializer(indicator)
        return Response(serializer.data)

    @api_view(['GET'])
    def get_indicators(request):
        indicators = FinancialIndicator.objects.all()
        data = [
            {
                'year': indicator.year,
                'gross_profit_margin': indicator.gross_profit_margin,
                'net_profit_margin': indicator.net_profit_margin,
                # Add other fields as needed
            }
            for indicator in indicators
        ]
        return Response(data)


@api_view(['POST'])
def chatbot_interaction(request):
    user_message = request.data.get('message')
    response_message = f"Réponse automatique pour: {user_message}"  # Simulation
    return Response({'message': response_message})




