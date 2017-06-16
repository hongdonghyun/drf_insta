from .forms import LoginForm, SignupForm


def forms(request):
    context = {
        'login_form': LoginForm,
        'sign_form': SignupForm,
    }
    return context
