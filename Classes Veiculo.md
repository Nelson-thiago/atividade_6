Aqui está uma modelagem das classes, mostrando a hierarquia entre a classe mãe e as classes filhas:

### Classe Mãe: `Veiculo`
Essa será a classe base, que contém as propriedades e métodos comuns a todos os veículos, independentemente de serem carros ou motocicletas.

#### **Propriedades da Classe `Veiculo`:**
- `nome (privado)`: Nome do veículo.
- `ano (privado)`: Ano de fabricação do veículo.
- `valor_diario (privado)`: Valor diário do aluguel.

#### **Métodos da Classe `Veiculo`:**
- `get_nome() / set_nome()`: Métodos para acessar e alterar o nome do veículo.
- `get_ano() / set_ano()`: Métodos para acessar e alterar o ano do veículo.
- `get_valor_diario() / set_valor_diario()`: Métodos para acessar e alterar o valor diário do aluguel.
- `calcular_aluguel(dias)`: Método para calcular o valor total do aluguel com base no número de dias. Esse método pode ser sobrescrito nas subclasses.
- `calcular_aluguel(dias, desconto_opcional=None)`: Método sobrecarregado para aceitar um desconto opcional.

#### **Métodos de Classe:**
- `total_veiculos()`: Método de classe para contar quantos veículos foram cadastrados no sistema.
- `aumentar_valor(percentual)`: Método de classe para aplicar um aumento percentual ao valor diário de todos os veículos.

---

### Classe Filha: `Carro` (herda de `Veiculo`)
Essa classe herda de `Veiculo`, mas adiciona propriedades e comportamentos específicos para carros.

#### **Propriedades da Classe `Carro`:**
- `tipo_combustivel (privado)`: Propriedade específica para armazenar o tipo de combustível (gasolina, etanol, etc.).

#### **Métodos da Classe `Carro`:**
- Sobrescrever o método `calcular_aluguel` para aplicar um desconto se o aluguel for por mais de 7 dias.

---

### Classe Filha: `Motocicleta` (herda de `Veiculo`)
Essa classe também herda de `Veiculo`, mas foca nas especificidades das motocicletas.

#### **Propriedades da Classe `Motocicleta`:**
- `cilindrada (privado)`: Propriedade específica para armazenar a cilindrada da motocicleta (150cc, 250cc, etc.).

#### **Métodos da Classe `Motocicleta`:**
- Sobrescrever o método `calcular_aluguel` para aumentar o custo do aluguel se a cilindrada for maior que 200cc.

---

### Resumo da Hierarquia

1. **Classe Mãe:** `Veiculo`
   - Contém as propriedades e métodos básicos que são comuns a todos os veículos.
2. **Classe Filha:** `Carro`
   - Herda de `Veiculo` e adiciona a propriedade de `tipo_combustivel`, além de sobrescrever o cálculo de aluguel para aplicar descontos.
3. **Classe Filha:** `Motocicleta`
   - Herda de `Veiculo` e adiciona a propriedade de `cilindrada`, além de sobrescrever o cálculo de aluguel para aumentar o custo dependendo da cilindrada.

Essa modelagem separa claramente as responsabilidades e permite que os desenvolvedores possam trabalhar de forma independente nas subclasses enquanto compartilham a mesma estrutura básica da classe mãe.