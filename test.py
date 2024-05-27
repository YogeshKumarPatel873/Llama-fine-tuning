import easy_llama as ez

Llama3 = ez.Model('Meta-Llama-3-8B-Instruct-q8_0.gguf')
Thread = ez.Thread(Llama3, ez.formats.llama3, ez.samplers.TikTokenSampling)

first_name="Shanu"
job_description="""
Customer Support Specialist / Virtual Assistant
Posted 3 days ago
Worldwide
Job Description:

Giovanni Dienstmann is seeking a dedicated and professional Customer Support Specialist / Virtual Assistant to join his team. The ideal candidate will assist Giovanni in various tasks, primarily focusing on customer support, research, and administrative duties.

Responsibilities:

- Provide excellent customer support by responding to customer inquiries via email in a timely and professional manner.
- Conduct research on various topics as required by Giovanni to support his content creation and business needs.
- Perform data entry tasks accurately and efficiently.
- Assist in managing and updating customer relationship management (CRM) systems.
- Collaborate with the team to ensure smooth operation of daily activities.
- Handle other administrative tasks as assigned by Giovanni.
- Understand the purpose of tasks and think about the best course of action, rather than performing tasks mechanically.

Qualifications:

- Excellent English language skills, both written and verbal.
- Proven experience in customer support or as a virtual assistant.
- Familiarity with CRM systems is necessary; experience with Kartra and Go High Level is desirable but not necessary.
- Customer service experience with memberships, subscriptions, or digital products such as courses and mobile app support is highly desirable.
- Strong research skills and the ability to gather and analyze information.
- High attention to detail and strong organizational skills.
- Ability to work independently and manage time effectively.
- Empathy and a caring attitude towards customers, ensuring their concerns are addressed thoughtfully.
- Proactive attitude and ability to take initiative.

Preferred Skills:

- Experience with WordPress.
- Calendar management.
- Ability to manage multiple tasks and projects simultaneously.
- Strong problem-solving skills and a proactive attitude.

Working Hours:

- Approximately 10 hours per week.

Do not contact Giovanni outside of Upwork.
Any contact attempts will immediately disqualify the candidate.

How to Apply:

If you believe you are the right fit for this role and are excited about the opportunity to work closely with Giovanni Dienstmann, please submit your resume along with a cover letter detailing your relevant experience and why you are interested in this position.



"""

user_prompt_one = f"""
        I am providing you a job description which you have to examine:
        Following is the job Description: '{job_description}'
        client_name='{first_name}'
        ------------------------------------------

        ***Role***:- You are the expert email drafter and I would like you to draft an email 
        proposal for Upwork for the above job description.
        Being as an experienced of 10 years in the given technology in the job description.
        The emails should not be very long and its readability matrix should be as if a 7th grader can read 
        the email. Since the attention span of a client is low so needs to write an impressive email. 

        ***Note***:-Write the email in very simple language and the email should be very enthusiastic,  
        engaging and well-structured. In the entire email client should be placed as a top priority and 
        respectful. The subject of the email should not be fancy or Jazy should be relevant to the project 
        description. Write I instead of we. As we are an organization.

        Start the email by introducing myself as "I am Sanjana, from Hiphype Tech & wanted to speak to you 
        regarding the job posted on Upwork." And then continue with your email

        The proposal should be structured in the following way and must use the 'Upwork' word in subject line without any special characters. 

        Structure of email should be like:

        "
        Subject : It should be related to job_description and should contain the word 'Upwork'.

        Hello/Hi/Dear client_name,

        First Paragraph: write about which technologies should be used(Try to engage the technology with the external world), and any other technical details required for the project to succeed.

        Second Paragraph: Ask 3 questions, that are related to the project description and make the questions engaging and should be in the below format

        Question 1 :
        Question 2 :
        Question 3 :

        Third Paragraph: Write a call to action "If you have any further questions or require additional details, I suggest we schedule a call at 2:00 PM your time, where I can provide you with more insights.".

        at the end of the email add this given signature without any editing from your end:
        "Best regards
        Sanjana Mourya 
        Business Development Manager 
        HipHype Tech
        https://hiphype.co"

    ***Rules***:1. These must be a line break after each paragraph and in salutation you must include recipients name.
            2. Subject line must have heading as "Subject :" before starting subject .
            2.Do not give any other text like "Paragraph","Response" or other text with generated email response
        """

result=Thread.send(user_prompt_one)
print(result)



"""
Well I agree that a 7b model can run on a CPU as long as you have enough RAM, but I would not say it is "fast".
On an Ampere GPU like an A10, A40, A100, you should expect a x10 speedup at least when using text generation
models. But sometimes this speedup is not needed at all and in that case a CPU is definitely enough.
"""