# ContosoPizza — exercício de ASP.NET Core

API de estudo baseada no módulo [Criar uma API Web com os controladores do ASP.NET Core](https://learn.microsoft.com/pt-br/training/modules/build-web-api-aspnet-core/) do Microsoft Learn. Implementação e verificação realizadas com assistência de IA, como material para revisão posterior.

**Conclusão registrada:** 01/10/2026, no perfil Cauã Moreira. As nove unidades e as verificações de conhecimento foram concluídas. [Comprovante oficial da conquista](https://learn.microsoft.com/pt-br/users/caumoreira-1798/achievements/print/VSREL87M). Trata-se de um emblema de conclusão de módulo, distinto de uma certificação profissional Microsoft.


## Executar

Pré-requisito: SDK do .NET 10. Na pasta deste arquivo:

```powershell
dotnet run --launch-profile http
```

A API fica disponível em `http://localhost:5206`. Esse perfil HTTP foi usado somente para a demonstração local. O perfil `https` original e o redirecionamento HTTPS foram preservados.

## Rotas

| Método | Caminho | Resultado |
|---|---|---|
| GET | /weatherforecast | Exemplo inicial do template |
| GET | /pizza | Lista as pizzas |
| GET | /pizza/{id} | Consulta uma pizza; 404 se não existir |
| POST | /pizza | Cadastra; retorna 201, JSON e Location |
| PUT | /pizza/{id} | Atualiza; retorna 204, 400 ou 404 |
| DELETE | /pizza/{id} | Exclui; retorna 204 ou 404 |

## Entender em cinco pontos

1. **Requisição:** o front-end envia o método HTTP, a URL e, quando necessário, um JSON.
2. **Controller:** `PizzaController` decide qual método C# atende à rota e monta a resposta HTTP.
3. **Model:** `Pizza` descreve os dados: ID, nome e opção sem glúten.
4. **Service:** `PizzaService` guarda a lista e realiza as operações.
5. **Resposta:** a API devolve dados e um código HTTP. 200 = consulta bem-sucedida; 201 = criado; 204 = sucesso sem corpo; 400 = solicitação inválida; 404 = não encontrado.

`[ApiController]` habilita comportamentos de API, como inferência de parâmetros e validação automática. `[Route("[controller]")]` associa `PizzaController` ao caminho `/pizza`. `[HttpGet]`, `[HttpPost]`, `[HttpPut]` e `[HttpDelete]` associam métodos C# aos verbos HTTP.

## Verificação

O projeto compilou com SDK 10.0.300, sem avisos ou erros. Foram executadas **14 verificações HTTP** cobrindo operações CRUD, leitura após criação e atualização, cabeçalho Location, confirmação de exclusão e erros por recurso inexistente, ID divergente e ID não numérico.

As respostas reais estão em `evidencias/verificacao-api.json`. Para repetir, reinicie a API para restaurar as duas pizzas iniciais e execute, em outro terminal:

```powershell
python verify_api.py
```

O script usa somente a biblioteca padrão do Python. Também há requisições em `ContosoPizza.http` para uso com um cliente REST compatível.

## Adaptações e limites

- O material usa .NET 8; este exercício usa o SDK .NET 10 já instalado. O comportamento das rotas do exercício foi mantido.
- O template foi criado com `--no-openapi`, sem dependências extras. O HTTP REPL é uma atividade opcional e foi substituído por requisições HTTP diretas verificadas.
- O armazenamento é uma lista em memória, conforme o exercício. Os dados são perdidos ao reiniciar. Não há SQL nem Entity Framework neste módulo.
- A lista estática não foi preparada para acessos simultâneos de produção. O exemplo também não implementa autenticação nem validação completa do domínio, como nome obrigatório.
- É um exercício introdutório de curso. Aprofundar persistência, injeção de dependência, validação e testes faz parte de uma evolução posterior.

## Revisão prática sugerida

Leia `Program.cs`, `Models/Pizza.cs`, `Services/PizzaService.cs` e `Controllers/PizzaController.cs`, nessa ordem. Depois, altere o nome de uma pizza usando o arquivo HTTP e acompanhe o caminho da requisição pelo controller e pelo service.

## Origem

- [Criar o projeto](https://learn.microsoft.com/pt-br/training/modules/build-web-api-aspnet-core/3-exercise-create-web-api/)
- [Adicionar o armazenamento](https://learn.microsoft.com/pt-br/training/modules/build-web-api-aspnet-core/5-exercise-add-data-store/)
- [Adicionar o controlador](https://learn.microsoft.com/pt-br/training/modules/build-web-api-aspnet-core/6-exercise-add-controller/)
- [Implementar CRUD](https://learn.microsoft.com/pt-br/training/modules/build-web-api-aspnet-core/8-exercise-implement-crud/)

