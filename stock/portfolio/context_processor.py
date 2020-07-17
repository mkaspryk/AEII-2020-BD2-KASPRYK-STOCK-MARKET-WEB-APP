from currencies.models import Currency

def user_balance_context(request):
    if request.user.is_authenticated:
        balance = request.user.userwallet.calculate_balance()
        return {'user_balance_context': balance}
    return {}


