# Lith 语言 API 文档
**针对开发/调试人员使用的 API 概述**
## 概述

Lith 是一种基于 Python 的编程语言，旨在简洁且可扩展。本文件提供了 API 的概述，包括其组件、类和方法。

## 目录

1. [常量](#常量)
2. [错误处理](#错误处理)
3. [词法分析器](#词法分析器)
4. [解析器](#解析器)
5. [节点](#节点)
6. [运行时结果](#运行时结果)
7. [值](#值)
8. [函数](#函数)
9. [上下文和符号表](#上下文和符号表)
10. [解释器](#解释器)
11. [运行程序](#运行程序)

## 常量

- **DIGITS**: 包含所有数字字符的字符串（`'0123456789'`）。
- **LETTERS**: 包含所有字母字符（大小写）的字符串。
- **LETTERS_DIGITS**: 字母和数字的组合。
- **VERSION**: 当前的 Lith 语言版本（`'L0.1.1'`）。
- **AUTHOR**: 语言的作者（`'UNREAL'`）。
- **LNAME**: 语言的名称（`'Lith'`）。

## 错误处理

### 类

- **Error**: 所有错误类型的基类。
  - **IllegalCharError**: 针对代码中的非法字符引发的错误。
  - **ExpectedCharError**: 当缺少预期字符时引发的错误。
  - **InvalidSyntaxError**: 针对无效语法引发的错误。
  - **RTError**: 在运行时错误，包含回溯信息。

### 方法

- `as_string()`: 返回错误的字符串表示。

## 词法分析器

### 类: `Lexer`

`Lexer` 类负责将输入文本进行词法分析。

#### 方法

- `__init__(fn, text)`: 使用文件名和文本初始化词法分析器。
- `advance()`: 前进到输入中的下一个字符。
- `make_tokens()`: 从输入文本生成一个令牌列表。

## 解析器

### 类: `Parser`

`Parser` 类负责将令牌解析为抽象语法树（AST）。

#### 方法

- `__init__(tokens)`: 使用令牌列表初始化解析器。
- `parse()`: 将令牌解析为 AST。
- `statements()`: 解析多个语句。
- `statement()`: 解析单个语句。
- `expr()`: 解析表达式。
- 其他用于解析特定结构的方法（例如 `if_expr`、`for_expr`、`while_expr` 等）。

## 节点

### 类

- **NumberNode**: 表示 AST 中的数字。
- **StringNode**: 表示 AST 中的字符串。
- **ListNode**: 表示 AST 中的列表。
- **VarAccessNode**: 表示 AST 中的变量访问。
- **VarAssignNode**: 表示 AST 中的变量赋值。
- **BinOpNode**: 表示 AST 中的二元操作。
- **UnaryOpNode**: 表示 AST 中的单元操作。
- **IfNode**: 表示 AST 中的 if 语句。
- **ForNode**: 表示 AST 中的 for 循环。
- **WhileNode**: 表示 AST 中的 while 循环。
- **FuncDefNode**: 表示 AST 中的函数定义。
- **CallNode**: 表示 AST 中的函数调用。
- **ReturnNode**: 表示 AST 中的返回语句。
- **ContinueNode**: 表示 AST 中的继续语句。
- **BreakNode**: 表示 AST 中的中断语句。

## 运行时结果

### 类: `RTResult`

`RTResult` 类用于处理运行时执行过程中的结果。

#### 方法

- `reset()`: 重置结果状态。
- `register(res)`: 注册一个结果。
- `success(value)`: 将结果标记为成功。
- `failure(error)`: 将结果标记为失败。
- `should_return()`: 检查结果是否指示返回。

## 值

### 类

- **Value**: 所有值的基类。
- **Number**: 表示数值。
- **String**: 表示字符串值。
- **List**: 表示值的列表。

### 方法

- 算术和比较操作（例如 `added_to`、`subbed_by` 等）在 `Value` 类及其子类中定义。

## 函数

### 类: `BaseFunction`

用户定义和内置函数的基类。

#### 方法

- `generate_new_context()`: 为函数生成新的执行上下文。
- `check_args(arg_names, args)`: 检查传递给函数的参数数量。
- `populate_args(arg_names, args, exec_ctx)`: 在上下文中填充函数的参数。

### 类: `Function`

表示用户定义的函数。

### 类: `BuiltInFunction`

表示内置函数。

## 上下文和符号表

### 类: `Context`

表示执行上下文，包括符号表。

### 类: `SymbolTable`

管理变量名称及其对应的值。

#### 方法

- `get(name)`: 从符号表中检索值。
- `set(name, value)`: 在符号表中设置值。
- `remove(name)`: 从符号表中移除值。

## 解释器

### 类: `Interpreter`

`Interpreter` 类执行 AST。

#### 方法

- `visit(node, context)`: 访问 AST 中的节点并执行它。
- 访问特定节点类型的其他方法（例如 `visit_NumberNode`、`visit_VarAccessNode` 等）。

## 运行程序

### 函数: `run(fn, text)`

执行 Lith 程序。

#### 参数

- `fn`: 脚本的文件名。
- `text`: 脚本内容的字符串。

#### 返回值

- 包含结果值和在执行过程中发生的任何错误的元组。

---

本文件提供了 Lith 语言 API 的高层次概述。有关详细用法和示例，请参考源代码和其他资源。
