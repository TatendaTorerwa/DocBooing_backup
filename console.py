#!/usr/bin/python3
"""The console module."""

import cmd

class DocBookingCommand(cmd.Cmd):
    prompt = "(BookingDoc) > "

    def emptyline(self):
        """Reprompts when user press Enter on an empty line."""
        pass

    def do_quit(self, arg):
        """quit to exit the cmd loop"""
        return True
        
        """aliasing."""
        do_exit = do_quit

    def do_EOF(self, arg):
        """Control D to successfully exit loop."""
        print()
        return True

if __name__ == "__main__":
    DocBookingCommand().cmdloop()
