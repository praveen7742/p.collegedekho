import configparser

config=configparser.RawConfigParser()
config.read("/home/collegedekho/p.collegedekho/CTA 2/Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getHomepageURL():
        desktop_url=config.get('common info','HomePageUrl')

        return desktop_url
        
    @staticmethod
    def getExamURL():
        ExamDetail_Url=config.get('common info','ExmDtlUrl')
    
        return ExamDetail_Url

    # @staticmethod
    # def getUseremail():
    #     username=configfile.get('common info','useremail')
    #     return 