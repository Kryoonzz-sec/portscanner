"""
PORT SCANNER CRIADO POR: KRYOONZZ
"""

import socket, sys, threading

# Função para realizar o scan de uma porta específica em um IP
def portscan(ip, porta):
    # Cria um socket TCP/IP
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Define um tempo limite de 0.5 segundos para a conexão
    meusocket.settimeout(0.5)
    
    # Tenta estabelecer uma conexão com o IP e porta especificados
    if meusocket.connect_ex((ip, porta)) == 0:
        # Se a conexão for bem-sucedida, imprime que a porta está aberta
        print("Porta: " + str(porta) + "[ABERTA]")
    
    # Fecha o socket
    meusocket.close()

# Função principal do programa
def main():
    # Verifica se foi fornecido um IP como argumento na linha de comando
    if len(sys.argv) > 1:
        # Obtém o IP a ser escaneado a partir do argumento
        ip = sys.argv[1]
        # Imprime o IP que está sendo escaneado
        print("Varrendo o host: " + ip)
        # Imprime que o scan está sendo iniciado
        print("Iniciando o scan.")
        
        # Cria uma lista para armazenar as threads
        threads = []
        
        # Loop para escanear todas as portas de 1 a 65535
        for porta in range(1, 65536):
            # Cria uma nova thread para escanear a porta atual
            t = threading.Thread(target=portscan, args=(ip, porta))
            # Adiciona a thread à lista de threads
            threads.append(t)
            # Inicia a thread
            t.start()
        
        # Aguarda todas as threads terminarem
        for t in threads:
            t.join()
    else:
        # Se nenhum IP for fornecido, imprime uma mensagem de erro
        print("Informe o IP para scan.")

# Verifica se o programa está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Chama a função principal
    main()