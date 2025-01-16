# 锂语言/Lith Language

## 项目简介
锂语言（Lith）是一种基于Python进行扩展的编程语言（库），旨在提供更为精炼和高效的编程体验。目前，锂语言仍处于开发阶段，部分功能尚不完善，但已具备基本的语法结构和运行时环境。

*tips*:本语言部分技术来自YouTube@davidcallanan。语言大多数命令均为大写。

**许可证**：本项目遵循在`29 June 2007`发布的`Version 3`版本的`GNU GENERAL PUBLIC LICENSE`

# Lith 语言更新日志
#### L0.1.4
- **网络操作**：调用`ddos(ip, thread, datapackage_size, executions)`可实现向目标发送UDP数据包，执行executions次。**（慎用）**
- **内容追加**：调用`append_to_file(file_path, content)`来在指定文件后面追加内容。
- **字典操作**：调用`merge_dicts(*dicts)`合并多个字典，简化了字典合并的代码，提高开发效率。
- **列表去重**：调用`unique_list(lst)`去除列表中的重复元素，同时保持原有顺序，适用于需要去重但又希望保留元素顺序的场景。
- **时间转换**：调用`timestamp_to_datetime(timestamp)`将时间戳转换为datetime对象，便于进行更复杂的时间操作和格式化。
- **字符串格式化**：调用`format_string(template, **kwargs)`使用关键字参数格式化字符串，使字符串格式化更加灵活和可读。
- **路径操作**：调用`create_directory(path)`创建目录，如果目录已存在则不报错，简化了目录创建的代码，避免了重复创建目录的错误。
- **随机数生成**：调用`random_int(min_val, max_val)`生成指定范围内的随机整数，方便进行随机数相关的操作和测试。
- **数据排序**：调用`sort_dict_by_value(d, reverse=False)`根据字典的值进行排序，返回排序后的字典，适用于需要根据字典值进行排序的场景。
- **异常处理**：调用`safe_divide(a, b)`进行安全除法，避免除以零的错误，返回合适的值，提高了代码的健壮性。
- **命令行参数解析**：调用`parse_arguments()`解析命令行参数，支持输入和输出文件路径的参数，方便从命令行接收用户输入。
- **配置文件读取**：调用`load_config(file_path)`从JSON文件中加载配置，简化了配置文件读取的代码，方便进行程序配置的管理和使用。
- 修复了一些已知问题。

#### L0.1.4rc1(预发布)
- 修复了一些已知问题。
- 增加了一些帮助性命令。

#### L0.1.4-Beta(测试版本)
- 修复了一些已知问题。

#### L0.1.4-Alpha(测试版本)
- **元素存在性检查**：在`ChemicalFormulaChecker`类中新增了一个`element_exists`方法，用于检查指定元素是否在任何化学方程式中出现。
- **运算优化**：在调用数学运算时，化简了像`math.sin(60)`这样的代码，改为`sin(60)`，也包含了cot等函数。
- **文件操作**：该为了较为简洁的操作。
- **远端请求**：化简合并了原`request`请求。

#### L0.1.3
- **实验性GUI支持**：引入了一个新的实验性GUI，允许用户通过图形界面与Lith程序交互。
- **帮助文档**：新增了一个`help()`函数，用户可以通过调用该函数获取锂语言的帮助信息。

#### L0.1.2
- 增加了对列表和字典的支持。
- 优化了词法分析器的性能。

#### L0.1.1
- 初始公开发布版本，支持基本的算术运算和控制结构。

## 安装指南
### Python环境
- 确保已安装Python 3.x版本。可通过在终端运行`python --version`或`python3 --version`来检查Python版本。
- 若未安装Python，可访问[Python官网](https://www.python.org/downloads/)下载并安装适合您操作系统的Python版本。

### 锂语言环境
- 克隆或下载本项目仓库到本地。
- 在项目根目录下，打开终端或命令提示符。
- 运行`pip install .`将锂语言添加到Python环境变量（别问我为什么不用pypi，因为太复杂）。

## 代码示例
### 基本语法
- 首先，让我们导入`Lith Language`。
```python
from lith import *
```
或者
```python
import lith #不推荐
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

### 新特性

- **元素存在性检查**：在`ChemicalFormulaChecker`类中新增了一个方法`element_exists`，该方法用于检查指定元素是否在任何已添加的化学方程式中出现，并返回布尔值。
示例代码（L0.1.4-A第一轮测试）：
```python
# 测试 list_elements 和 listnum_elements 函数
element_to_check = "H"
print(f"包含元素 '{element_to_check}' 的化学方程式: {checker.list_elements(element_to_check)}")
print(f"包含元素 '{element_to_check}' 的化学方程式数量: {checker.listnum_elements(element_to_check)}")

element_to_check = "O"
print(f"包含元素 '{element_to_check}' 的化学方程式: {checker.list_elements(element_to_check)}")
print(f"包含元素 '{element_to_check}' 的化学方程式数量: {checker.listnum_elements(element_to_check)}")

# 测试 chem 函数
test_elements = ["H", "He", "Xx", "O", "Na", "Zz"]
for elem in test_elements:
    print(f"元素 '{elem}' 是否有效: {checker.chem(elem)}")
```
- **简化数学**：在库中已经包含了许多数学模块，包括但不限于`cot(x)`、`sqrt(x)`。以下是一些使用方法。
  - **正弦**
  ```python
  y = sin(x)
  ```
  - **余弦**
  ```python
  y = cos(x)
  ```
  - **正切**
  ```python
  y = tan(x)
  ```
  - **余切**
  ```python
  y = cot(x)
  ```
  - **平方根**
  ```python
  y = sqrt(x)
  ```
  - **指数函数**
  ```python
  y = exp(x)
  ```
  - **对数**
  ```python
  y = log(x)
  ```
  - **阶乘**
  ```python
  y = factorial(x)
  ```
  - **幂次函数**
  ```python
  y = power(x, a) # 计算x的a次方
  ```
  - **绝对值**
  ```python
  y = abs_value(x)
  ```
  - **最大公约数**
  ```python
  y = gcd(x, a) # 计算a和b的最大公约数
  ```
  - **最小公倍数**
  ```python
  y = lcm(x, a) # 计算a和b的最小公倍数
  ```
- **文件操作**：改进了原python使用的`with open(代码省略)`，转为使用`r_file(filename)`读取和`w_file(filename)`写入。示例：
```python
x = r_file('exp.txt')
print(x) # 打印exp.txt的内容
```
- **远端请求**：化简合并了原`request`请求。示例：
```python
x = send_request("http://exp.com/data", method='GET')
print(x) # 使用GET方法向http://exp.com/data请求数据。
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

# 后记
## 为什么要编写Lith？
- Lith设计的初衷就是优化当前版本Python的语法，并不是为了盈利。
- 我们也没有打算将Lith进行收费。

## Lith命名的由来是什么？
- Lith，全名Lithium。而Lith在希腊语中翻译为“石”，寓意着Lith的坚固可靠。
- 锂是最轻的碱金属元素，代表着Lith的轻便性。

## Lith语言是完全由Unreal开发的吗？
- **不是**，Lith并非完全由Unreal编写。

### Lith将保持开源在Github，后续将在Gitee上发布1.0.x版本（预计）。

# 联系我们
## 项目地址
- **Github**：https://github.com/svila-ylym/LithLanguage
## 邮箱
- **Unreal**：3775359187@qq.com