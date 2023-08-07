"""
PORT SCANNER CRIADO POR: KRYOONZZ
"""

import socket,sys,threading

def portscan(ip, porta):
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meusocket.settimeout(0.5)
    if meusocket.connect_ex((ip, porta)) == 0:
        print("Porta: " + str(porta) + "[ABERTA]")
    meusocket.close()

def main():
    if len(sys.argv) > 1:
        ip = sys.argv[1]
        print("Varrendo o host: " + ip)
        print("Iniciando o scan.")
        threads = []
        for porta in range(1, 65536):
            t = threading.Thread(target=portscan, args=(ip, porta))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    else:
        print("Informe o IP para scan.")

if __name__ == "__main__":
    main()