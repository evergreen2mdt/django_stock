from django.shortcuts import render


def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=sk_11d376d6cb4145fea79db14da086fa2d")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api': api})
		
	else:
		return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol"})

	






def about(request):
	return render(request, 'about.html', {})