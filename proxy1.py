'''
    Disclaimer
    tiny httpd is a web server program for instructional purposes only
    It is not intended to be used as a production quality web server
    as it does not fully in compliance with the 
    HTTP RFC https://tools.ietf.org/html/rfc2616

'''
import os
import mimetypes
import sys
import subprocess
import socket
import threading
class HTTPServer:
       def __init__(self,ip,port):
           sock=socket.socket()
           sock.bind((ip,port))
           sock.listen()
           while True:
            conn, clt_addr=sock.accept()
            msg=""
            recvd=conn.recv(10000).decode()
            slicee=recvd[5:]
            res=slicee.index(' ')
            result=slicee[:res]
            print(clt_addr)
            if result == None or res == 0: 
                msg+=("<a href="+"ComputerSystems-p3"+">"+"ComputerSystems-p3"+"</a><br><br>")
                headers=("HTTP/1.1 200 \nContent-Type :text/html\nContent-Length :1000\n\n")
                msg = msg.encode()
            
            elif result=="ComputerSystems-p3":
                for filename in os.listdir("D:\MSIT Projects\ComputerSystems-p3"):
                    f = os.path.join('ComputerSystems-p3', filename)
                    typ1=(mimetypes.MimeTypes().guess_type(str(filename))[0])
                    msg+=("<a href="+str(filename)+">"+str(filename)+"</a><br><br>")
                headers=("HTTP/1.1 200 \nContent-Type :text/html\nContent-Length :1000\n\n")
                msg = msg.encode()  

                    
            elif result == "bin":
                for filename in os.listdir('bin'):
                    f = os.path.join('bin', filename)
                    typ1=(mimetypes.MimeTypes().guess_type(str(filename))[0])
                    if os.path.isfile(f):
                        msg+=("<a href="+str(filename)+">"+str(filename)+"</a><br><br>")
                headers=("HTTP/1.1 200 \nContent-Type :text/html\nContent-Length :1000\n\n")
                msg = msg.encode()  
                
            elif result=="www":
                for filename in os.listdir('www'):
                    f = os.path.join('www', filename)
                    typ1=(mimetypes.MimeTypes().guess_type(str(filename))[0])
                    if os.path.isfile(f):
                        msg+=("<a href="+str(filename)+">"+str(filename)+"</a><br><br>")
                    headers=("HTTP/1.1 200 OK\nContent-Type :"+str(typ1)+"\nContent-Length :1000\n\n")
                msg = msg.encode() 
                
            elif result=='ls' or result=='du':
                msg=os.popen("dir").read().encode()
                headers=("HTTP/1.1 200 \nContent-Type :text/html\nContent-Length :1000\n\n")
            
            else:
                if result in os.listdir('bin'):
                    typ1=(mimetypes.MimeTypes().guess_type(str(result))[0])
                    f = os.path.join('bin', result)
                    print_msg= subprocess.run([sys.executable, "-c", open(str(f)).read()], capture_output=True, text=True)
                    msg=print_msg.stdout.encode()
                    headers=("HTTP/1.1 200 \nContent-Type :"+str(typ1)+"\nContent-Length :"+str(len(msg))+"\n\n")
                elif result in os.listdir('www'):
                    typ1=(mimetypes.MimeTypes().guess_type(str(result))[0])
                    f = os.path.join('www', result)
                    msg = open(f, 'rb').read()
                    headers=("HTTP/1.1 200 OK\nContent-Type :"+str(typ1)+"\nContent-Length :"+str(len(msg))+"\n\n")
                else:
                    msg="<h1> 404 PAGE NOT FOUND </h1>".encode()
                    headers=("HTTP/1.1 404 \nContent-Type :text/html\nContent-Length :"+str(len(msg))+"\n\n")
                
            conn.sendall(headers.encode()+msg)

def main():
    # test harness checks for your web server on the localhost and on port 8888
    # do not change the host and port
    # you can change  the HTTPServer object if you are not following OOP
    # HTTPServer('127.0.0.1', 9999)
    p2 = threading.Thread()(target=HTTPServer,args=('127.0.0.1', 9999))
    p2.start()
    p2.join()

if __name__ == "__main__":
    main()
    p1 = threading.Thread()(target=main())
    p1.start()
    p1.join()

    