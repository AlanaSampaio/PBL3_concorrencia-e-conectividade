

# <div align="center">TEC502 - ZapZaps 2.0</div>

<em>
  A comunicação em tempo real é crucial para empresas no mundo globalizado. Softwares de mensagens instantâneas facilitam essa comunicação, quebrando barreiras de tempo e espaço.. Fez-se necessario o desenvolvimento de um novo software de mensagens instantâneas baseado no modelo peer-to-peer (P2P) que atenda aos requisitos específicos de descentralização, confiabilidade e simplicidade.  O sistema atual envia mensagens, mas não as recebe, tornando-o incompleto e inadequado para comunicação bidirecional em ambientes distribuídos. Este projeto fornece uma base sólida para um sistema de chat, destaca a importância da sincronização em ambientes distribuídos e opta pelo algoritmo  Lamport para garantir a consistência das mensagens. A implementação da sincronização é feita usando streams Python, que combinam o carimbo de data/hora do relógio  Lamport com o endereço IP  da pessoa que envia a mensagem ao comando. Embora exista funcionalidade para  envio de mensagens, o sistema precisa de melhorias para permitir o recebimento de mensagens e implementar recursos adicionais, como criptografia, interface gráfica e autenticação.
</em<>

---

## Índice

- [Introdução](#introducao)
- [Fundamentação Teórica](#fundamentacao)
- [Metodologia](#metodologia)
- [Implementação](#implementacao)
- [Como Executar a Aplicação](#execucao)
- [Áreas para Melhorias e Expansão](#melhoria)
- [Considerações Finais](#consideracoes)

---

## Introdução <a id="introducao"></a>

  Os dispositivos móveis, como smartphones e tablets, expandem a nossa conectividade ao mundo de hoje, facilitando a comunicação instantânea. Aplicativos de mensagens como chat de texto desempenham um papel importante nesta comunicação global.  
  
  O problema é desenvolver um novo software de mensagens P2P que atenda a requisitos específicos, como confiabilidade e uma interface específica. As restrições incluem o uso de contêineres Docker e a exclusão de estruturas de mensagens. Os recursos desejados são mensagens em tempo real e sincronização entre usuários, com interface shell script.  
  
  Para contribuir para isso, enfatizamos o desenvolvimento de  software que melhore a confiabilidade da comunicação. Dois métodos são propostos para garantir a continuidade do programa, mesmo em situações de perda de conexão. A implantação usando contêineres Docker e a remoção da estrutura de mensagens é eficiente e simples. 
  
  Na abordagem aplicada, foi implementada uma estratégia confiável de confirmação de entrega. O sistema desenvolvido permite mensagens em tempo real entre usuários, mas a função de recebimento ainda precisa ser ajustada.

---

## Fundamentação Teórica <a id="fundamentacao"></a>

### Sockets UDP:

- Protocolo utilizado para comunicação em rede.
- Ideal para aplicativos em tempo real devido à sua simplicidade e baixa sobrecarga.

### Relógio de Lamport:

- Utilizado para sincronização de eventos em ambientes distribuídos.
- Garante a preservação da ordem das mensagens, mesmo de fontes distintas.

### Mecanismo de confirmação de entrega (ACK):

- Essencial para garantir a integridade da comunicação.
- Confirmação da recepção das mensagens para assegurar sua entrega segura.

### Contêineres Docker:

- Facilita o desenvolvimento e a implantação do sistema.
- Garante portabilidade e consistência em diferentes ambientes de execução.

### Interface em shell script:

- Proporciona uma experiência de usuário familiar e acessível.
- Simplifica a interação com o sistema, tornando-o mais intuitivo para os usuários.

---

## Metodologia <a id="metodologia"></a>

Na metodologia de desenvolvimento deste sistema de mensagens instantâneas baseado em P2P (peer-to-peer), a sincronização desempenha um papel crucial para garantir a consistência das operações e a ordem das mensagens trocadas entre os usuários. Optou-se por utilizar relógios lógicos, em vez de relógios baseados em tempo absoluto, devido às características de ambientes distribuídos onde múltiplos dispositivos interagem.

Dentre as opções disponíveis para a implementação do relógio lógico, o algoritmo de Lamport foi escolhido devido à sua simplicidade e eficácia em lidar com sistemas distribuídos. Este algoritmo não depende de um tempo absoluto, mas sim de uma contagem local de eventos em cada processo. Cada evento é marcado com um carimbo de tempo lógico, o que representa a relação causal entre os eventos em diferentes nós da rede.

A ordenação das mensagens no sistema foi realizada combinando o timestamp do relógio de Lamport com o endereço IP do remetente da mensagem. Isso garante que as mensagens sejam ordenadas de acordo com o tempo lógico em que foram recebidas, mesmo em um ambiente distribuído onde os eventos podem ocorrer em diferentes nós de forma assíncrona.

A implementação da sincronização foi realizada utilizando threads em Python, onde cada thread é responsável por uma funcionalidade específica do sistema, como ouvir mensagens, enviar mensagens, enviar pings para verificar a presença online dos pares e exibir as mensagens enviadas e recebidas. Essa abordagem permite que as diferentes operações ocorram de forma assíncrona, garantindo uma comunicação eficiente e sincronizada entre os usuários do sistema.

---

## Implementação <a id="implementacao"></a>

  Na implementação deste sistema, foi aplicada uma abordagem com fluxos Python para lidar com diversas funções, como envio e recebimento de mensagens, verificação de presença online e exibição de mensagens. Esta estrutura permite operações assíncronas, garantindo uma comunicação eficiente e síncrona entre os usuários. 
  
  O algoritmo  Lamport é utilizado para classificar mensagens, combinando seus carimbos de data e hora com o endereço IP do remetente para garantir consistência mesmo em ambientes distribuídos. Esta implementação destaca-se pela sua eficiência e  capacidade de gerir a complexidade dos sistemas distribuídos, proporcionando uma experiência de comunicação fiável e ordenada aos utilizadores. 
    
  Além disso,  a confiabilidade da entrega de mensagens foi aprimorada através do uso de confirmações (ACKs), adicionando uma camada adicional de segurança para garantir a entrega precisa, mesmo em condições de conexão instáveis. 
      
  O uso de contêineres Docker facilita o desenvolvimento, o teste e a implantação do sistema, garante a consistência do tempo de execução entre plataformas e simplifica o processo de entrega de software.
  
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
- Implementação do shell.
- Implementação de um sistema de autenticação para garantir a segurança.
- Melhoria na gestão de erros e exceções para uma experiência mais robusta.

---

## Considerações Finais <a id="consideracoes"></a>


Este projeto resultou em um sistema de chat que, embora funcional para o envio de mensagens, ainda precisa de melhorias para permitir a recepção de mensagens, tornando-o mais completo e adequado para comunicação em tempo real em ambientes distribuídos. Atualmente, o sistema apenas envia mensagens entre os usuários, sem a capacidade de receber e exibir mensagens recebidas.

Embora o sistema não inclua recursos avançados, como criptografia, ele oferece uma base sólida que pode ser expandida e aprimorada para atender a diferentes requisitos e necessidades dos usuários. Uma melhoria imediata seria implementar a funcionalidade de recebimento de mensagens, garantindo assim uma comunicação bidirecional entre os usuários.

Além disso, o sistema poderia ser expandido para incluir recursos adicionais, como criptografia para garantir a segurança das comunicações, uma interface gráfica para uma melhor experiência do usuário e um sistema de autenticação para verificar a identidade dos usuários. Melhorias na gestão de erros e exceções também seriam benéficas para tornar o sistema mais robusto e confiável.
