from django.shortcuts import render
from django.views.generic import View
from .models import Counterparty
from django.db.models import Q
from .forms import AddCounterpartyForm, ChangeCounterpartyForm


class CounterpartyList(View):
    def get(self, request):
        # counterparty = Counterparty.objects.all()
        search_query = request.GET.get('search', '')
        #print("AAA ", search_query)
        if search_query != "":
            search_outLine = Counterparty.objects.filter(
                Q(firstName__icontains=search_query) |
                Q(lastName__icontains=search_query) |
                Q(telephone__icontains=search_query) |
                Q(adress__icontains=search_query))
        else:
            search_outLine = ""
        # print("12333123  ", search_outLine[0].photo)

        context = {"counterparty": search_outLine}
        return render(request, 'counterparty/List.html', context)
    # def post(self, request):
    #
    #     context = {"counterparty": search_outLine}
    #     return render(request, 'counterparty/counterpartyList.html', context)

class AddCounterparty(View):
    def get(self, request):
        form = AddCounterpartyForm(None)
        print("1 ", form)
        context ={
            'form': form
        }

        return render(request, 'counterparty/add.html', context)
    def post(self, request):
        print(request.FILES)
        counterparty = AddCounterpartyForm(request.POST, request.FILES or None)
        if counterparty.is_valid():
            #print(counterparty.cleaned_data)
            if "photo" in request.FILES:
                counterparty.photo = request.FILES['photo']
            counterparty.save(commit=True)
            return render(request, 'counterparty/List.html', {"counterparty": ""})
        return render(request, 'counterparty/List.html', {"counterparty": ""})


class ChangeCounterparty(View):
    def get(self, request, change):
        choise = Counterparty.objects.get(telephone=change)
        form = ChangeCounterpartyForm(instance=choise)
        context = {
            "form": form,
        }
        return render(request, "counterparty/change.html", context)


