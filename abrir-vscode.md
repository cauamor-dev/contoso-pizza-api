# Abrir a API no VS Code e preparar uma captura

1. Abra o VS Code. Vá em **Arquivo > Abrir Pasta** e escolha a pasta **ContosoPizza** deste projeto. Confirme **Selecionar Pasta**.
2. No explorador à esquerda, abra **Controllers > PizzaController.cs**. Esse arquivo mostra as ações da API e costuma render uma boa captura.
3. Vá em **Terminal > Novo Terminal** e execute:

```powershell
dotnet run --launch-profile http
```

Espere aparecer `Now listening on: http://localhost:5206`. Deixe esse terminal aberto: ele está executando a API.

4. Abra um segundo terminal pelo botão **+** do painel Terminal e execute:

```powershell
$resposta = Invoke-WebRequest -Uri 'http://localhost:5206/pizza'
"HTTP $($resposta.StatusCode)"
$resposta.Content | ConvertFrom-Json | ConvertTo-Json
```

O resultado esperado é `HTTP 200` e uma lista JSON com as pizzas **Classic Italian** e **Veggie**.

5. Deixe o código do controller visível na parte superior e a resposta JSON na parte inferior. Aumente a altura do terminal arrastando a divisória, se necessário. Use **Ctrl + +** para aumentar o texto se estiver pequeno.
6. Pressione **Windows + Shift + S** e selecione a região com o código e a resposta. Salve a captura como `contoso-pizza-api-vscode.png` para anexar ao post.

Para parar a API, volte ao primeiro terminal e pressione **Ctrl + C**. Os dados são somente em memória: ao executar novamente, a lista volta às duas pizzas originais.

Sugestão de legenda da imagem: “Controller em C# e resposta JSON da API de pizzas — exercício do Microsoft Learn.”

