stockDict = { 'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':"Eastman Kodak", 'GE': 'General Electric' }
purchases = [ ( 'GE', 100, '10-sep-2001', 48 ), ( 'CAT', 100, '1-apr-1999', 24 ), ( 'GE', 200, '1-jul-1998', 56 ) ]


for purchase in purchases:
	ticker = purchase[0]

	full_company_name = stockDict[ticker]
	number_of_shares = purchase[1]
	total_price = purchase[1] * purchase[3]

	print("I purhcased {} shares of {}'s stock for ${}.".format(number_of_shares, full_company_name, total_price))



for ticker in stockDict:
	print("Company Ticker: " + ticker)
	print("----------------")
	for purchase in purchases:
		if purchase[0] is ticker:
			print(purchase[1])