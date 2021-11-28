import dropbox
class Transferdata(object):
    def __init__(self,token):
        self.token=token


    def uploadfile(self,fromfile,tofile):
        dbx=dropbox.Dropbox(self.token)

        f=open(fromfile,'rb')
        #dbx.files_upload(f.read(),tofile)
        


def main():
    token='sl.A9I5q9gEjuWtpkLfz8KTfJLUf_XZhnWpRiUWC48SY5Ss1othc0kIWMAXSrZW7hbHeq9fHC0YJcXrUbZikGRLzkHaXOI1EeOF5gkXUk1Ml0XJLQWzRn-lzV4JXIdvCe6O-Nyq1ak'

    transferdata=Transferdata(token)
    fromfile=input("enter file path  ")

    tofile=input("enter your tofile path  ")

    transferdata.uploadfile(fromfile,tofile)
    print("file uploaded")


main()    


