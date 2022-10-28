import configparser

config=configparser.RawConfigParser()
config.read("/home/collegedekho/p.collegedekho/CTA 2/Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    # @staticmethod
    # def getUseremail():
    #     username=configfile.get('common info','useremail')
    #     return 