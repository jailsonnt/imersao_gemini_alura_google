# Trabalho de conclusão: Imersao AI Gemini Alura e Google

Esse projeto foi criado para apresentar o trabalho de finalização do treinamento intensivo para aprender o básico do gemini.

## O projeto: IAmiga, Gemini Explorer

Quantas vezes estamos viajando e queremos explorar? Mas quantas vezes perdemos muito tempo já na primeira tarefa: **Escolher onde ir** , mesmo em casa muitas vezes simplesmente não sabemos oque queremos para o fim de semana. Muito bem, **"Agora seus problemas acabaram"**. A **IAmiga**, em uma curta conversa vai entender o seu gosto e quem está com você para achar dicas de lugares para salvar o seu fim de semana.<br> Com grande ajuda do nosso amigo google esse projeto integrou o uso da API Gemini e Places para identificar seus gostos e prontamente procurar por lugares de interesse.
<br>Melhor do que uma simples busca no google, nós vamos tentar entender o seu gosto agora, e então achar lugares para você.

## Fontes

### Desenvolvimento no colab

**Arquivo:** final_imersao_gemini_alura_google_somente_colab.ipynb

Aqui está o fonte principal, o código solicita uma chave de API do gemini para uso na hora, é importante que seja uma chave válida.
<br>Depois disso, uma conversa será iniciada com o objetivo de preparar as sugestões. Assim que as sugestões são identificadas automaticamente é feita 
uma busca na API Places, através de uma function na google cloud (apresentaremos esse código abaixo). O programa finaliza apresentado na tela 2 sugestões para cada sugestão identificada.

### Desenvolvimento no google Cloud functions

**Arquivos:** main.py e requirements.txt

Esses arquivos contem o código e as bibliotecas necessárias para buscar na API places do google, mas para esse projeto já está tudo funcionando com a URL da function permanecendo ativa pelo menos até a data da avaliação do projeto 13/05/24.
Todos os custos dessa funcionalidade estão dentro da free tier do google cloud.



