from Helpers.Voodoo import *


def test_new_customer_login(request):
    API.api_push(
        "http://parabank.parasoft.com/parabank/services/bank",
        "createAccount",
        {
            "customerID" : "",
        },
        request
    )
