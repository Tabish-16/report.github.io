

#from_string
VOUCHERS = 50


def generateVoucher(count):
  import pdfkit
  html = '''
    <html><head>
    <title>UAQ BT Hub Batch 299</title>
    <style>
body {
  color: #000000;
  background-color: #FFFFFF;
  font-size: 13px;
  font-family:  'Helvetica', arial, sans-serif;
  margin: 0px;
  -webkit-print-color-adjust: exact;
}
table.voucher {
  display: inline-block;
  border: 0px dotted black;
  margin: 2px;
}
@page
{
  size: auto;
}
#num {
  float:right;
  display:inline-block;
}
    </style>
  </head>
  <body >'''
  site_title = "TESTING SITE TITLE"
  login_url = "login.net"
  username = "username-"
  password = "password-"
  for i in range(1,count+1):
    html = html +  f'''<table class="voucher" style=" width: 200px;">
  <tbody>
    <tr>
      <td style="text-align: left; font-size: 14px; font-weight:bold; border-bottom: 1px black solid;"><img src="http://protik.selfip.net:88/protik/uploads/users/6_loginlogo.png?1693233186" alt="logo" style="height:30px;border:0;">UAQ BT Hub<span id="num"> [1]<span id="num"> [299-14966]</span></span></td>
    </tr>
    <tr>
      <td>
    <table style=" text-align: center; width: 190px; font-size: 12px;">
  <tbody>
    <tr>
      <td>
        <table style="width:100%;">
        <tbody><tr>
          <td font-size:="" 12px;="">Voucher Code</td>
        </tr>
        <tr>
          <td style="width:100%; border: 1px solid black; font-weight:bold; font-size:16px;">14966112484</td>
        </tr>
        </tbody></table>
      </td>
    </tr><tr>
      <td colspan="2" style="border-top: 1px solid black;font-weight:bold; font-size:12px">Plan 30-Days-ME | 25 Dh</td>
    </tr>
    <tr><td colspan="2" style="border-top: 1px solid black;font-weight:bold; font-size:12px">Contact: 0</td></tr><tr><td colspan="2" style="border-top: 1px solid black; font-size:10px; text-align:left;"><strong>TERMS AND CONDITIONS:<br></strong>-Please keep voucher until expiry.<br>-New card is to be Purchased if lost.<br>-This card is NON-REFUNDABLE</td></tr><tr><td colspan="2" style="border-top: 1px solid black; font-size:10px">2023-08-16 23:35:55</td></tr>
  </tbody>
    </table>
      </td>
    </tr>
  </tbody>
</table>
    '''
  html = html +'''</body></html>'''
#   pdfkit.from_file("template.html","output_testing.pdf")
  pdfkit.from_string(html, 'output_testing.pdf',options={"orientation":"Portrait"})


generateVoucher(VOUCHERS)