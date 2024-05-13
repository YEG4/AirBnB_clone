#!/usr/bin/python3
import cmd


class Shell(cmd.Cmd):

    intro = "Welcome to my customized interactive shell"

    def do_EOF(self, line):
        print()

        return True


if __name__ == '__main__':
    Shell().cmdloop()
