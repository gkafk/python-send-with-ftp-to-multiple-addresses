Python file: send_files_ftp.py 
  uses send_files_ftp.cfg  json configuration file to send files via ftp protocol to remote users.

Json file: send_files_ftp.cfg
 It has the configuration for remote users.   


 "one":{
		"ip"			: "10.10.2.2",               # remote IP address
		"remote_path"	: "/users/x/Desktop",    # remote directory
		"user"			: "user",                  # remote user name
		"pass"			: "pass",                  # remote user password
		"local_folder"	: "output",            # local folder with files to be send
		"send"  		: "yes"                    # "yes" to send files to this user, "no" to continue with next user
	},
