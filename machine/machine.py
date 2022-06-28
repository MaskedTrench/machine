"""
Machine module
==============
    Provides exactly the state machine, which can be accessed from machine package.
"""

from typing import Any, List
from threading import Thread


class Machine(object):
    """
    Machine class
    =============
    """


    debug_flag: bool            = True
    states:     List[str]       = []
    callables:  List[object]    = []


    def __init__(self):
        ...


    def log_msg(self, t: str):
        if self.debug_flag:
            print(f'[DEBUG] {t}')


    def on(self, event_name: str, do: function):
        if event_name not in self.states:
            self.states.append(event_name)
            self.callables.append(do)
            return

        index = self.states.index(event_name)
        is_arr = type(self.callables[index])
        if is_arr == list:
            self.callables[index].append(do)
            return

        stored_do = self.callables[index]
        self.callables[index] = [stored_do, do]


    def trigger(self, event_name: str):
        if event_name not in self.states:
            return

        index = self.states.index(event_name)
        do = self.callables[index]
        if type(do) == list:
            for i in do:
                i()
            return

        do()


    def prevent(self, event_name: str, do: function):
        if event_name not in self.states:
            self.on(event_name, do)
            return

        index = self.states.index(event_name)
        self.callables[index] = do


