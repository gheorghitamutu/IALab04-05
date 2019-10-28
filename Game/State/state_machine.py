class StateMachine:
    def __init__(self):
        self.__stack_states = []
        self.__new_state = None

        self.__is_removing = False
        self.__is_adding = False
        self.__is_replacing = False

    def add_state(self, new_state, is_replacing):
        self.__new_state = new_state
        self.__is_adding = True
        self.__is_replacing = is_replacing

    def remove_state(self):
        self.__is_removing = True

    def process_state_changes(self):
        if self.__is_removing and len(self.__stack_states) != 0:
            self.__stack_states.pop()

            if len(self.__stack_states) != 0:
                self.__stack_states[-1].resume()

            self.__is_removing = False

        if self.__is_adding:
            if len(self.__stack_states) != 0:
                if self.__is_replacing:
                    self.__stack_states.pop()
                else:
                    self.__stack_states[-1].pause()

            self.__stack_states.append(self.__new_state)
            self.__stack_states[-1].init()
            self.__is_adding = False

    def get_active_state(self):
        return self.__stack_states[-1]  # simulate stack.top()

