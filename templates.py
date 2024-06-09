subject = 'Application for {position} at your company'

body_template =  """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cover Letter</title>
<style>
  body {{
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: #f2f2f2;
  }}
  .container {{
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
  }}
  .header {{
    text-align: center;
    margin-bottom: 20px;
  }}
  .header h1 {{
    color: #333;
    margin: 0;
  }}
  .content {{
    margin-bottom: 20px;
  }}
  .content p {{
    margin: 10px 0;
  }}
  .footer {{}
    text-align: center;
  }}
  .footer p {{
    color: #666;
    margin: 10px 0;
  }}
</style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>Cover Letter</h1>
    </div>
    <div class="content">
      <p>Dear Recruiter,</p>
      <p>I am writing to express my enthusiastic interest in the {position} at your company. With a strong foundation in {field}, a keen desire to learn, and a deep admiration for the innovative work being done at your company, I am eager to contribute to your team and further develop my skills in this exciting field.</p>
      <p>Currently, I am pursuing a B.Tech in Computer Science from Gurukula Kangri (Deemed to be University), where I have maintained a GPA of {gpa} and have been actively involved in the Google Developers Student Club. My academic background, combined with my hands-on project experience, has equipped me with a solid understanding of {field} principles and techniques.</p>
      <p>{project_descriptions}</p>
      <p>I am confident that my technical skills, coupled with my enthusiasm for learning and passion for {field}, make me a strong candidate for this position. I am eager to bring my background in {field} and my proactive, collaborative approach to your team.</p>
      <p>Thank you for considering my application. I look forward to the possibility of discussing how I can contribute to the innovative work at your company. Please find my resume attached for your review. I am available for an interview at your earliest convenience and can be reached at <a href="tel:{phone_number}">{phone_number}</a> or via email at <a href="mailto:{email_id}">{email_id}</a>.</p>
    </div>
    <div class="footer">
      <p>Sincerely,<br>{your_name}</p>
    </div>
  </div>
</body>
</html>

"""