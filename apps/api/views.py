from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Company

import json

class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                data = {'message':'Success', 'company': company}
            else:
                 data = {'message':"Compan not found..."}
            
            return JsonResponse(data)
        else:
            companies = list(Company.objects.values())
            if len(companies)>0:
                data = {'message':"Success","companies":companies}
            else:
                data = {'message':"Companies not found...",}

        return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Company.objects.create(
                name=jd['name'],
                website=jd['website'],
                foundation=jd['foundation']
                )
        data = {'message':"Success"}
        return JsonResponse(data)
    
    def put(self, request, id):
        jdata = json.loads(request.body)
        company = list(Company.objects.filter(id=id).values())
        if len(company) > 0:
            company = Company.objects.get(id=id)
            company.name = jdata['name']
            company.website = jdata['website']
            company.foundation = jdata['foundation']
            company.save()
            data = {'message':"Success"}
        else :
            data = {'message':"Compan not found..."}
        return JsonResponse(data)
    
    def delete(self, request, id):
        company = list(Company.objects.filter(id=id).values())
        
        if len(company) > 0:
            Company.objects.filter(id=id).delete()
            data = {'message':"Success"}
        else :
            data =  {'message':"Compan not found..."}
        return JsonResponse(data)
    