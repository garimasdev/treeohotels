from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# customer dashboard
@login_required
def customer_dashboard(request):
    return render(request, 'db-dashboard.html')



# vendor or agent dashboard 
@login_required
def vendor_dashboard(request):
    return render(request, 'db-vendor-dashboard.html')
