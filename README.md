# 锂语言/Lith Language

## 项目简介
锂语言（Lith）是一种基于Python进行扩展的编程语言（库），旨在提供更为精炼和高效的编程体验。目前，锂语言仍处于开发阶段，部分功能尚不完善，但已具备基本的语法结构和运行时环境。

*tips*:本语言部分技术来自YouTube@davidcallanan。

## 安装指南
### Python环境
- 确保已安装Python 3.x版本。可通过在终端运行`python --version`或`python3 --version`来检查Python版本。
- 若未安装Python，可访问[Python官网](https://www.python.org/downloads/)下载并安装适合您操作系统的Python版本。

### 锂语言环境
- 克隆或下载本项目仓库到本地。
- 在项目根目录下，打开终端或命令提示符。
- 运行`python basic.py`或`python3 basic.py`启动锂语言解释器。

## 代码示例
### 基本语法
- 首先，让我们导入`Lith Language`。
```python
import lith
```
- 现在，您便可在`Python 3.x`中运行Lith。
```python
# 变量声明与赋值
VAR x = 5
VAR y = "Hello, Lith!"

# 输出
PRINT(x)
PRINT(y)
```
### 控制结构
```python
# 条件语句
IF x > 3 THEN
    PRINT("x 大于 3")
ELSE
    PRINT("x 小于等于 3")
END

# 循环语句
FOR i = 0 TO 5 THEN
    PRINT(i)
END

WHILE x > 0 THEN
    PRINT(x)
    x = x - 1
END
```
### 函数定义与调用
```python
# 函数定义
FUN add(a, b) THEN
    RETURN a + b
END

# 函数调用
VAR result = add(3, 4)
PRINT(result)
```
# 语法规则

## 语句序列（statements）
- **statements**：语句序列
  - **NEWLINE\***：零个或多个换行符
  - **statement**：语句
  - **(NEWLINE+ statement)\***：一个或多个换行符后跟一个语句，此结构可重复零次或多次
  - **NEWLINE\***：零个或多个换行符

## 语句（statement）
- **statement**：语句
  - **KEYWORD:RETURN expr?**：返回语句，可选地后跟一个表达式
  - **KEYWORD:CONTINUE**：继续语句
  - **KEYWORD:BREAK**：中断语句
  - **expr**：表达式

## 表达式（expr）
- **expr**：表达式
  - **KEYWORD:VAR IDENTIFIER EQ expr**：变量声明，后跟一个标识符、等号和一个表达式
  - **comp-expr ((KEYWORD:AND|KEYWORD:OR) comp-expr)\***：比较表达式，可选地后跟一个或多个由“与”或“或”连接的比较表达式

## 比较表达式（comp-expr）
- **comp-expr**：比较表达式
  - **NOT comp-expr**：非比较表达式
  - **arith-expr ((EE|LT|GT|LTE|GTE) arith-expr)\***：算术表达式，可选地后跟一个或多个由相等、小于、大于、小于等于、大于等于连接的算术表达式

## 算术表达式（arith-expr）
- **arith-expr**：算术表达式
  - **term ((PLUS|MINUS) term)\***：项，可选地后跟一个或多个由加号或减号连接的项

## 项（term）
- **term**：项
  - **factor ((MUL|DIV) factor)\***：因子，可选地后跟一个或多个由乘号或除号连接的因子

## 因子（factor）
- **factor**：因子
  - **(PLUS|MINUS) factor**：加号或减号后跟一个因子
  - **power**：幂表达式

## 幂表达式（power）
- **power**：幂表达式
  - **call (POW factor)\***：调用表达式，可选地后跟一个或多个由幂运算符连接的因子

## 调用表达式（call）
- **call**：调用表达式
  - **atom (LPAREN (expr (COMMA expr)*)? RPAREN)?**：原子表达式，可选地后跟一个由左括号、零个或多个由逗号分隔的表达式、右括号组成的参数列表

## 原子表达式（atom）
- **atom**：原子表达式
  - **INT|FLOAT|STRING|IDENTIFIER**：整数、浮点数、字符串或标识符
  - **LPAREN expr RPAREN**：括号内的表达式
  - **list-expr**：列表表达式
  - **if-expr**：条件表达式
  - **for-expr**：循环表达式
  - **while-expr**：循环表达式
  - **func-def**：函数定义

## 列表表达式（list-expr）
- **list-expr**：列表表达式
  - **LSQUARE (expr (COMMA expr)*)? RSQUARE**：左方括号、零个或多个由逗号分隔的表达式、右方括号

## 条件表达式（if-expr）
- **if-expr**：条件表达式
  - **KEYWORD:IF expr KEYWORD:THEN (statement if-expr-b|if-expr-c?)**：如果表达式，后跟一个语句、条件表达式分支b或条件表达式分支c（可选）
  - **(NEWLINE statements KEYWORD:END|if-expr-b|if-expr-c)**：换行符后跟语句序列和结束关键字，或条件表达式分支b或条件表达式分支c

## 条件表达式分支b（if-expr-b）
- **if-expr-b**：条件表达式分支b
  - **KEYWORD:ELIF expr KEYWORD:THEN (statement if-expr-b|if-expr-c?)**：否则如果表达式，后跟一个语句、条件表达式分支b或条件表达式分支c（可选）
  - **(NEWLINE statements KEYWORD:END|if-expr-b|if-expr-c)**：换行符后跟语句序列和结束关键字，或条件表达式分支b或条件表达式分支c

## 条件表达式分支c（if-expr-c）
- **if-expr-c**：条件表达式分支c
  - **KEYWORD:ELSE statement**：否则表达式，后跟一个语句
  - **(NEWLINE statements KEYWORD:END)**：换行符后跟语句序列和结束关键字

## 循环表达式（for-expr）
- **for-expr**：循环表达式
  - **KEYWORD:FOR IDENTIFIER EQ expr KEYWORD:TO expr (KEYWORD:STEP expr)? KEYWORD:THEN statement**：for循环表达式，后跟一个标识符、等号、表达式、to关键字、表达式、可选的step关键字和表达式、then关键字和一个语句
  - **(NEWLINE statements KEYWORD:END)**：换行符后跟语句序列和结束关键字

## 循环表达式（while-expr）
- **while-expr**：循环表达式
  - **KEYWORD:WHILE expr KEYWORD:THEN statement**：while循环表达式，后跟一个表达式、then关键字和一个语句
  - **(NEWLINE statements KEYWORD:END)**：换行符后跟语句序列和结束关键字

## 函数定义（func-def）
- **func-def**：函数定义
  - **KEYWORD:FUN IDENTIFIER? LPAREN (IDENTIFIER (COMMA IDENTIFIER)*)? RPAREN (ARROW expr)**：函数定义，可选地后跟一个标识符、左括号、零个或多个由逗号分隔的标识符、右括号和箭头表达式
  - **(NEWLINE statements KEYWORD:END)**：换行符后跟语句序列和结束关键字

# 贡献指南
欢迎对锂语言项目进行贡献！以下是一些贡献方式和建议：

## 报告问题
- **发现错误**：在使用锂语言的过程中，如果遇到任何错误或异常，请详细记录错误信息、发生错误的代码片段以及复现步骤，并在项目仓库的“Issues”页面提交一个新的问题报告。
- **提出改进建议**：如果你认为锂语言在某些方面可以做得更好，比如增加新的功能、优化性能、改进语法等，也可以在“Issues”页面提出你的建议。

## 提交代码
- **修复错误**：如果你有能力修复某个已知的问题，可以先在本地环境中进行修复，然后将修复后的代码提交到项目仓库。请确保你的代码符合项目的编码规范，并且通过了所有相关的测试。
- **添加新功能**：如果你想要为锂语言添加新的功能或特性，建议先与项目维护者进行沟通，了解项目的整体规划和需求。在得到认可后，你可以开始编写代码，并在完成后提交一个“Pull Request”。
- **优化代码**：如果你发现锂语言的某些代码可以进行优化，比如提高效率、降低内存占用等，也可以提交优化后的代码。请在提交前确保优化后的代码不会破坏现有的功能，并且通过了所有相关的测试。

## 编写文档
- **完善文档**：帮助完善项目的文档，包括语言的语法说明、使用教程、API文档等。清晰、详细的文档对于开发者和用户来说非常重要。
- **编写教程**：编写一些关于如何使用锂语言的教程，比如入门教程、高级特性教程、最佳实践等，帮助用户更好地学习和使用锂语言。

## 社区参与
- **回答问题**：在项目的社区论坛或讨论组中，积极回答其他用户的问题，分享你的经验和知识。
- **参与讨论**：参与项目相关的讨论，提出你的见解和想法，与社区成员一起探讨锂语言的发展方向和改进方案。

感谢你的贡献！对于任何有效的贡献，我们都会给予认可和感谢。

# 联系我们
## 邮箱
- **Unreal**：3775359187@qq.com