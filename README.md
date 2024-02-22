

# TEC502 - ZapZaps 2.0

Este projeto consiste em um sistema de chat implementado em Python utilizando sockets UDP para comunicação entre os usuários. O sistema permite que múltiplos usuários se comuniquem em tempo real, sem a necessidade de uma conexão persistente, o que é ideal para ambientes distribuídos.

## Índice

- [Introdução](#introducao)
- [Fundamentação Teórica](#fundamentacao)
- [Desenvolvimento](#desenvolvimento)
- [Metodologia](#metodologia)
- [Funcionalidades e Interfaces](#funcionalidade)
- [Como Executar a Aplicação](#execucao)
- [Áreas para Melhorias e Expansão](#melhoria)
- [Considerações Finais](#consideracoes)

---

## Introdução <a id="introducao"></a>

Os aplicativos de mensagens desempenham um papel fundamental no ambiente corporativo, transformando a forma como as organizações se comunicam e colaboram. Em um mundo empresarial cada vez mais dinâmico e globalizado, a capacidade de trocar informações de maneira rápida e eficiente é crucial para o sucesso de qualquer empreendimento. Os aplicativos de mensagens oferecem uma plataforma instantânea para a comunicação, quebrando as barreiras de tempo e espaço, permitindo que equipes se conectem instantaneamente, independentemente da localização geográfica.

---

## Fundamentação Teórica <a id="fundamentacao"></a>

### Sockets UDP

A comunicação em rede é realizada utilizando o protocolo UDP (User Datagram Protocol), que é ideal para aplicações em tempo real, como um chat, devido à sua simplicidade e baixa sobrecarga.

### Relógio de Lamport

O sistema utiliza um relógio de Lamport para sincronização de eventos em um ambiente distribuído. Isso garante que a ordem das mensagens seja preservada, mesmo quando estas são enviadas e recebidas de diferentes fontes.

---

## Desenvolvimento <a id="desenvolvimento"></a>

O produto em forma de software foi desenvolvido utilizando a linguagem de programação Python na versão 3.11. Foram utilizadas as bibliotecas padrão da linguagem, incluindo socket, threading, json, time, os, entre outras. O sistema foi construído para operar em um ambiente descentralizado, sem a necessidade de um servidor central, proporcionando uma solução simples e eficiente para comunicação entre os membros de uma empresa.

---
## Metodologia <a id="metodologia"></a>

Na metodologia de desenvolvimento deste sistema de mensagens instantâneas baseado em P2P (peer-to-peer), a sincronização desempenha um papel crucial para garantir a consistência das operações e a ordem das mensagens trocadas entre os usuários. Optou-se por utilizar relógios lógicos, em vez de relógios baseados em tempo absoluto, devido às características de ambientes distribuídos onde múltiplos dispositivos interagem.

Dentre as opções disponíveis para a implementação do relógio lógico, o algoritmo de Lamport foi escolhido devido à sua simplicidade e eficácia em lidar com sistemas distribuídos. Este algoritmo não depende de um tempo absoluto, mas sim de uma contagem local de eventos em cada processo. Cada evento é marcado com um carimbo de tempo lógico, o que representa a relação causal entre os eventos em diferentes nós da rede.

A ordenação das mensagens no sistema foi realizada combinando o timestamp do relógio de Lamport com o endereço IP do remetente da mensagem. Isso garante que as mensagens sejam ordenadas de acordo com o tempo lógico em que foram recebidas, mesmo em um ambiente distribuído onde os eventos podem ocorrer em diferentes nós de forma assíncrona.

A implementação da sincronização foi realizada utilizando threads em Python, onde cada thread é responsável por uma funcionalidade específica do sistema, como ouvir mensagens, enviar mensagens, enviar pings para verificar a presença online dos pares e exibir as mensagens enviadas e recebidas. Essa abordagem permite que as diferentes operações ocorram de forma assíncrona, garantindo uma comunicação eficiente e sincronizada entre os usuários do sistema.

---

## Funcionalidades e Interfaces <a id="funcionalidade"></a>

O sistema permite que os usuários realizem as seguintes operações:

- Envio de mensagens em tempo real.
- Sincronização de mensagens através do relógio de Lamport.

---

## Como Executar a Aplicação <a id="execucao"></a>

Para executar o servidor do chat, siga as etapas abaixo:

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Execute o arquivo `updateChat.py`.
4. Digite um apelido quando solicitado.
5. Envie mensagens para o chat digitando no terminal.

---

## Áreas para Melhorias e Expansão <a id="melhoria"></a>

Este projeto pode ser expandido e melhorado de várias maneiras, incluindo:

- Desenvolvimento de uma interface gráfica para melhorar a usabilidade.
- Recebimento das mensagens pelos usuários.
- Implementação de um sistema de autenticação para garantir a segurança.
- Melhoria na gestão de erros e exceções para uma experiência mais robusta.

---

## Considerações Finais <a id="consideracoes"></a>


Este projeto resultou em um sistema de chat que, embora funcional para o envio de mensagens, ainda precisa de melhorias para permitir a recepção de mensagens, tornando-o mais completo e adequado para comunicação em tempo real em ambientes distribuídos. Atualmente, o sistema apenas envia mensagens entre os usuários, sem a capacidade de receber e exibir mensagens recebidas.

Embora o sistema não inclua recursos avançados, como criptografia, ele oferece uma base sólida que pode ser expandida e aprimorada para atender a diferentes requisitos e necessidades dos usuários. Uma melhoria imediata seria implementar a funcionalidade de recebimento de mensagens, garantindo assim uma comunicação bidirecional entre os usuários.

Além disso, o sistema poderia ser expandido para incluir recursos adicionais, como criptografia para garantir a segurança das comunicações, uma interface gráfica para uma melhor experiência do usuário e um sistema de autenticação para verificar a identidade dos usuários. Melhorias na gestão de erros e exceções também seriam benéficas para tornar o sistema mais robusto e confiável.
