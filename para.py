import paramiko
import time

def get_raw_log(config):
    try:
        client=paramiko.SSHClient()
        #private_key = paramiko.RSAKey.from_private_key_file('/home/xinyu/VSCode/python/kafka/rsa/my_key')
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy() )
        client.connect(config['IP'], config['port'], config['username'], config['password'], timeout=10)        #pkey=private_key,

stdin, stdout, stderr = client.exec_command('df -h ')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
 print(stdout.read().decode('utf-8'))
 client.close()

        
        sftp_client=client.open_sftp()
        pos= 0
        while True:
            remote_file=sftp_client.open(config['server-log'], 'r')
            if pos!=0:
                remote_file.seek(pos, 0)
            while True:
                line=remote_file.readline()
                if line.strip():
                    print(line.strip() )
                    res=analysis_raw_log(line.strip() )
                    if res is not None:
                        disp_log_diagnosis(res)
                pos+=len(line)
                if not line.strip():
                    break
        time.sleep((config['interval']))
    except KeyboardInterrupt:
        print('stop manually.')
    #except Exception as e:
        #print(e, '，fail to get raw log.')
    finally:
        client.close()


if __name__ == '__main__':
    a = {'IP':' ', 'username':' ', 'password':' ', 'port':22, 'interval':5} 
    #a['IP']=input('userID:')
    #a['port']=input('port:')
    #a['username']=input('username:')
    #a['password']=input('password:')
    #a['server-log']=input('server-log:')
    a['server-log']='~/myfiles/test.txt'
    get_raw_log(a)
