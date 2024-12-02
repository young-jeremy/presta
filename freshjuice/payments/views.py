import json
from django.shortcuts import render
from django.conf import settings
from datetime import datetime
import requests
from base64 import b64encode

from django.http import JsonResponse
from django.shortcuts import render


def payment_view(request):
    if request.method == "POST":
        access_token = get_access_token()
        if access_token is None:
            return JsonResponse({"error": "Failed to obtain access token"}, status=500)

        # Proceed with payment initiation logic...
        payment_url = f"{settings.MPESA_BASE_URL}/path/to/your/payment/endpoint"  # Replace with the correct endpoint
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        # Construct your payment request body here
        payload = {
            # Add your payment request parameters here
        }

        payment_response = requests.post(payment_url, json=payload, headers=headers)

        # Check the payment response
        print("Payment Response Status Code:", payment_response.status_code)
        print("Payment Response Content:", payment_response.json())

        if payment_response.status_code == 200:
            return JsonResponse({"message": "Payment initiated successfully"})
        else:
            return JsonResponse({"error": "Failed to initiate payment", "details": payment_response.json()},
                                status=payment_response.status_code)

    return render(request, 'payments/payment_form.html')  # Adjust the template name accordingly


def make_payment(amount, phone_number):
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json"
    }

    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": settings.MPESA_PASSKEY,
        "Timestamp": generate_timestamp(),
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallbackURL": settings.CALLBACK_URL,
        "TransactionType": "CustomerPayBillOnline"
    }

    response = requests.post(f"{settings.MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest", json=payload,
                             headers=headers)

    return response.json()


def get_access_token():
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    consumer_key = "43x4pUkMeFMcsVAvCcn8ajuLbqGdtMd8wbWRXp5dQG1H7FpH"  # Replace with your Consumer Key
    consumer_secret = "iZ7vIHjn6WRnYNQJgCG1S9GbU85WoJqXQQng4GTJcFgr867d83y3Ax3SyemKHICU"  # Replace with your Consumer Secret
    key_secret = f"{consumer_key}:{consumer_secret}"

    headers = {
        "Authorization": "Basic " + b64encode(key_secret.encode()).decode()
    }

    response = requests.get(api_url, headers=headers)

    # Debugging output
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)  # Print the raw response text

    if response.status_code == 200:
        try:
            json_response = response.json()
            return json_response["access_token"]
        except ValueError as e:
            print("Error decoding JSON:", e)
            return None
    else:
        print(f"Error: {response.status_code}, Response: {response.text}")
        return None


def generate_timestamp():
    # Format the timestamp as YYYYMMDDHHmmss
    now = datetime.now()
    return now.strftime('%Y%m%d%H%M%S')
