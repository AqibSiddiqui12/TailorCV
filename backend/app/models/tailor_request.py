class TailorRequest:
    APP_NAME="TailrCV"
    API_VERSION="v1"
    SUPPORTED_LANGUAGES=["en","de"]
    
    def __init__(self,master_resume,job_description,language,cv_type):
        self.master_resume=master_resume
        self.job_description=job_description
        self.language=language
        self.cv_type=cv_type
    @classmethod
    def from_dict(cls,data):
            return cls(
            master_resume=  data["master_resume"],
            job_description=  data["job_description"],
            language=  data["language"],
            cv_type= data["cv_type"]
            )
    def summary(self):
        return f"Language {self.language} ,CV Type : {self.cv_type}"
    def resume_length(self):
        return len(self.master_resume)
    def job_description_length(self):
        return len(self.job_description)
    @staticmethod
    def is_supported_language(language):
        return language in TailorRequest.SUPPORTED_LANGUAGES

payload = { "master_resume" : "... ",  "job_description" : "..." ,    "language": "en",  "cv_type" : "Tech"  }   
info= TailorRequest.from_dict(payload)

# print(TailorRequest.APP_NAME)
# print(TailorRequest.API_VERSION)
# print(TailorRequest.is_supported_language("en"))

# print(info.summary())
# print(info.resume_length())
# print(info.job_description_length())


# request = TailorRequest(master_resume="...",job_description="...",language="en",cv_type="Tech")

