import configparser

config=configparser.RawConfigParser()
import os
from pathlib import Path
os.chdir("..")
read_file = os.getcwd()
config_path = str(read_file)+"/Configurations/config.ini"
print(config_path)

config.read(config_path)
#config.read("/home/collegedekho/p.collegedekho/CTA 2/Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getHomepageURL():
        homepage_url=config.get('common info','HomePageUrl')
        
        return homepage_url
    
    @staticmethod
    def getNewslistingUrl():
        NewslistingUrl=config.get('common info','NewslistUrl')
    
        return NewslistingUrl

    # def getHomepageXpath():
    #     homepage_xpath = config.get('HomePageXpath','Talk-to-experts')
    #     homepage_xpath = config.get('HomePageXpath','Footer-Form')
        
    #     return homepage_xpath


        
    @staticmethod
    def getExamDetailURL():
        ExamDetail_Url=config.get('common info','ExmDtlUrl')
    
        return ExamDetail_Url

    @staticmethod
    def getEXamListingURL():
        ExamLstng_Url=config.get('common info','ExmLstngUrl')
    
        return ExamLstng_Url
    
    @staticmethod
    def getCareerDtlURL():
        CareerDetail_Url=config.get('common info','Career_Url')
    
        return CareerDetail_Url

    @staticmethod
    def getCollegeDtlURL():
        CollegeDetail_Url=config.get('common info','ColDtl_Url')
    
        return CollegeDetail_Url
    
    @staticmethod
    def getNewsDtlURL():
        NewsDetail_Url=config.get('common info','NewsDtl_Url')
    
        return NewsDetail_Url

    @staticmethod
    def getBoardDtlURL():
        BoardDetail_Url=config.get('common info','BoardDtl_Url')
    
        return BoardDetail_Url

    @staticmethod
    def getCoursedetailURL():
        CoursedetailURL=config.get('common info','CoursedetaillUrl')
    
        return CoursedetailURL

    # @staticmethod
    # def getUseremail():
    #     username=configfile.get('common info','useremail')
    #     return 