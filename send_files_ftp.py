
import os,sys
import shutil
from ftplib import FTP
import traceback
import logging

logging.basicConfig(filename='ftp.log', filemode='a',format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

# Συνάρτηση για αποστολή αρχειων
def send_ftp(ip,remote_folder,user,password,out_dir):
    try:
        out_List = os.listdir(out_dir)
    except Exception as e:
##        print(e,traceback.print_exc())
        print("ERROR:",e)
        logging.error(f"ERROR:{e}")
##        logging.exception(f"check folder {out_dir}")
        sys.exit(f"check folder {out_dir}")
    if len(out_List)==0:
        print( "\n", "There are no files in folder to send  \n" )
        logging.warning('There are no files in folder to send . - Exit')
        sys.exit("There are no files in folder to send .")
        
    with FTP(ip) as ftp:
        ftp.login(user, password)
        ftp.cwd(remote_folder)
        ftp.encoding='iso8859_7'
        ftp_return=[]
        for file in out_List:
            print("file to send:",file)
            ftp.storbinary('STOR ' + file , open(out_dir +'\\'+ file, 'rb'))
##            ftp_return=ftp.nlist()
            ftp.retrlines('NLST',ftp_return.append)
            if file in ftp_return:
                print("The file: ",file,"  has been sent")
                logging.info(f'The file: {file} has been sent.')
            else:
                print("The file: ",file," has not been sent")
                logging.warning(f'The file: {file} has not been sent.')
                
        print('\nRemote folder list=\n',ftp.nlst())

def main():
    import json
    with open("send_files_ftp.cfg") as cfg:
        json_data = json.load(cfg)
        for item in json_data:
            location = item
            ip    = json_data[item]['ip']
            user  = json_data[item]['user']
            passw = json_data[item]['pass']
            send  = json_data[item]['send']
            local_folder  = json_data[item]['local_folder']
            remote_path   = json_data[item]['remote_path']
            if send =="yes":
                print(location,"\t",ip,remote_path,user,passw,send)        
                # sending to all addresses.            
                try:
                    print("\n********************************************************\n")
                    print( "\nSending files to",location," in folder: " ,remote_path )
                    logging.info(f'Sending files to {location} in folder: {remote_path}' )
                    send_ftp(ip,remote_path,user,passw,local_folder)
                except Exception as e:
                    print(e,traceback.print_exc())
                    print( "\n",location, "not reachable\n" )
                    logging.error(f"ERROR:{e}")
##                    logging.exception("Exception occurred in sending with ftp")
                


if __name__ == "__main__":
    main()
