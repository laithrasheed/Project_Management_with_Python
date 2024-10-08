import ipywidgets as widgets
from IPython.display import display

# Create main checklist items
task1 = widgets.Checkbox(value=False, description='Task 1')
task2 = widgets.Checkbox(value=False, description='Task 2')
task3 = widgets.Checkbox(value=False, description='Task 3')

# Create sub-checklist items for task1
subtask_A = widgets.Checkbox(value=False, description='Task 1A')
subtask_B = widgets.Checkbox(value=False, description='Task 1B')
subtask_C = widgets.Checkbox(value=False, description='Task 1C')
subtask_D = widgets.Checkbox(value=False, description='Task 1D')
subtask_E = widgets.Checkbox(value=False, description='Task 1E')

# Group subtasks under task1 with indentation using VBox and layout
subtasks_layout = widgets.VBox(
    [subtask_A, subtask_B, subtask_C, subtask_D, subtask_E],
    layout=widgets.Layout(padding='0 0 0 20px')  # Add padding to the left to indent subtasks
)

# Group task1 with its subtasks
task1_group = widgets.VBox([task1, subtasks_layout])

# Group all main tasks including task1 with its subtasks
checklist = widgets.VBox([task1_group, task2, task3])

# Display the checklist
display(checklist)

