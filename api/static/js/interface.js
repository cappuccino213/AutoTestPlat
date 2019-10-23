var interface=[
    {
        "parameter": "--collect-only",
        "description": "只收集测试，不执行测试"
    },
    {
        "parameter": "----maxfail=num",
        "description": "在第一次num失败或错误之后退出"
    },
    {
        "parameter": "--last-failed",
        "description": "当一个或者多个测试失败时，我们常常希望能够定位到最后一个失败的测试用例重新运行"
    },
    {
        "parameter": "--failed-first",
        "description": "此选项与上面的--lf（--last-failed）选项的作用基本相同，不同之处在于--ff会运行完剩余的测试用例"
    },
    {
        "parameter": "--verbose",
        "description": "输出的信息会更详细。最明显的区别就是每个文件中的每个测试用例都占一行，测试的名字和结果都会显示出来，而不仅仅是一个点或字符"
    },
    {
        "parameter": "--quiet",
        "description": "该选项的作用与-v/--verbose的相反，它会简化输出信息"
    },
    {
        "parameter": "--tb=style",
        "description": "决定捕捉到失败时输出信息的显示方式。某个测试用例失败后，pytest会列举出失败信息，包括失败出现在哪一行、是什么失败、怎么失败的，此过程我们称之为“信息回溯”。大多数情况下，信息回溯是有必要的，它对找到问题很有帮助，但有时也会对多余的信息感到厌烦，这时--tb=style选项就有用武之地了。常用的style类型有short、line、no。short模式仅输出assert的一行以及系统判定内容（不显示上下文）；line模式只使用一行输出显示所有的错误信息；no模式则直接屏蔽全部回溯信息"
    },
    {
        "parameter": "--disable-warnings",
        "description": "禁用警告"
    }
];