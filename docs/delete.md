You are an excellent resume creator that ensures resumes that you create work with ATS softwares and aim to reach the hands of the employers so they are convinced to interview the candidate as soon as possible. 

scan the existing project and learn how its working. after you scan you can learn below requirements so you are aware how you can refactor it. use existing project as a reference. use what you can use from existing project and remove those that does not belong the this project goal. existing project is already in good shape but we need to be sure below is considered as well in the resume building.


 Now you need to Refactor current project in the workspace with below requirements. Below are the details for each aspect of the how the repo should help create resumes in .md and .pdf files in the locations which the project will guide where it needs to be created.

1. this project is suppose to work with claude code, so claude code gets prompts. so this project should only expect these commands to work with. if it does not match the words exactly how its supposed to expect, it shall stop and does not run further by informing user that expected prompt is not received. and is suggested to the user what the common prompts claude code can do. below are the commands:

    1. Build a resume for user whose details are found in file: profile.yml
    2. Create resume in pdf format from file name: 



2. For the career summary that is created in the resume workflow by claude code, the process should be as i define it below:

    1. contact details of the user are always static and fixed which should only come from profile.yml. this is the source contact details.

    2. user will mention bunch of careerSummary files within /Users/anildhage/Downloads/resume-workflow/profiles/anil/careerSummary/ these are his actual summaries that user has. When a new resume is being created for whatever job, when it comes to creating summary, first it should scan this folder, get an undestanding of career summaries and then read the data from jd.md. now a new career summary needs to be created for the resume, so calude code needs to use existing data in /Users/anildhage/Downloads/resume-workflow/profiles/anil/careerSummary/ and then align it to the jd.md because user wants to apply to this role, so career summary should be aligned so employers find it curated. how you do is, use factual information you learn from /Users/anildhage/Downloads/resume-workflow/profiles/anil/ and then keep those but align it to the role from jd.md. always create a career summary with the role position similar to whats in jd.md. if there is not already present in the /Users/anildhage/Downloads/resume-workflow/profiles/anil/careerSummary/ create a new one and save it in this directory and eventuall use it in the target resume you will create. if there is already the position available matching to jd.md in /Users/anildhage/Downloads/resume-workflow/profiles/anil/careerSummary/ then use that as a starting point, make it better based on the job user wants to apply from jd.md then modify and update existing role in /Users/anildhage/Downloads/resume-workflow/profiles/anil/careerSummary/ and use that in target resume you create. 




4. for the skills section in the target resumes you create as per the workflow, folow below process

    scan the jd.md file that user is trying to apply, understand and catch the skills that are required. then access/Users/anildhage/Downloads/resume-workflow/profiles/anil/skills/ folder where should find skills the user has. pick the ones that are relavant and aligning to the job from jd.md. and then based on the alignment to target the jd.md, create best picked skills and add it to the target resume. once you add it. Keep as many skills as you can to ensure we only mention those that are relevant. any skills matching from /Users/anildhage/Downloads/resume-workflow/profiles/anil/skills/ and from jd.md file, they need to be mentioned in bold so employers can focus on it. 



5. For the work experience section, its very important below rules are applied while creating a resume

    1. first job is to scan the /Users/anildhage/Downloads/resume-workflow/profiles/anil/ to learn factual information about anil. after this read the jd.md file that anil wants to apply and expect a resume. 
    2. lets start from present work experience, take his present work experience from /Users/anildhage/Downloads/resume-workflow/profiles/anil/ align his work experience to the jd.md file so bullet points that claude code will create are accurate experience bullet points and aligned it to the role from jd.md. goal is to provide 5-6 points. these bullet points should show how anils work experience overall you learnt from /Users/anildhage/Downloads/resume-workflow/profiles/anil/ is going to align with jd.md and create 5-6 bullet points. 
    3. highlight words or verbs with subject in the bullet points that are relavant to the jd.md role and those that are matching to the position anil wants to apply from jd.md
    
6. for the other job roles from /Users/anildhage/Downloads/resume-workflow/profiles/anil/ had before the current work experience follow below rules
    1. use data from /Users/anildhage/Downloads/resume-workflow/profiles/anil/ 
    2. copy as it is to target resume
    3. dont edit or make them in bold or highlight.

7. education and certifications sections are also fixed and these should not be changed and should always stay as it is in the file resumeSkeleton.md

8. for projects section, you need to decide which best projects you can pick up from /Users/anildhage/Downloads/resume-workflow/profiles/anil/projects/ and make it aligned to the role user wants to apply for the role which is inside jd.md 

8. resumeSkeleton.md is the target skeleton to how the resume is created on top of. 
    1. where ever there is information you keep it as it is and use it in the target resumes you create, but whereever there is - to be updated mentioned, you folow the above rules mentioned for that specific section to how you should apply the edits. 







