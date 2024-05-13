#!/usr/bin/python3
import cmd


class Shell(cmd.Cmd):
    """nljaskldasj

    Args:
        cmd (_type_): _description_

    Returns:
        _type_: _description_
    """
    intro = "Welcome to my customized interactive shell"

    def do_EOF(self, line):
        print()
        return True


if __name__ == '__main__':
    print(Shell().do_EOF.__doc__)
    Shell().cmdloop()
