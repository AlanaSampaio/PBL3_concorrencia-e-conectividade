import socket
import threading
import json
import time

# Porta padrão usada para a comunicação UDP.
numIp = 12334

# Intervalo de tempo para enviar pings (em segundos)
PING_INTERVAL = 30

# Classe para implementar um relógio de Lamport.
class LamportClock:
    """Classe para implementar um relógio de Lamport.
    O relógio de Lamport é uma maneira simples de ordenar eventos em um sistema distribuído."""
    def __init__(self):
        # Valor inicial do relógio.
        self.value = 0  
        # Lock para sincronização em ambientes multithread.
        self.lock = threading.Lock()

    def increment(self):
        """Incrementa o valor do relógio e retorna o novo valor."""
        with self.lock:
            self.value += 1
            return self.value

    def update(self, received_time):
        """Atualiza o relógio com base no tempo recebido de outra mensagem."""
        with self.lock:
            self.value = max(self.value, received_time) + 1
            return self.value

# Lista para armazenar as mensagens enviadas
sent_messages = []

# Lista para armazenar as mensagens recebidas
received_messages = []

# Função para ouvir mensagens de outros usuários do chat.
def listen_for_messages(sock, clock, alias, peers, online_peers):
    while True:
        try:
            # Recebe dados de outros usuários.
            data, addr = sock.recvfrom(1024)  
            # Desempacota a mensagem
            message = json.loads(data.decode())  
            # Obtém o tempo da mensagem
            received_time = message['time']  
            # Atualiza o relógio com base no tempo recebido.
            clock.update(received_time)  
            # Adiciona a mensagem à lista de mensagens recebidas
            received_messages.append((message, addr))  
            # Envia um ACK para o remetente
            ack_data = json.dumps({"type": "ACK", "time": clock.value}).encode()
            sock.sendto(ack_data, addr)
        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")

# Função para enviar mensagens para outros usuários.
def send_message(sock, clock, alias, peers):
    while True:
        # Solicita ao usuário uma mensagem para enviar.
        message_text = input("Digite sua mensagem: ")  
        # Verifica se o usuário digitou o comando para sair.
        if message_text.strip() == "/sair":  
            print("Encerrando o programa...")
            # Fecha o socket
            sock.close()  
            # Sai do loop
            break  
        # Incrementa o relógio antes de enviar a mensagem.
        lamport_time = clock.increment()  
        # Prepara os dados da mensagem para envio.
        message_data = {"alias": alias, "text": message_text, "time": lamport_time}
        data = json.dumps(message_data).encode()
        # Envia a mensagem para todos os peers (outros usuários) do chat.
        for peer in peers:
            sock.sendto(data, peer)
            # Adiciona a mensagem à lista de mensagens enviadas
            sent_messages.append((message_data, peer))  

# Função para enviar pings para verificar a presença online dos pares.
def send_pings(sock, peers, online_peers):
    while True:
        for peer in peers:
            try:
                sock.sendto(b"PING", peer)
                data, addr = sock.recvfrom(1024)
                if addr not in online_peers:
                    online_peers.append(addr)
                    print(f"{addr} está online.")
            except Exception as e:
                if addr in online_peers:
                    online_peers.remove(addr)
                    print(f"{addr} está offline.")
        time.sleep(PING_INTERVAL)

# Função para exibir as mensagens enviadas e recebidas.
def display_messages(alias, peers, sock):
    while True:
        command = input("Digite /historico para ver o histórico de mensagens ou digite sua mensagem: ")
        if command.strip() == "/historico":
            print("\nMensagens Enviadas:")
            for message, peer in sent_messages:
                print(f"Para {peer}: {message['text']}")
            print("\nMensagens Recebidas:")
            for message, addr in received_messages:
                print(f"De {addr}: {message['text']}")
        else:
            # Não envia o tempo do relógio ao digitar mensagens diretamente.
            message_data = {"alias": alias, "text": command}
            data = json.dumps(message_data).encode()
            for peer in peers:
                sock.sendto(data, peer)
                # Adiciona a mensagem à lista de mensagens enviadas
                sent_messages.append((message_data, peer))  

# Função principal para executar o chat.
def main():
    # Solicita ao usuário um apelido para o chat.
    alias = input("Digite seu apelido no chat: ")  

    # Obtém o IP da máquina
    ip = socket.gethostbyname(socket.gethostname())
    print("Meu IP:", ip)

    # Lista para armazenar os endereços IP dos outros membros do chat (pré-definidos).
    peers = [("192.16.103.9", numIp)]  # Adiciona o seu próprio IP à lista de pares

    # Lista para armazenar os pares online.
    online_peers = []

    # Configura o socket para comunicação UDP.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', numIp))  # Associa o socket à porta definida.

    # Cria uma instância do relógio de Lamport.
    clock = LamportClock()  

    # Cria e inicia uma thread para ouvir mensagens.
    listener_thread = threading.Thread(target=listen_for_messages, args=(sock, clock, alias, peers, online_peers), daemon=True)
    listener_thread.start()

    # Cria e inicia uma thread para enviar mensagens.
    sender_thread = threading.Thread(target=send_message, args=(sock, clock, alias, peers), daemon=True)
    sender_thread.start()

    # Cria e inicia uma thread para enviar pings.
    ping_thread = threading.Thread(target=send_pings, args=(sock, peers, online_peers), daemon=True)
    ping_thread.start()

    # Cria e inicia uma thread para exibir as mensagens.
    display_thread = threading.Thread(target=display_messages, args=(alias, peers, sock), daemon=True)
    display_thread.start()

    # Aguarda as threads terminarem (o que nunca deve acontecer neste caso).
    listener_thread.join()
    sender_thread.join()
    ping_thread.join()
    display_thread.join()

    sock.close()

if __name__ == "__main__":
    main()  # Executa a função principal se o script for o módulo principal.
