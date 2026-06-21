from html import escape


class HTMLGenerator:
    """
    Generates a static HTML webpage from healthcare technology updates.
    """

    def __init__(self, output_file="index.html"):
        self.output_file = output_file

    def generate_page(self, updates):
        """
        Generate the index.html page using the list of technology updates.
        """
        cards_html = ""

        for update in updates:
            employee_name = escape(update.employee_name)
            department = escape(update.department)
            category = escape(update.category)
            news_title = escape(update.news_title)
            summary = escape(update.summary)
            why_it_matters = escape(update.why_it_matters)
            source_link = escape(update.source_link)
            status = escape(update.status)

            status_class = status.lower().replace(" ", "-")

            cards_html += f"""
            <section class="update-card">
                <div class="card-top">
                    <span class="category-badge">{category}</span>
                    <span class="status-badge {status_class}">{status}</span>
                </div>

                <h2>{news_title}</h2>

                <p class="meta">
                    Submitted by <strong>{employee_name}</strong> · {department}
                </p>

                <div class="section-block">
                    <h3>Summary</h3>
                    <p>{summary}</p>
                </div>

                <div class="section-block why">
                    <h3>Why It Matters</h3>
                    <p>{why_it_matters}</p>
                </div>

                <a class="source-button" href="{source_link}" target="_blank">
                    View Source
                </a>
            </section>
            """

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Healthcare Technology Watch CMS</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    
    <style>
        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: linear-gradient(135deg, #e8f7f5, #f4fbff);
            color: #1f2933;
        }}

        header {{
            background: linear-gradient(135deg, #063b4c, #0f766e);
            color: white;
            padding: 40px 20px;
            text-align: center;
        }}

        header h1 {{
            margin: 0;
            font-size: 42px;
        }}

        header p {{
            max-width: 850px;
            margin: 16px auto 0;
            font-size: 18px;
            line-height: 1.6;
        }}
        
        .workflow {{
            display: flex;
            justify-content: center;
            gap: 14px;
            flex-wrap: wrap;
            margin-top: 24px;
        }}

        .workflow span {{
            background: rgba(255, 255, 255, 0.16);
            border: 1px solid rgba(255, 255, 255, 0.35);
            padding: 10px 16px;
            border-radius: 999px;
            font-weight: bold;
            backdrop-filter: blur(6px);
        }}

        .dashboard-summary {{
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            padding: 25px;
            background: white;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        }}

        .summary-box {{
            min-width: 180px;
            padding: 18px;
            border-radius: 14px;
            background: #f0fdfa;
            border: 1px solid #99f6e4;
            text-align: center;
        }}

        .summary-box strong {{
            display: block;
            font-size: 28px;
            color: #0f766e;
        }}

        main {{
            width: 90%;
            max-width: 1100px;
            margin: 35px auto;
        }}

        .update-card {{
            background: white;
            border-radius: 18px;
            padding: 28px;
            margin-bottom: 25px;
            box-shadow: 0 8px 22px rgba(15, 118, 110, 0.15);
            border-left: 8px solid #0f766e;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        
        .update-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 14px 28px rgba(15, 118, 110, 0.22);
        }}

        .card-top {{
            display: flex;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 12px;
        }}

        .category-badge {{
            background: #ccfbf1;
            color: #115e59;
            padding: 8px 12px;
            border-radius: 999px;
            font-weight: bold;
            font-size: 14px;
        }}

        .status-badge {{
            padding: 8px 12px;
            border-radius: 999px;
            font-weight: bold;
            font-size: 14px;
            background: #e5e7eb;
            color: #374151;
        }}

        .pending-review {{
            background: #fef3c7;
            color: #92400e;
        }}

        .approved {{
            background: #dcfce7;
            color: #166534;
        }}

        .featured {{
            background: #dbeafe;
            color: #1e40af;
        }}

        .rejected {{
            background: #fee2e2;
            color: #991b1b;
        }}

        h2 {{
            color: #063b4c;
            margin-bottom: 8px;
        }}

        .meta {{
            color: #52616b;
            font-size: 15px;
            margin-bottom: 20px;
        }}

        .section-block {{
            margin-top: 18px;
        }}

        .section-block h3 {{
            color: #0f766e;
            margin-bottom: 6px;
        }}

        .section-block p {{
            line-height: 1.6;
        }}

        .why {{
            background: #f8fafc;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
        }}

        .source-button {{
            display: inline-block;
            margin-top: 18px;
            padding: 12px 18px;
            background: #0f766e;
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
        }}

        .source-button:hover {{
            background: #115e59;
        }}

        footer {{
            text-align: center;
            padding: 25px;
            color: #52616b;
        }}
    </style>
</head>

<body>
    <header>
        <h1>🏥 Healthcare Technology Watch</h1>
        <p>
            An internal platform for collecting, reviewing,
            and sharing important healthcare technology updates submitted by employees.
        </p>
    <div class="workflow">
        <span>📝 Submit</span>
        <span>🔎 Review</span>
        <span>✅ Approve</span>
        <span>🌐 Share</span>
    </div>
    </header>

    <section class="dashboard-summary">
        <div class="summary-box">
            <strong>{len(updates)}</strong>
            Total Updates
        </div>
        <div class="summary-box">
            <strong>Saved Updates</strong>
            Stored Records
        </div>
        <div class="summary-box">
            <strong>Review</strong>
            Approve & Share
        </div>
    </section>

    <main>
        {cards_html}
    </main>

    <footer>
        Healthcare Technology Watch · Internal Innovation Review Dashboard
    </footer>
</body>
</html>
"""

        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write(html_content)