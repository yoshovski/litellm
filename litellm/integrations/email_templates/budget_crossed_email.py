"""
Modern Email Template for LiteLLM Budget Crossed
"""

BUDGET_CROSSED_EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Budget Limit Reached</title>
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            color: #333333;
            background-color: #f8fafc;
            line-height: 1.5;
        }}
        .container {{
            max-width: 560px;
            margin: 20px auto;
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .header {{
            padding: 24px 0;
            text-align: center;
            border-bottom: 1px solid #f1f5f9;
        }}
        .content {{
            padding: 32px 40px;
        }}
        .greeting {{
            font-size: 16px;
            margin-bottom: 20px;
            color: #333333;
        }}
        .message {{
            font-size: 16px;
            color: #333333;
            margin-bottom: 20px;
        }}
        .budget-info {{
            background-color: #fef2f2;
            border-radius: 6px;
            padding: 16px 20px;
            margin: 24px 0;
            font-size: 15px;
            border: 1px solid #fecaca;
            color: #991b1b;
        }}
        .budget-info p {{
            margin: 8px 0;
        }}
        h2 {{
            font-size: 18px;
            font-weight: 600;
            margin-top: 36px;
            margin-bottom: 16px;
            color: #333333;
        }}
        .btn {{
            display: inline-block;
            padding: 10px 24px;
            background-color: #ef4444;
            color: #ffffff !important;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
            margin-top: 16px;
            text-align: center;
            font-size: 15px;
            transition: background-color 0.2s;
        }}
        .btn:hover {{
            background-color: #dc2626;
            color: #ffffff !important;
        }}
        .separator {{
            height: 1px;
            background-color: #f1f5f9;
            margin: 40px 0 30px;
        }}
        .footer {{
            padding: 24px 40px 32px;
            text-align: center;
            color: #64748b;
            font-size: 13px;
            background-color: #f8fafc;
            border-top: 1px solid #f1f5f9;
        }}
        @media only screen and (max-width: 620px) {{
            .container {{
                width: 100%;
                margin: 0;
                border-radius: 0;
            }}
            .content {{
                padding: 24px 20px;
            }}
            .footer {{
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="{email_logo_url}" alt="{app_name} Logo" style="height: 32px; width: auto;">
        </div>
        <div class="content">
            <div class="greeting">
                <p>Hi {recipient_name},</p>
            </div>
            
            <div class="message">
                <p>Your {team_info}LLM API usage this month has reached the <strong>monthly budget of ${max_budget}</strong>.</p>
            </div>
            
            <div class="budget-info">
                <p><strong>Current Spend:</strong> ${current_spend}</p>
                <p><strong>Budget Limit:</strong> ${max_budget}</p>
                <p style="margin-top: 12px; font-weight: 500; font-size: 14px; color: #b91c1c;">
                    ⚠️ API requests will be rejected until either (a) you increase your monthly budget or (b) your monthly usage resets at the beginning of the next calendar month.
                </p>
            </div>
            
            <a href="{base_url}" class="btn" style="color: #ffffff;">Manage Budget</a>
            
            <div class="separator"></div>
            
            <h2>Need Help?</h2>
            <p>If you have any questions or need to request a budget increase, please contact us at {email_support_contact}.</p>
        </div>
        {email_footer}
    </div>
</body>
</html>
"""
