def send_task(task_id, **kwargs):
    from .models import Tasks
    from django.utils import timezone
    from datetime import timedelta, datetime

    task = Tasks.objects.get(id=task_id)
    print(f"Message : {task.message}")
    
    current_count = task.number_repeat
    task.number_repeat -= 1
    
    if task.number_repeat <= 0:
        task.is_done = True
    
    task.save()  

    response = {
        "message": task.message,
        "time_added": task.date_added.isoformat() if task.date_added else None,
        "number_of_times_left": current_count,
        "time_stamp": datetime.now().isoformat()   
    }

    return response