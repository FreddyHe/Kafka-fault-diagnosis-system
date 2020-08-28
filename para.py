import paramiko
import time

def transfer_log(config):
    try:
        client=paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy() )
        client.connect(config['IP'], config['port'], config['username'], config['password'], timeout=10)
        sftp_client=client.open_sftp()
        pos= 0
        while True:
            log_content=sftp_client.open(config['server-log'], 'r')
            if pos!=0:
                log_content.seek(pos, 0)
            while True:
                line=log_content.readline()
                if line.strip():
                    print(line.strip() )
                pos+=len(line)
                if not line.strip():
                    break
        time.sleep((config['interval']))
    except Exception as e:
        print('Failed to get logs due to',e)
    finally:
        client.close()

if __name__ == '__main__':
    a = {'port':22, 'interval':5} 
    a['IP']=input('请输入诊断服务器的IP地址:')
    a['username']=input('请输入诊断服务器用户名:')
    a['password']=input('请输入诊断服务器密码:')
    a['server-log']=input('请输入待诊断日志路径:')
    transfer_log(a)