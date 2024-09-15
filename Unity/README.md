## 1. Configuração da Unity para receber os dados via serial.

Primeiramente, deve-se criar um projeto 3D. Ao criar, clique em "Edit", "Project Settings", "Player", procure pela opção "Apl Compability Level" e altere para ".NET Framework".

## 2. Código de comunicação serial.

Cique com o mouse direito na caixa onde contém as pastas (a princípio haverá apenas a pasta "Scenes") e depois em "Create". Crie um código em C#. O código pode ser encontrado nesta mesma pasta do repositório do GitHub com o nome "serial_unity".

## 3. Observações importantes.

O código do Arduino deve retornar apenas os valores dos sensores separados por vírgulas. A Unity interpreta os valores como uma string, ou seja, se o Arduino retornar mensagens de texto, haverá uma interferência nos valores lidos pela Unity, por isso é importante que o Arduino retorne apenas floats. Assim, o código em C# da Unity serve para fazer a comunicação serial e transformar as variáveis string em float.

Não se esqueça de fechar o serial do Arduino para que a Unity possa ler os valores. Além disso, confirme se o baud rate e porta serial são os mesmos configurados na Unity e Arduino.