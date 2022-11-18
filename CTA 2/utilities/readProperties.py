import configparser

config=configparser.RawConfigParser()
config.read("/home/collegedekho/p.collegedekho/CTA 2/Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getHomepageURL():
        homepage_url=config.get('common info','HomePageUrl')
        
        return homepage_url

    # def getHomepageXpath():
    #     homepage_xpath = config.get('HomePageXpath','Talk-to-experts')
    #     homepage_xpath = config.get('HomePageXpath','Footer-Form')
        
    #     return homepage_xpath


        
    @staticmethod
    def getExamURL():
        ExamDetail_Url=config.get('common info','ExmDtlUrl')
    
        return ExamDetail_Url

    # @staticmethod
    # def getUseremail():
    #     username=configfile.get('common info','useremail')
    #     return 