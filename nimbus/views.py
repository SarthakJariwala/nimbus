from django.contrib.auth.decorators import login_required
from inertia import render


@login_required
def home(request):
    return render(request, "Index", props={"user": request.user})
