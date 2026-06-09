import os

def create_html_resource():
    output_filename = "wolters_kluwer_university_guide.html"
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wolters Kluwer Health Library Guide</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 0 20px; color: #333; background-color: #fcfcfc; }
        h1 { color: #005a9c; border-bottom: 2px solid #005a9c; padding-bottom: 10px; }
        h2 { color: #0073bc; margin-top: 30px; }
        .section { background: white; padding: 20px; margin-bottom: 20px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); border-left: 4px solid #005a9c; }
        code { background: #f4f4f4; padding: 2px 6px; border-radius: 4px; font-family: monospace; }
        ul { padding-left: 20px; }
        li { margin-bottom: 8px; }
    </style>
</head>
<body>
    <h1>📘 Mastering the Wolters Kluwer Health Library</h1>
    <p><strong>A University Student Guide for Active Recall and Exam Preparation</strong></p>
    <div class="section">
        <h2>🔑 1. How to Authenticate and Log In</h2>
        <ul>
            <li><strong>Proxy Link:</strong> Log in via your university's electronic library single sign-on portal.</li>
            <li><strong>Personal Profile:</strong> Create a personalized login on the portal to track your individual quiz results.</li>
        </ul>
    </div>
    <div class="section">
        <h2>📚 2. Core Digital Features</h2>
        <ul>
            <li><strong>Textbook Portability:</strong> Jump to specific textbook chapters or save sections to clean PDF formats.</li>
            <li><strong>Video Bank:</strong> Utilize the clinical procedures and medical animation videos to visualize complex systems.</li>
        </ul>
    </div>
    <div class="section">
        <h2>🗂️ 3. Anki Flashcard Automation</h2>
        <ul>
            <li><strong>Bulk Decks:</strong> Organize study rows in Excel, save as a <code>.csv</code> file, and click <code>File -> Import</code> inside Anki.</li>
        </ul>
    </div>
</body>
</html>
"""

    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"✅ Generated '{output_filename}' successfully.")

if __name__ == "__main__":
    create_html_resource()
