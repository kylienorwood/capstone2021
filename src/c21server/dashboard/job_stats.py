from redis import Redis
r = Redis()

def get_jobs_stats():
    jobs_waiting = int(r.hlen('jobs_waiting'))
    jobs_in_progress = int(r.hlen('jobs_in_progress'))
    jobs_done = int(r.hlen('jobs_done'))
    jobs_total = jobs_waiting + jobs_in_progress + jobs_done
    return {
        'num_jobs_waiting': jobs_waiting,
        'num_jobs_in_progress': jobs_in_progress,
        'num_jobs_done': jobs_done,
        'jobs_total': jobs_total
    }
