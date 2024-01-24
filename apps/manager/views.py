from django.shortcuts import render
from services.models import Budgets

def list_budgets(request):
    budgets = Budgets.objects.all()
    return render(request, 'list_budget.html', {'budgets': budgets})