import qrcode

upi_id=input("Enter your UPT ID:")

phonepe_url = f'upi://pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlrpay_url = f'upi://pa={upi_id}&pn=Recipient%20Name&mc=1234'


phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
googlrpay_qr=qrcode.make(googlrpay_url)

paytm_qr.save('paytm_qr.png')
phonepe_qr.save('phonrpe_qr.png')
googlrpay_qr.save('googlrpay_qr.png')

phonepe_qr.show()
paytm_qr.show()
googlrpay_qr.show()