# import geocoder

# def get_current_location():
#     # Get the current location based on IP address
#     g = geocoder.ip('me')

#     if g.ok:
#         return g.address
#     else:
#         return "Location not available"

# # Example usage
# current_location = get_current_location()
# print("Current Location:", current_location)

# a = "scrapbridge-101124153941"
# print(a.capitalize())
# # Example of making a string bold in the terminal
# text = "Nibdahuhuhuhuhh121221"
# bold_text = "\033[1m" + text + "\033[0m"
# print(bold_text)
import html

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            color: #333;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #4CAF50;
            font-size: 24px;
            text-align: center;
        }
        p {
            font-size: 16px;
            line-height: 1.6;
        }
        .order-details {
            background-color: #f1f1f1;
            padding: 15px;
            margin-top: 20px;
            border-radius: 8px;
        }
        .order-details p {
            margin: 5px 0;
        }
        .button {
            display: inline-block;
            background-color: #4CAF50;
            color: #fff;
            padding: 12px 20px;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
            margin-top: 20px;
            font-weight: bold;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            font-size: 12px;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Thanks for choosing ScrapBridge!</h1>
        <p>Hello,</p>
        <p>We appreciate your interest in ScrapBridge. We’ve received your service request and are now processing it. Below are the details of your request:</p>

        <div class="order-details">
            <p><strong>Your reference ID:</strong> {{order_id}}</p>
            <p><strong>Service Requested:</strong> Scrap Collection</p>
            <p><strong>Requested Date:</strong></p>
        </div>

        <p>If you have any questions or need further assistance, feel free to reply to this email.</p>

        <a href="" class="button">Track Your Request</a>

        <div class="footer">
            <p>Thank you for choosing ScrapBridge. We look forward to serving you!</p>
            <p>&copy; 2024 ScrapBridge Inc. | All rights reserved.</p>
        </div>
    </div>
</body>
</html>
"""

# Escape special HTML characters
encoded_text = html_code.encode('utf-8')
decoded_text = encoded_text.decode('utf-8')
print(decoded_text)