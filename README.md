CASE PROPOSTO

Uma empresa decidiu criar seu Data Lake on premise. Demonstre, com uma prototipação, como você faria a criação do data lake com base em uma distribuição de Hadoop. O Data lake deve conter as camadas de arquitetura de dados organizadas como preferir. Entre os cenários de implementação a seguir escolha no mínimo 4 para embarcar no seu protótipo. Quanto mais implementações corretas maior será a sua pontuação.

CENÁRIO IMPLEMENTADO

•	Ingestão de dados do Twitter com #Santander
•	Demonstrar uma ingestão lambda
•	Demonstrar as opções para melhorar a performance de consumo de dados do data lake via SQL
•	Demonstre a importância da modelagem de dados para data lake.

PROPOSTA IMPLEMENTADA

Para a protótipo de demonstração solicitado, foi utilizado uma arquitetura flexível onde o cliente pode decidir utilizar uma arquitetura interna ou em um futuro, possa utilizar uma arquitetura cloud, poderá adaptar esse protótipo de uma forma tranquila para utilização de todos os recursos propostos.

Como fonte de informações vamos utilizar o Twitter, executando por um processo batch a consulta por hashtag e nessa execução utilizamos #Santander.

Toda a execução está sendo feita por containers Docker, configurados em um arquivo único de inicialização do ambiente, (docker-compose.yml) ficando disponível para ser utilizado.
























DESENHO DA ARQUITETURA UTILIZADA











•	Twitter: fonte de dados de mídia social utilizada para consultas de posts.
•	Python: linguagem de programação escolhida para integrar com a mídia social e disponibilizar dados em um tópico.
•	Kafka: utilizado para recepcionar os dados processados do Twiter através do motor python e disponibilizar para vários destinos se necessário através de tópico replicado em vários brockers.
•	Zookeeper: nesse protótipo é utilizado para gerencias os brockers do Kafka e controlar falhas caso necessário.
•	Kafdrop: ferramenta web de monitoramento dos tópicos disponíveis na arquitetura do Kafka
•	Python: motor desenvolvido para consumir os dados disponibilizados no Kafka e gravar em uma estrutura dentro de um database nosql, processamento lambda.
•	ScyllaDB: Banco de dados NoSql de alta performance de leitura e gravação escolhido para disponibilizar os dados para consumo.
•	Docker: serviço de virtualização utilizado para montar todo o ambiente utilizado.





Iniciando ambiente para execução

•	Iniciar os containers com o comando abaixo:
D:\Users\xxx\twitter>docker-compose up -d







•	Verifica se todos os containers foram iniciados 
D:\Users\xxx\twitter>docker-compose ps





•	Checa se os nós, do scylladb estão disponíveis
D:\Users\xxx\twitter>docker exec -it twitter_scylla-node1_1 nodetool status












•	Abrir o endereço do Kafdrop para monitorar os tópicos utilizados
http://localhost:19000/
















•	Instala as dependências python necessárias para o projeto
pip install tweepy
pip install kafka-python
pip install scylla-driver
pip install pyspark


•	Executando o motor coleta_tweets.py, ele vai pesquisar e inserir as mensagens no tópico do Kafka
python.exe D:/Users/xxx/twitter/coleta_tweets.py






•	Lista as mensagens no Kafdrop















•	Executa motor de consumo do Kafka e armazena os dados ScyllaDB 
python.exe D:/Users/cmora/twitter/grava_scylla.py





•	Verifica as mensagens inseridas no ScyllaDB
docker exec -it twitter_scylla-node1_1 cqlsh
Select * from twitters.twitt;






MELHORAR PERFORMANCE DE CONSUMO DOS DADOS NO DATA LAKE

Para melhor consumo e resiliência dos dados, utilizamos um cluster de banco de dados com três nós e modelamos a tabela para que tenhamos partições dos dados nesse exemplo por dia. Mas poderíamos utilizar também uma sub partição por region para os dados brutos coletados.
CREATE TABLE twitt (
horario text,
created_at text,
desc_text text,
hashtg text,
id_usr text,
screen_name text,
location text,
followers_count text,
friends_count text,
listed_count text,
created_at_usr text,
favourites_count text,
statuses_count text,
retweet_count text,
favorite_count text,
lang text,
dt_proc text,...
PRIMARY KEY((dt_proc)));


Cluster ScyllaDB
 

MODELAGEM DE DADOS PARA DATA LAKE

O conceito de um data lake é um repositório central que possa armazenar todos os tipos de dados estruturados e não estruturados de forma bruta. Muitas vezes pode -se usar mais que uma tecnologia para garantir todas as estratégias de armazenamento.
Para que os cientistas de dados possam ter um melhor proveito desses dados precisamos:
•	Escolher as tecnologias corretas para cada tipo de necessidade e informação que vamos utilizar
•	Governança dos dados existentes de forma que os usuários saibam o que existe e o que obter com cada um
•	Interface de consumo dos dados transparentes e de fácil acesso para geração de valor sobre toda a gama de informações disponíveis

Vantagens e termos fáceis acesso as informações e um poder de processamento ideal pode evitar por exemplo fraudes em sistemas, consultas rápidas a históricos de uso de aplicações, entre outras.

