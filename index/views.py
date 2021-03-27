from django.shortcuts import render, HttpResponse
from django.views.generic import View



class Index(View):

    def get(self, request):
        # print(dir(request.user.userprofile.manager))
        # print(request.user.userprofile.manager)
        man = request.user.groups.filter(name='manager').exists()

        context = {"manager": man}
        return render(request, "index/index.html", context)
