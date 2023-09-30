from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm
from .models import Expense
# Create your views here.

@login_required
def index(request):
    if request.method == "POST":
        expense = ExpenseForm({"user":request.user, 'name':request.POST['name'], 'amount':request.POST['amount'], 'category':request.POST["category"]})
        if expense.is_valid():
            expense.save()
    elif request.method=="DELETE":
        print("Delete request")
    expenses = Expense.objects.filter(user=request.user)
    ef = ExpenseForm()
    return render(request, 'myapp/index.html', {'expense_form': ef, 'expenses':expenses})