class TaskFlowError(Exception):
    pass

class ValidationError(TaskFlowError):
    pass

class EmptyTaskTitleError(ValidationError):
    pass

class DatabaseError(TaskFlowError):
    pass