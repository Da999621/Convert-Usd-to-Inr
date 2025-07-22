# convert usd in inr

import requests

def convert_usd_to_inr(amount_usd):
    # API endpoint to fetch current exchange rate
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"

    # Fetch exchange rate data
    response = requests.get(api_url)
    data = response.json()

    # Get the current exchange rate for INR
    exchange_rate = data["rates"]["INR"]

    # Convert USD to INR
    amount_inr = amount_usd * exchange_rate

    return amount_inr

# Example usage
amount_usd = 1000
amount_inr = convert_usd_to_inr(amount_usd)
print(f"{amount_usd} USD is equal to {amount_inr:.2f} INR")


