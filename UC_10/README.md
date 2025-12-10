# UC 10 - Desenvolver Banco de Dados

## Configurações Iniciais

Trabalharemos as noções fundamentais de Banco de Dados e linguagem SQL com o auxílio do [SQLite](https://www.sqlitetutorial.net/).

Para tanto, siga as instruções abaixo para configurar o SQLite.

### **Passo a passo para usar SQLite com a base Chinook**

#### **1. Instalar SQLite**

Baixe o gerenciador gráfico para o SQLite:
*   **DB Browser for SQLite** (<https://sqlitebrowser.org/>)

#### **2. Baixar a base Chinook**

A base de dados `chinook.db` já está disponivel na pasta `SQLite`.

Portanto, para acessar a base por meio deste repositório, basta abrir o terminal, navegar até a pasta do repositório `TecInfo_2024.7.101`, e digitar a seguinte sequência de comandos:

```bash
git checkout main
git pull
```

Desta forma, quaisquer mudanças realizadas na base de dados de exemplo poderá ser facilmente revertida ao final da realização dos testes.

> [!note]
> A base de dados de testes pode ser encontrada também no site oficial do SQLite:
> *   Acesse: <https://www.sqlitetutorial.net/sqlite-sample-database/>
> *   Baixe o arquivo **Chinook.db** (já pronto para uso)

#### **3. Abrir a base**

*   No **DB Browser for SQLite**:
    *   Clique em **Open Database**
    *   Selecione **Chinook.db**
*   Você verá tabelas como:
    *   **albums, artists, customers, invoices, tracks**

#### **4. Testar consultas**

No **DB Browser**, abra a aba *Execute SQL* e digite o seguinte comando:

```sql
SELECT * FROM albums LIMIT 10;
```
