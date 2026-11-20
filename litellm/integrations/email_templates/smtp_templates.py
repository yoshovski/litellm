"""
Modern Email Templates for LiteLLM Email Service with professional styling
"""

KEY_CREATED_EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your API Key is Ready</title>
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
        .key-container {{
            margin: 28px 0;
        }}
        .key-label {{
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 8px;
            color: #4b5563;
        }}
        .key {{
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            word-break: break-all;
            background-color: #f9fafb;
            border-radius: 6px;
            padding: 16px;
            font-size: 14px;
            border: 1px solid #e5e7eb;
            color: #4338ca;
        }}
        h2 {{
            font-size: 18px;
            font-weight: 600;
            margin-top: 36px;
            margin-bottom: 16px;
            color: #333333;
        }}
        .budget-info {{
            background-color: #f0fdf4;
            border-radius: 6px;
            padding: 14px 16px;
            margin: 24px 0;
            font-size: 14px;
            border: 1px solid #dcfce7;
        }}
        .code-block {{
            background-color: #f8fafc;
            color: #334155;
            border-radius: 8px;
            padding: 20px;
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 13px;
            overflow-x: auto;
            margin: 20px 0;
            line-height: 1.6;
            border: 1px solid #e2e8f0;
        }}
        .code-comment {{
            color: #64748b;
        }}
        .code-string {{
            color: #0369a1;
        }}
        .code-keyword {{
            color: #7e22ce;
        }}
        .btn {{
            display: inline-block;
            padding: 8px 20px;
            background-color: #6366f1;
            color: #ffffff !important;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
            margin-top: 24px;
            text-align: center;
            font-size: 14px;
            transition: background-color 0.2s;
        }}
        .btn:hover {{
            background-color: #4f46e5;
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
        .social-links {{
            margin-top: 12px;
        }}
        .social-links a {{
            display: inline-block;
            margin: 0 8px;
            color: #64748b;
            text-decoration: none;
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
                <p>Hi {user_name},</p>
            </div>

            <div class="message">
                <p>Great news! Your API key is ready to use.</p>
            </div>

            {budget_info_html}

            {key_display_html}

            <a href="https://docs.litellm.ai/docs/proxy/user_keys" class="btn" style="color: #ffffff;">View Documentation</a>

            <div class="separator"></div>

            <h2>Need Help?</h2>
            <p>If you have any questions or need assistance, please contact us at {email_support_contact}.</p>
        </div>
        {email_footer}
    </div>
</body>
</html>
"""

"""
Modern Email Templates for LiteLLM Email Service with professional styling
"""

KEY_ROTATED_EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your API Key Has Been Rotated</title>
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
        .key-container {{
            margin: 28px 0;
        }}
        .key-label {{
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 8px;
            color: #4b5563;
        }}
        .key {{
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            word-break: break-all;
            background-color: #f9fafb;
            border-radius: 6px;
            padding: 16px;
            font-size: 14px;
            border: 1px solid #e5e7eb;
            color: #4338ca;
        }}
        h2 {{
            font-size: 18px;
            font-weight: 600;
            margin-top: 36px;
            margin-bottom: 16px;
            color: #333333;
        }}
        .budget-info {{
            background-color: #f0fdf4;
            border-radius: 6px;
            padding: 14px 16px;
            margin: 24px 0;
            font-size: 14px;
            border: 1px solid #dcfce7;
        }}
        .code-block {{
            background-color: #f8fafc;
            color: #334155;
            border-radius: 8px;
            padding: 20px;
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 13px;
            overflow-x: auto;
            margin: 20px 0;
            line-height: 1.6;
            border: 1px solid #e2e8f0;
        }}
        .code-comment {{
            color: #64748b;
        }}
        .code-string {{
            color: #0369a1;
        }}
        .code-keyword {{
            color: #7e22ce;
        }}
        .btn {{
            display: inline-block;
            padding: 8px 20px;
            background-color: #6366f1;
            color: #ffffff !important;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
            margin-top: 24px;
            text-align: center;
            font-size: 14px;
            transition: background-color 0.2s;
        }}
        .btn:hover {{
            background-color: #4f46e5;
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
        .social-links {{
            margin-top: 12px;
        }}
        .social-links a {{
            display: inline-block;
            margin: 0 8px;
            color: #64748b;
            text-decoration: none;
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
                <p>Hi {user_name},</p>
            </div>

            <div class="message">
                <p><strong>Your API key has been rotated</strong> as part of our ongoing commitment to security best practices.</p>
                <p style="margin-top: 16px;">Your previous API key has been deactivated and will no longer work. Please update your applications with the new key below.</p>
            </div>

            {budget_info_html}

            {key_display_html}

            <div class="separator"></div>

            <h2>Security Best Practices</h2>
            <p style="margin-bottom: 12px;">To keep your API key secure:</p>
            <ul style="margin: 0; padding-left: 20px; color: #333333;">
                <li style="margin-bottom: 8px;">Never share your API key publicly or commit it to version control</li>
                <li style="margin-bottom: 8px;">Store it securely using environment variables or secret management systems</li>
                <li style="margin-bottom: 8px;">Monitor your API usage regularly for any unusual activity</li>
                <li style="margin-bottom: 8px;">Rotate your keys periodically as a security best practice</li>
            </ul>

            <a href="https://docs.litellm.ai/docs/proxy/user_keys" class="btn" style="color: #ffffff;">View Documentation</a>

            <div class="separator"></div>

            <h2>Need Help?</h2>
            <p>If you have any questions or need assistance updating your systems, please contact us at {email_support_contact}.</p>
        </div>
        {email_footer}
    </div>
</body>
</html>
"""

"""
Modern Email Templates for LiteLLM Email Service with professional styling
"""

USER_INVITATION_EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to LiteLLM</title>
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            color: #333333;
            background-color: #f8f8f8;
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
        .logo {{
            padding: 24px 0 0 24px;
            text-align: left;
        }}
        .greeting {{
            font-size: 16px;
            margin-bottom: 20px;
            color: #333333;
        }}
        .content {{
            padding: 24px 40px 32px;
        }}
        h1 {{
            font-size: 24px;
            font-weight: 600;
            margin-top: 24px;
            margin-bottom: 16px;
            color: #333333;
        }}
        p {{
            font-size: 16px;
            color: #333333;
            margin-bottom: 16px;
            line-height: 1.5;
        }}
        .intro-text {{
            margin-bottom: 24px;
        }}
        .link {{
            color: #6366f1;
            text-decoration: none;
            font-weight: 500;
        }}
        .link:hover {{
            text-decoration: underline;
        }}
        .link-with-arrow {{
            display: inline-flex;
            align-items: center;
            color: #6366f1;
            text-decoration: none;
            font-weight: 500;
            margin-bottom: 20px;
        }}
        .link-with-arrow:hover {{
            text-decoration: underline;
        }}
        .arrow {{
            margin-left: 6px;
        }}
        .divider {{
            height: 1px;
            background-color: #f1f1f1;
            margin: 24px 0;
        }}
        .btn {{
            display: inline-block;
            padding: 12px 24px;
            background-color: #5c5ce0;
            color: #ffffff !important;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
            margin-top: 12px;
            text-align: center;
            font-size: 15px;
            transition: background-color 0.2s ease;
        }}
        .btn:hover {{
            background-color: #4b4bb3;
        }}
        .btn-container {{
            text-align: center;
            margin: 24px 0;
        }}
        .footer {{
            padding: 24px 40px 32px;
            text-align: left;
            color: #666;
            font-size: 14px;
        }}
        .quickstart {{
            margin-top: 32px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <img src="{email_logo_url}" alt="{app_name} Logo" style="max-height: 32px; max-width: 150px; object-fit: contain;">
        </div>
        <div class="content">
            <h1>Welcome to {app_name}</h1>

            <div class="greeting">
                <p>Hi there,</p>
            </div>

            <div class="intro-text">
                <p>{app_name} allows you to call 100+ LLM providers in the OpenAI API format. Get started by accepting your invitation.</p>
            </div>

            <div class="btn-container">
                <a href="{base_url}" class="btn">Accept Invitation</a>
            </div>

            <div class="quickstart">
                <p>Here's a quickstart guide to get you started:</p>
            </div>

            <div class="divider"></div>

            <a href="https://docs.litellm.ai/docs/proxy/user_keys" class="link-with-arrow">
                Make your first LLM request →
                <span class="arrow"></span>
            </a>

            <p>Making LLM requests with OpenAI SDK, Langchain, LlamaIndex, and more.</p>

            <div class="divider"></div>

            <a href="https://docs.litellm.ai/docs/supported_endpoints" class="link-with-arrow">
                Supported Endpoints →
                <span class="arrow"></span>
            </a>

            <p>View all supported LLM endpoints on {app_name} (/chat/completions, /embeddings, /responses etc.)</p>

            <div class="divider"></div>

            <a href="https://docs.litellm.ai/docs/pass_through/vertex_ai" class="link-with-arrow">
                Passthrough Endpoints →
                <span class="arrow"></span>
            </a>

            <p>We support calling VertexAI, Anthropic, and other providers in their native API format.</p>

            <div class="divider"></div>

            <p>Thanks for signing up. We're here to help you and your team. If you have any questions, contact us at {email_support_contact}</p>

        </div>
        {email_footer}
    </div>
</body>
</html>
"""

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

"""
Modern Email Template for LiteLLM Soft Budget Crossed
"""

SOFT_BUDGET_CROSSED_EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soft Budget Limit Reached</title>
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
            background-color: #fffbeb;
            border-radius: 6px;
            padding: 16px 20px;
            margin: 24px 0;
            font-size: 15px;
            border: 1px solid #fde68a;
            color: #92400e;
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
            background-color: #f59e0b;
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
            background-color: #d97706;
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
                <p>Your {team_info}LLM API usage this month has reached the <strong>soft monthly budget of ${soft_budget}</strong>.</p>
            </div>

            <div class="budget-info">
                <p><strong>Current Spend:</strong> ${current_spend}</p>
                <p><strong>Soft Budget Limit:</strong> ${soft_budget}</p>
                {max_budget_info}
                <p style="margin-top: 12px; font-weight: 500; font-size: 14px; color: #b45309;">
                    ⚠️ Note: Your API requests will continue to work, but you should monitor your usage closely. If you reach your maximum budget, requests will be rejected.
                </p>
            </div>

            <a href="{base_url}" class="btn" style="color: #ffffff;">View Dashboard</a>

            <div class="separator"></div>

            <h2>Need Help?</h2>
            <p>If you have any questions or need to request a budget increase, please contact us at {email_support_contact}.</p>
        </div>
        {email_footer}
    </div>
</body>
</html>
"""
