#
# import psutil
# import os
# import errno
# import signal
#
#
# def pid_exists(pid):
#     if psutil:
#         return psutil.pid_exists(pid)
#
#
#     if pid == 0:
#         return True
#     try:
#         os.kill(pid, 0)
#     except OSError as err:
#         if err.errno == errno.ESRCH:
#             return False
#         elif err.errno == errno.EPERM:
#             return True
#         else:
#             raise err
#     else:
#         return True
#
#
#
# pid = 87015
#
#
# print(pid_exists(pid))
#
# os.kill(pid, signal.SIGTERM)
#
# print(pid_exists(pid))
#
#
# os.kill(pid, 0)
# print(pid_exists(pid))
import os

def child():
    print 'A new child:', os.getpid()
    print 'Parent id is:', os.getppid()
    os._exit(0)

def parent():
    while True:
        newpid=os.fork()
        print newpid
        if newpid==0:
            child()
        else:
            pids=(os.getpid(),newpid)
            print "parent:%d,child:%d"%pids
            print "parent parent:",os.getppid()
        if raw_input()=='q':
            break

parent()
